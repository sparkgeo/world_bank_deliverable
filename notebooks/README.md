# World Bank Notebooks

## Folder Structure

- data
    - raw 
    - processed
- models
    - for model development
- outputs
    - outputs of any notebooks
- notebooks
    - data science notebooks
- src
    - for scripts

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
