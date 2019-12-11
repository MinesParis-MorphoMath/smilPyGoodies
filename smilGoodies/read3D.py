#
# This goodie intends to help reading 3D image files in two situations not
# directly implemented on Smil library
#   * images are saved as files : one 2D image per slice
#   * 3D images are stored in a single TIFF file
#
# History : 
#   2019/11/29 - José-Marcio Martins da Cruz
#       Created
# TODO :
#   * 3D images - how to ???
#   * 16 and 32 bits images - convert them to float ?
#
#

import os
import sys
import glob
import re
import numpy as np

import smilPython as sp

tiffOK = True
try:
  # need TIFF and TiffFile to be able to read 3D tiff files
  from libtiff import *
except:
  print("\n    read3d : Can't import module python-libtiff\n")
  print("\n      Reading 3D .tiff files isn't available\n")
  tiffOK = False
  pass

_smilTypes = ['UINT8', 'UINT16', 'UINT32']

#
#
#
def read3DImage(fin, width = 0, height = 0, depth = 0, 
                    TYPE = None, bSwap = None, post = None):
  """
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
  """
  im = None

  if not os.path.isfile(fin):
    return im

  # read a 3D raw image file  
  if os.path.splitext(fin)[1] in ['.raw']:
    im = sp.Image(TYPE)

    if not (width > 0 and height > 0 and depth > 0):
      return NONE

    if sp.readRAW(fin, width, height, depth, im) != 1:
      print("Error : reading image file ", fin)
      
    if not post is None:
      funcs = []
      if not type(post).__name__ == 'list':
        funcs.append(post)
      else:
        funcs = post
      for f in funcs:
        pass
        
    return im

  # Read a 3D tif image file
  if os.path.splitext(fin)[1] in ['.tif', 'tiff']:
    print("Reading tiff file")
    if not tiffOK:
      print("  module python-libtiff not loaded")
      return im

    tif = TIFF.open(fin, mode = 'r') 

    n = 0
    imArr = np.array([])
    (w, h) = (0, 0)
    for im in tif.iter_images():
      n += 1
      if imArr.shape == (0,):
        imArr = im
        (w, h) = imArr.shape
      else:
        imArr = np.vstack((imArr, im))
  
    imArr = imArr.reshape(n, w, h)

    if bSwap is None and tif.IsByteSwapped() == 1 or bSwap:
      imArr = imArr.byteswap()
    
    if not post is None:
      if type(post).__name__ == 'function':
        imArr = post(imArr)
      else:
        print(" 'post' parameter isn't a function : ignored")
    
    if not imArr.dtype.name in _smilTypes:
      if TYPE is None or not TYPE in _smilTypes:
        TYPE = 'UINT8'

    if not TYPE is None and TYPE.upper() in _smilTypes:
      if TYPE.lower() != imArr.dtype.name:
        if imArr.min() < 0:
          imArr -= imArr.min()

        amax = imArr.max()
        imax = sp.Image(TYPE.upper()).getDataTypeMax()
        imArr = (imArr.astype(np.float) * imax / amax)
        imArr = imArr.astype(TYPE.lower())

    #print("Numpy data type ", imArr.dtype.name)
    imArr = imArr.T
    im = sp.Image(imArr.dtype.name.upper())
    im.fromNumArray(imArr)

    return im

  print("This isn't a 3D image file ", fin)
  return im

#
#
#
def read3DStack(dir, width = None, height = None, 
                TYPE = None, expr = None, fext = None):
  """
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
  """
  if not os.path.isdir(dir):
    print("dir parameter isn't a directory") 
    return None
  
  if expr is None and fext is None:
    print("Either expr or fext shall be defined : all files will be considered")
    expr = "*"

  if not expr is None:
    gpath = os.path.join(dir, expr)
    files = [x for x in sorted(glob.glob(gpath)) if os.path.isfile(x)]
    if not fext is None:
      files = [x for x in files if f.endswith(fext)]
    files = [os.path.basename(x) for x in files]
  else:
    gpath = os.path.join(dir, "*")
    files = [x for x in sorted(glob.glob(gpath)) if os.path.isfile(x)]
    files = [os.path.basename(x) for x in files if x.endswith(fext)]

  if len(files) == 0:
    print("No image files found")
    return None

  # make sure fext has the pattern ".xxx"
  _, fext = os.path.splitext(files[0])

  # Files in the usual format kind
  if fext in [".png", ".tif", ".tiff", ".jpg"]:
    nim = 0
    im3d = None
    for f in files:
      fpath = os.path.join(dir, f)
      
      im = sp.Image(fpath)

      hi = im.getHeight()
      wi = im.getWidth()
      di = im.getDepth()
      ti = im.getTypeAsString()
      
      # RGB images are converted to gray level images.
      if ti == 'RGB':
        imt = sp.Image(im, 'UINT8')
        sp.RGBToLuminance(im, imt)
        im = imt

      if nim == 0:
        h = hi
        w = wi
        t = ti
        im3d = sp.Image(im)
        im3d.setSize(w, h, len(files))

      if h != hi or w != wi:
        print("Error  : images doesn't have the same size : ", f)
        return None
      if t != ti:
        printf("Error : images doesn't have the same pixel type")
        return None

      sp.copy(im, 0, 0, 0, im3d, 0, 0, nim)
      nim += 1      
      
    return im3d

  # Raw files (no metadata)
  if fext in [".raw"]:
    if width is None or not width > 0:
      print("width shall be an integer greater than 0")
      return None
    if height is None or not height > 0:
      print("height shall be an integer greater than 0")
      return None 
    if not TYPE is None and not TYPE in ['UINT8', 'UINT16', 'UINT32']:
      print("TYPE shall be one of UINT8, UINT16 or UINT32")
      return None

    nim = 0
    im3d = None
    for f in files:
      fpath = os.path.join(dir, f)

      imt = sp.Image(TYPE)
      if sp.readRAW(fpath, width, height, 1, imt) != 1:
        print("Error : reading image file ", fpath)
      if nim == 0:
        im3d = sp.Image(TYPE)
        im3d.setSize(width, height, len(files))

      if sp.copy(imt, 0, 0, 0, im3d, 0, 0, nim) != 1:
        print("  Error copying slice ", str(nim))
      nim += 1    
    return im3d

  return None


