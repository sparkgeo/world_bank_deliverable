# World Bank Group Delivery from Sparkgeo

This repository holds the deliverables that will be given to the World Bank Group (WBG). There are several components to this that are broken up into various directories.
Some of this work may be incomplete.
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

# Installation

First `clone` this repository to your local environment.

To run the notebooks locally you need to install the environments for `R` , `Quarto` and `Python`.

## Python

### Conda or Mamba

To build the environment from a `yml` file using mamba (recommended)

`mamba env create -f environment.yml`

### Usage

Once activating your conda environment:

`conda activate wb-spk-env`
You should be able to run the `.ipynb` notebooks.

For the provided example applications, activate the virtual environment and then run one in this fashion:

```sh
python src/count_cars.py --detection-file data/processed/test_cars.gpkg --intersect-file data/processed/beitbridge_road_mask_v2.gpkg --output-json cars.geojson
```

Please see the Readme in the notebooks directory for their usage.

### R Projects

To replicate the R environment, you can simply `install.packages('renv')` and open up the R Project file and run  `renv::restore() ` to restore the  `renv ` lockfile to load in all the appropriate libraries.

### Usage

Restoring the `renv` above will allow you to run any `.qmd` notebooks.

## Quarto

[Quarto](https://quarto.org/) is an open-source scientific and technical publishing system.

Review [Quarto's Quickstart](https://quarto.org/docs/get-started/) for installation instructions.

To regenerate outputs from Quarto:

`quarto render hello.ipynb --to html`

`quarto render hello.ipynb --to docx`
