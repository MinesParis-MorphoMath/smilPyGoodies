#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  smilToNumpyPlot.py
#  
#  Copyright 2015 Fehri <afehri@afehri-Precision-T1500>
#
# Modified by Samy Blusseau on Octobre 2018
#   added: function randColormap
#   and the generated random colormap called randcmap
#   is used instead of cm.Paired

import smilPython as sp

import numpy as np

import matplotlib        as mpl
import matplotlib.pyplot as plt
import matplotlib.image  as mpimg

import matplotlib.cm       as cm
import matplotlib.colors   as cl

import matplotlib.gridspec as gridspec

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
def smilPlot(iml, titles = [], ncols = 2, falseColor = False):
  """
   smilPlot :
  """

  def showSmilImage(im, i):
    print("   pos = {:d} {:d} {:d}". format(nrows, ncols, i))
    return True

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

  plt.ion()
  plt.clf()
  ax = []
  print(" {:2d} rows and {:2d} cols".format(nrows, ncols))
  for i in range(1, nb + 1):
    print("Will show image {:d}".format(i))
    if not titles[i - 1] is None:
      title = titles[i - 1]
    else:
      title = img[i - 1].getName()
      if title == '':
        title = "Image {:d}".format(i)
    a = plt.subplot(nrows, ncols, i, title = title)
    ax.append(a)
    a.axis('off')

    showSmilImage(img[i-1], i)

    im = img[i - 1].getNumArray()
    im = im.T
    plt.imshow(im, cmap = "gray")

  return ax




