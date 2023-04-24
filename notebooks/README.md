# World Bank Notebooks

Here you'll find various notebooks created by Sparkgeo.
## Notebooks


`gps_data` - Data cleaning of the Beitbridge Truck Data.

`Extract_dates` - extract dates from news articles and GPS data

`gps_eda` - explore border wait time data with plots and summary statistics

`gps_modelling` - timeseries modelling for border wait time (incomplete)

`MS_OSM_Data_download` - Retrieving Microsoft Buildings, Google Open Buildings and OSM Data.

`tdi/tdi-notebook` - How to calculate TDI from Planetscope Imagery


TODO:
`Object Detection` - call `.py` test image `--output` with output folder, results, save

## Folder Structure

- ../data
    - raw 
    - processed
- notebooks
    - data science notebooks
    
  - _outputs
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
## Docker

Build the docker container

`docker build -t wbnb .`

Run the docker container and jupyter notebook from port 8888 from your active directory and share the volumnes 

`docker run --name wbnb -p 8888:8888 -v $(pwd):/home/jovyan/work .`

“-v” ( — volume) tag in our “docker run …” command to mount the host storage and bind it with the storage of `wbnb`

Additionally, you can just run the notebooks in iterative mode:

`docker run -it -p 8888:8888 jupyter/scipy-notebook:0fd03d9356de`

`docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work wbnb`

`docker run -it --rm \
    -p 8888:8888 \
    -v <my-vol>:<container-dir> \
    jupyter/minimal-notebook:latest`

All in one to build directly from environment file:

`docker run -p 8888:8888 --name notebook -v /notebooks/:/home/jovyan/work --environment.yml .env -it wbnb`

