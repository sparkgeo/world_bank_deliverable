# Stand-alone Python Applications

In this directory are stand-alone Python 3 applications that can be run.  Please see the information in the main README.md file for installation instructions.

* **count_cars.py**: This application takes in a detected GeoJSON or Geopackage file and a file defining an area and counts the number of cars in that area.  It includes confidence and other supporting information.
* **get_bounding_boxes.py**: This application takes a trained YOLO model and runs it against an input image, returning a JSON containing the image coordinates of the detections.
* **get_bounding_detections.py**: This file takes in a georeferenced image, runs the model against it, and then outputs a GeoJSON that contains the areas of the images containing detections.