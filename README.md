# World Bank Group Delivery from Sparkgeo

This repository holds the deliverables that will be given to the World Bank Group (WBG). There are several components to this that are broken up into various directories.
Some of this work may be incomplete, as the project ended before implementation.
## Demo

View the notebook demo website [here](https://sparkgeo.quarto.pub/sparkgeo---world-bank-demo/)

## Structure

-   **darknet**: This directory holds the Python 3 interface to Darknet. It has been modified for use by Sparkgeo.
-   **data**: This directory holds raw and processed data to be used in the notebooks, in addition to test data that can be used to verify operation.
-   **lib**: Compiled libraries that are necessary for the Python 3 interface. Provided are shared libraries for x86-64 Linux and Arm-based OS-X.
-   **model**: Example model to run. This model was trained on a custom merged dataset.
-   **notebooks**: Notebooks to perform various processing on data.
-   **src**: Stand-alone Python 3 programs.

## Getting Started

### Prerequisites

The best way to run the notebooks and Python applications provided is to create a virtual environment with

``` sh
mkvirtualenv -p python3 worldbank
```

Inside the virtual environment, run

``` sh
pip install -r requirements.txt
```

This should install all of the required Python modules into the virtual environment.

## Usage

For the provided example applications, activate the virtual environment and then run one in this fashion:

``` sh
python src/count_cars.py --detection-file data/processed/test_cars.gpkg --intersect-file data/processed/beitbridge_road_mask_v2.gpkg --output-json cars.geojson
```

Please see the readme in the notebooks directory for their usage.
