# Darknet Python Module

This module contains the Python 3 interface to darknet as provided by the main Darknet project.  It has been modified by Sparkgeo in the following ways:

* Modified to load the appropriate shared library based on if it is run on a ARM OS-X instance or a x86-64 Linux instance.
* generate_darknet_image was added to create a "darknet-formatted" image to Python callers.