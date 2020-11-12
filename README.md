
# smilPyGoodies

Some goodies to help use Smil under Python

# Directory Contents

* __smilPyGoodies__  - Python modules

  * __smilPyRead3D__ : this module helps reading 3D images
  * __smilPyPlot__ : this module contains a Matplotlib based GUI.
    This module has two reasons to be :
    * no dependency on Qt libraries;
    * can be used with jupyter notebooks.

* __samplePrograms__ - examples on how to use these goodies

* __examples__ - smilPython examples

* __images__ - some images to play with

# Modules

Take a look in the sample programs to see how to use these modules in your program.

##  smilPyRead3D

  Ce module complements the Smil native read functions, which allows reading 3D images only from images in the RAW format.

  This module allows reading 3D images :
* as a stack of 2D images of the same size and data type;
* TIFF 3D images, both in float or integer data type.

## smilPyPlot

  The first goal of this module is to replace the Qt based graphical user interface, which causes some problems under some Linux distributions.

  Also it can be used on some web kind applications such as jupyter. This isn't possible with the Qt based GUI.

  One of the advantages smilPyPlot is to be able to show more than one image on the same window (or space).

  Two obvious disadvantages are limited interactivity and impossibility to display 3D images, for the moment. 

  Interactivity is limited to, e.g., things like zooming and consulting pixel values.



# Installing

## Requirements

__python3-matplotlib__ - Matplotlib

__PyQt__ - Under Ubuntu, package __python3-pyqt5__

__libtiff__ - To be able to read __3D__ tiff files - Under Ubuntu, packages 
  __libtiff5__, __tifffile__ and (optional) __libtiff-tools__

## Installing

    git clone https://github.com/ensmp-cmm/smilPyGoodies
    cd smilPyGoodies
    cp -pr smilPyGoodies /installation_path/
    
    export PYTHONPATH=/installation_path:${PYTHONPATH}

# Using it (under Python...) :

    import smilPyGoodies as sg

    sg.someFunctionCall...

# Sample programs

Still in the directory where you distribution was cloned, you can just type :

    env PYTHONPATH=$(pwd)/smilPyGoodies:${PYTHONPATH} \
      python samplePrograms/smilPyPlotSample.py
    
or

    env PYTHONPATH=$(pwd)/smilGoodies:${PYTHONPATH} \
      python samplePrograms/read3DSample.py

