
# smilPyGoodies
 
Some goodies to help use Smil under Python

Initial goals of this stuff is :

* a trivial replacement of all __Qt__ libraries needed to compile __Smil__. This
a little bit problematic with different versions of __Qt__ and their 
availability under different __Linux__ flavors. 

* some functions helping to read __3D__ images stored in __raw__ format or as
as stack of __2D__ images.

## Directory Contents

* __smilPyGoodies__  - Python modules

  * __smilPyRead3D__ : this module helps reading 3D images
  * __smilPyPlot__ : this module contains a Matplotlib based GUI.
    This module has two reasons to be :
    * no dependency on Qt libraries;
    * can be used with jupyter notebooks.

* __samplePrograms__ - examples on how to use these goodies

* __examples__ - smilPython examples

* __images__ - some images to play with

## Modules

Take a look in the sample programs to see how to use these modules in your 
program.

###  smilPyRead3D

  Ce module complements the Smil native read functions, which allows reading 3D images only from images in the RAW format.

  This module allows reading 3D images :
* as a stack of 2D images of the same size and data type;
* TIFF 3D images, both in float or integer data type.

### smilPyPlot

The first goal of this module is to replace the __Qt__ based graphical user interface, which causes some problems under some Linux distributions.

Also it can be used on some web kind applications such as jupyter. This isn't possible with the Qt based GUI.

One of the advantages smilPyPlot is to be able to show more than one image on 
the same window (or space).

Two obvious disadvantages are limited interactivity and impossibility to 
display __3D__ images, for the moment. 

Interactivity is limited to, e.g., things like zooming and consulting pixel 
values.



## Installing

### Requirements

* __python3-matplotlib__ - Matplotlib

* __PyQt__ - Under Ubuntu, package __python3-pyqt5__

* __libtiff__ - To be able to read __3D__ tiff files - Under Ubuntu, packages 
  __libtiff5__, __tifffile__ and (optional) __libtiff-tools__

### Installing

    git clone https://github.com/ensmp-cmm/smilPyGoodies
    cd smilPyGoodies
    cp -pr smilPyGoodies /installation_path/
    
    export PYTHONPATH=/installation_path:${PYTHONPATH}

## Using it :

    import smilPyGoodies as sg

    sg.someFunctionCall...

## Sample programs

Still in the directory where you distribution was cloned, you can just type :

    env PYTHONPATH=$(pwd)/smilPyGoodies:${PYTHONPATH} \
      python samplePrograms/smilPyPlotSample.py

or

    env PYTHONPATH=$(pwd)/smilGoodies:${PYTHONPATH} \
      python samplePrograms/read3DSample.py

## Short documentation

Don't hesitate to take a look at the __Sample Programs__

### smilPyPlot

####  * ImShow

    ImShow(
        im,
        ncols=4,
        titles=[],
        onGui=None,
        fakeColor=False,
        showAxis='Off',
    )

    Docstring:
    class ImShow :
      Parameters :
        im        : an image or a list of images
        ncols     : number of columns
        titles    : A list of names to be shown. If empty, names will be taken
                    from the images by calling "im.getName()"
        onGui     : a ImShow handle. if present, will be shown in a previously
                    defined ImShow instance
        fakeColor : with gray images use a randColorMap - useful to present
                    different regions in labelled images.
        showAxis  : show image axis with scale

      Methods :
        refresh : update display window when some images were modified
        
      Returns :
        a handle to the class instance. Need this to update the output.

#### * setBackend

    setBackend(backend='')

    Docstring:

    defBackend(backend) - sets the matplotlib backend to use.
    
    Valid values for backend :
        backend in ['qt5agg', 'gtk3agg', 'gtkcairo', 'tkagg']

    See : https://matplotlib.org/faq/usage_faq.html#what-is-a-backend

    Requirements :
      qt5agg   : PyQt5
      gtk3agg  : PyGObject and pycairo or cairocffi
      gtkcairo : PyGObject and pycairo or cairocffi
      tkagg    : TkInter


### smilPyRead3D

#### * smilRead3DImage

    read3DImage(
        fin,
        width=0,
        height=0,
        depth=0,
        TYPE=None,
        bSwap=None,
        post=None,
    )
    Docstring:
    read3DImage : creates a 3D image from a single .raw or .tif image file.

    Parameters :
      fin     : image file name
      width,
      height,
      depth   : dimensions, only needed for images in raw format
      TYPE    : TYPE of pixel value. One of 'UINT8', 'UINT16' or 'UINT32'
                Mandatory for raw images.
                Output images will be converted to this data type.
      bSwap   : bytes shall be swapped (lowendian vs bigendian)
      post    : post process function (a numpy function).
    Return value :
      A 3D image if success, None otherwise

#### * read3DStack
    read3DStack(
        dir,
        width=None,
        height=None,
        TYPE=None,
        expr=None,
        fext=None,
    )
    Docstring:
    read3DStack : creates a 3D image from a stack of 2D images

    Parameters :
      dir     : directory where to find all 2D image files
      width,
      height  : dimensions of each 2D image, only needed for images in 
                raw format
      TYPE    : TYPE of pixel value, only needed for raw images. 
                One of 'UINT8', 'UINT16' or 'UINT32'
      expr    : regular expression (glob syntax) of filename
      fext    : file extension

    Return value :
      A 3D image if success, None otherwise

