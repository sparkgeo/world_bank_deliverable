FROM jupyter/scipy-notebook

WORKDIR /

# Create the environment:
COPY environment.yml .
RUN mamba env create -f environment.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "osm-extract", "/bin/bash", "-c"]

# Demonstrate the environment is activated:
RUN echo "Make sure osmx installed:"
RUN python -c "import osmnx"

# The code to run when container is started:
ENTRYPOINT ["mamba", "run", "--no-capture-output", "-n", "osm-extract"]
EXPOSE 8888
CMD [ "jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root" ]