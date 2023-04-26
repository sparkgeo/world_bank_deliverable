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

In this Dockerfile, we start from a base Ubuntu 20.04 LTS image and set the working directory to `/`. We then install system packages that will be necessary for building and running some of the libraries we need.

Next, we install Miniconda and use it to install mamba. We set the PATH environment variable to include the Miniconda executable so we can use it later.

We copy the environment.yml file to the container and use mamba to create a conda environment called my_env based on the specifications in environment.yml. We then set up renv by installing it with remotes::install_github().

We set the PATH environment variable to include the R executable within the my_env environment. We then use pip to install Jupyter and Quarto, two notebook environments that can run both R and Python code.

Finally, we expose port 8888 for Jupyter Notebook and start it with a command that specifies the IP and port to listen on and disables the browser.

Make sure to replace environment.yml with your own environment file and modify any other settings as needed.

Build the docker container

`docker build -t wbnb .`

Once the image has finished building, you can start a container using the following command:

`docker run -p 8888:8888 wb-spk-env`

This command maps port 8888 in the container to port 8888 on your computer so you can access the Jupyter Notebook running in the container.

To access Quarto, you'll need to start a new notebook with the Quarto kernel. Here's how:

Open a web browser and navigate to http://localhost:8888.
Click the "New" button in the upper right corner and select "Quarto" from the dropdown menu.
A new Quarto notebook will open. You can use this notebook to write and render Quarto documents.


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

