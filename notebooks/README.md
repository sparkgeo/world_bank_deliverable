# World Bank Notebooks

Here you'll find various notebooks created by Sparkgeo.
## Notebooks


`gps_data` - Data cleaning of the Beitbridge Truck Data.

`Extract_dates` - extract dates from news articles and GPS data

`gps_eda` - explore border wait time data with plots and summary statistics

`gps_modelling` - timeseries modelling for border wait time (incomplete)

`MS_OSM_Data_download` - Retrieving Microsoft Buildings, Google Open Buildings and OSM Data.

`tdi/tdi-notebook` - How to calculate TDI from Planetscope Imagery

`tdi/skywatch-api-notebook` - How to set up a query for skywatch api ordering

`tdi/tdi_documentation` - Detailed instructions on the workflows and methodologies of the above tdi notebooks.

`yolo.qmd` - How to count cars from an image.
## Folder Structure

- ../data
    - raw 
    - processed
- notebooks
    - data science notebooks
    
  - outputs
      - outputs of any notebooks
- src
    - for scripts

## Conda or Mamba

To build the environment from a `yml` file using mamba (recommended)

`mamba env create -f environment.yml`

## R Projects

To replicate the R environment, you can simply `install.packages('renv')` and open up the R Project file and run `renv::restore()` to restore the `renv` lockfile to load in all the appropriate libraries.

## Quarto

(Quarto)[https://quarto.org/] is an open-source scientific and technical publishing system.

Review (Quarto's Quickstart)[https://quarto.org/docs/get-started/] for installation instructions.


To regenerate outputs from Quarto:

`quarto render hello.ipynb --to html`

`quarto render hello.ipynb --to docx`