#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Application to retrieve the bounding boxes from Darknet.

This application will run a darknet model against a passed in image and create a JSON file
with the bounding boxes found.
"""

import argparse
import cv2
import os
import json
import sys
pdir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(pdir)
from darknet import darknet


# Our template string for each JSON item
template_str = """
{{
    "label": "{}",
    "confidence": {},
    "left": {},
    "top": {},
    "right": {},
    "bottom": {}
}}
"""

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

        detections = darknet.detect_image(darknet_network, darknet_classes, darknet_image)

        # Deallocate our input image
        darknet.free_image(darknet_image)

        # Open our output image
        with open(args["output_json"], "w") as output_file:
            output_file.write("[")
            # Iterate through our detections, convert our coordiantes to image coordinates, and output our json
            for label, confidence, bounding_box in detections:
                # Convert our coordinates to actual image coordinates
                left, top, right, bottom = darknet.bbox2points(bounding_box)
                left, top, right, bottom = int(left * ratio_width), int(top * ratio_height), int(right * ratio_width), \
                    int(bottom * ratio_height)
                

                # Generate our JSON string for the item.
                json_string = template_str.format(label, confidence, left, top, right, bottom)

                # Convert to a dict
                json_dict = json.loads(json_string)

                # write it
                json.dump(json_dict, output_file)
                output_file.write(",\n")
            output_file.write("]\n")

        print("JSON generated")


    except Exception as e:
        print(f"Got exception {e} during runtime.")

if __name__ == "__main__":
    main()