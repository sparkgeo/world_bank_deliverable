#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Application to interset detection bouding boxes against an AOI.

This application will interset the passed-in geojson of detections against an
AOI 
"""

import geopandas
import geojson
import argparse

def main():
    """Main function
    """

    # Argument parsing
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--detection-file", type=str, required=True, help="Path to the detection file.")
    ap.add_argument("-i", "--intersect-file", type=str, required=True, help="Path to the intersection file.")
    ap.add_argument("-o", "--output-json", type=str, required=True, help="Output JSON file to write.")
    args = vars(ap.parse_args())
    
    try:
        # Load the files
        detection_df = geopandas.read_file(args["detection_file"])
        intersect_df = geopandas.read_file(args["intersect_file"])

        # Create our intersection data
        intersection_df = geopandas.overlay(detection_df, intersect_df, how="intersection")
        
        # Reproject so we can get our area in meters
        intersection_df = intersection_df.to_crs(epsg=3857)

        # Calculate our areas
        area = intersection_df.area

        # Add the areas to the intersection dataframe
        intersection_df = intersection_df.assign(area=area)

        # Print our statistics
        print(f"Total area occupied in the input detection file: {detection_df.to_crs(epsg=3857).area.sum()} square meters")
        print(f"Total area of the intersection file: {intersect_df.to_crs(epsg=3857).area.sum()} square meters")
        print(f"Total area of the objects in the intersections: {area.sum()} square meters")

        print(f"Number of vehicles inside the roads area: {len(intersection_df.index)}")

        # Print out each row in the intersection dataframe
        print("Individual areas of the intersection")
        for index, row in intersection_df.iterrows():
            print(f"Class: {row['class']} Confidence: {row['confidence']} Area: {row['area']} square meters")

        # Write to a file
        with open(args["output_json"], "w") as outjson:
            outjson.write(intersection_df.to_json())

    except Exception as e:
        print(f"Got exception {e} during processing.")

if __name__ == "__main__":
    main()