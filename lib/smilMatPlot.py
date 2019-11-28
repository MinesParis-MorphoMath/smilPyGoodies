#!/usr/bin/env python
# -*- coding: utf-8 -*-


import smilPython as sp

import numpy as np

import matplotlib        as mpl
import matplotlib.pyplot as plt
import matplotlib.image  as mpimg

import matplotlib.cm       as cm
import matplotlib.colors   as cl

import matplotlib.gridspec as gs

import random

#
#
#
def randColormap(SEED = 448):
  random.seed(SEED)
  randarray = np.random.rand(255, 3)
  randarray[0] = [0, 0, 0]
  cmap = cl.ListedColormap(randarray)
  return cmap

# Global colormap used as a unique LUT
randcmap = randColormap(448)

#
#
#
def smilPlot(iml, titles = [], ncols = 2, falseColor = False, new = True):
  """
   smilPlot :
     iml        : Image or list of images to display
     titles     : List with image titles
     ncols      : number of columns
     falseColor : 
     new        : create a new image window or use the last created one
     
  """

  def showIt(img, title, i):
    print("   pos = {:d} {:d} {:d}". format(nrows, ncols, i))
    a = plt.subplot(nrows, ncols, i + 1, title = title)
    a.axis('off')
    im = img.getNumArray()
    im = im.T
    a.imshow(im, cmap = "gray")
 
    return a

  img = []
  if isinstance(iml, list):
    img = iml
  else:
    img.append(iml)

  nb = len(img)
  if nb == 0:
    return false
  while len(titles) < nb:
    titles.append(None)

  if nb < ncols:
    ncols = nb
  nrows = nb // ncols
  if nb % ncols > 0:
    nrows += 1

  if new:
    plt.figure()
  plt.ion()
  plt.clf()
  ax = []
  #print(" {:2d} rows and {:2d} cols".format(nrows, ncols))
  for i in range(0, nb):
    # print("Will show image {:d}".format(i))
    if not titles[i] is None:
      title = titles[i]
    else:
      title = img[i].getName()
      if title == '':
        title = "Image {:d}".format(i)

    a = showIt(img[i], title, i)
    ax.append(a)

  return ax



if __name__ == "__main__":
  se = sp.CrossSE()
  sz = 3

  img = []

  for i in range(0, 1):
    img.append(sp.Image("images/Gray/astronaut.png"))

  for i in range(1, 8):
    img.append(sp.Image(img[0]))
 
  sp.dilate(img[0], img[1], se(sz))
  sp.erode(img[0], img[2], se(sz))
  sp.open(img[0], img[3], se(sz))
  sp.close(img[0], img[4], se(sz))
  sp.gradient(img[0], img[5])
  sp.inv(img[0], img[6])
  sp.threshold(img[0], 150, img[7])

  titles = ["Original", "Dilate", "Erode", "Open", 
            "Close", "Gradient", "Inverse", "Threshold"]

  smilPlot(img, ncols = 4, titles = titles, new = False)

  input("Press Enter to continue...")




