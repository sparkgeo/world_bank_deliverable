# Trained YOLOv4-Tiny Darknet Model

This directory contains a trained YOLOv4-tiny model in the darknet format.  It was trained on a custom merged dataset.  This model only achieves a 55% validation accuracy due to the project being cut short.  

This directory contains the following files:
* **yolov4-tiny-custom_best.weights**: The actual weights file generate by darknet.
* **yolov4-tiny-custom.cfg**: The YOLOv4-tiny config file that was used to generate this model.
* **yolov4-tiny.data**: Darknet-formatted data file that defines paths for various things.
* **yolov4-tiny.names**: Object class labes for the model.