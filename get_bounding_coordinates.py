#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Application to retrieve the bounding boxes from Darknet.

This application will run a darknet model against a passed in image and create a JSON file
with the bounding boxes found.
"""


from darknet import darknet
from osgeo import gdal
from osgeo import osr 
import argparse
import cv2
import os
import json
import geojson

def generate_polygon(in_geo_transform: list, left: int, top: int, right: int, bottom: int) -> geojson.Polygon:
    """Convert the passed-in coordinates to a GeoJSON polygon

    Args:
        in_geo_transform (list): Input list of coordinates from GDAL
        left (int): Upper-left X
        top (int): Upper-left Y
        right (int): Lower-right X
        bottom (int): Lower-right Y

    Returns:
        geojson.Polygon: GeoJSON Polygon object
    """

    coordinate_list = list()
    ulx = in_geo_transform[0]
    uly = in_geo_transform[3]
    pixel_width = in_geo_transform[1]
    pixel_height = in_geo_transform[5]

    # Upper left
    temp_x = ulx + left * pixel_width
    temp_y = uly + top * pixel_height
    coordinate_list.append([temp_x, temp_y])

    # Top right
    temp_x = ulx + right * pixel_width
    temp_y = uly + top * pixel_height
    coordinate_list.append([temp_x, temp_y])

    # Bottom right
    temp_x = ulx + right * pixel_width
    temp_y = uly + bottom * pixel_height
    coordinate_list.append([temp_x, temp_y])

    # Bottom left
    temp_x = ulx + left * pixel_width
    temp_y = uly + bottom * pixel_height
    coordinate_list.append([temp_x, temp_y])

    # Upper left
    temp_x = ulx + left * pixel_width
    temp_y = uly + top * pixel_height
    coordinate_list.append([temp_x, temp_y])

    return geojson.Polygon([coordinate_list])      

def main():
    """Main function
    """

    # Argument parsing
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--data-file", type=str, required=True, help="Path to the data definitions file.")
    ap.add_argument("-c", "--config-file", type=str, required=True, help="Path to the model configuration file.")
    ap.add_argument("-n", "--names-file", type=str, required=True, help="Path to the model names file.")
    ap.add_argument("-w", "--weights-file", type=str, required=True, help="Path to the pre-trained model weights file.")
    ap.add_argument("-i", "--input-image", type=str, required=True, help="Input image to run detection on.")
    ap.add_argument("-o", "--output-json", type=str, required=True, help="Output JSON file to write.")
    ap.add_argument("-t", "--threshold", type=str, default=0.4, help="Threshold [0, 1].")
    args = vars(ap.parse_args())

    # Make sure our files exist
    if not os.path.exists(args["data_file"]):
        print(f"Data file {args['data_file']} cannot be found.")

    if not os.path.exists(args["config_file"]):
        print(f"Data file {args['config_file']} cannot be found.")

    if not os.path.exists(args["names_file"]):
        print(f"Data file {args['names_file']} cannot be found.")

    if not os.path.exists(args["weights_file"]):
        print(f"Data file {args['weights_file']} cannot be found.")

    if not os.path.exists(args["input_image"]):
        print(f"Data file {args['input_image']} cannot be found.")

    try:
        # Load our image using opencv
        input_image = cv2.imread(args["input_image"])

        darknet_network, darknet_classes, darknet_colors = darknet.load_network(args["config_file"], args["data_file"], 
                                                                                args["weights_file"])

        network_width = darknet.network_width(darknet_network)
        network_height = darknet.network_height(darknet_network)

        darknet_image, ratio_width, ratio_height = darknet.generate_darknet_image(input_image, network_width, 
                                                                                  network_height)

        detections = darknet.detect_image(darknet_network, darknet_classes, darknet_image, args["threshold"])

        # Deallocate our input image
        # darknet.free_image(darknet_image)

        # Open the input image using gdal
        geo_image = gdal.Open(args["input_image"])
        
        # Get our projection parameters
        image_projection = geo_image.GetProjection()
        image_srs = osr.SpatialReference()
        image_srs.ImportFromWkt(image_projection)


        # Get our transform parameters
        image_geotransform = geo_image.GetGeoTransform()

        feature_list = list()
        identifier = 0
        # Iterate through our detections, convert our coordiantes to image coordinates, and output our json
        for label, confidence, bounding_box in detections:
            # Convert our coordinates to actual image coordinates
            left, top, right, bottom = darknet.bbox2points(bounding_box)
            left, top, right, bottom = int(left * ratio_width), int(top * ratio_height), int(right * ratio_width), \
                int(bottom * ratio_height)
            
            # Init our feature dictionary
            feature_dict = dict()
            feature_dict["class"] = label
            feature_dict["confidence"] = confidence
            
            # Generate our polygon geometry object
            polygon_geometry = generate_polygon(image_geotransform, left, top, right, bottom)

            # Create our feature here
            temp_feature = geojson.Feature(id=identifier, geometry=polygon_geometry, properties=feature_dict)

            feature_list.append(temp_feature)
            identifier += 1

        # Write out our feature collection
        feature_collection = geojson.FeatureCollection(feature_list)
        
        with open(args["output_json"], "w") as out_json:
            geojson.dump(feature_collection, out_json)

        print("GeoJSON generated")


    except Exception as e:
        print(f"Got exception {e} during runtime.")

if __name__ == "__main__":
    main()