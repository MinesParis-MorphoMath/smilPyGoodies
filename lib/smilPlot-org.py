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

from   matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.cm       as cm
import matplotlib.colors   as cl

import numpy as np
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
def smilToNumpyPlot(imIn,labelImage = False):
  if (imIn.getTypeAsString() == "RGB"):
    imIn3ch = sp.Image()
    sp.splitChannels(imIn, imIn3ch)
    imInArr = imIn3ch.getNumArray()
    imInArr = np.rot90(imInArr, -1)
    imInArr = np.fliplr(imInArr)
    plt.figure()
    plt.imshow(imInArr)
    plt.show()
  else:
    imInArr = imIn.getNumArray()
    imInArr = np.rot90(imInArr, -1)
    imInArr = np.fliplr(imInArr)
    if not labelImage:
      plt.figure()
      plt.imshow(imInArr, cmap = "gray", norm = cl.NoNorm()) 
      #plt.imshow(imInArr, cmap = cm.Greys_r, norm = cl.NoNorm())  
      plt.show()
    else:
      plt.figure()
      plt.imshow(imInArr, cmap = randcmap)
      plt.show()

#
#
#
def smilToNumpyPlotNoNorm(imIn,labelImage = False):
  if (imIn.getTypeAsString() == "RGB"):
    imIn3ch = sp.Image()
    sp.splitChannels(imIn,imIn3ch)
    imInArr = imIn3ch.getNumArray()
    imInArr = np.rot90(imInArr, -1)
    imInArr = np.fliplr(imInArr)
    plt.figure()
    plt.imshow(imInArr)
    plt.show()
  else:
    imInArr = imIn.getNumArray()
    imInArr = np.rot90(imInArr, -1)
    imInArr = np.fliplr(imInArr)
    if not labelImage:
      plt.figure()
      plt.imshow(imInArr, cmap = "gray", norm = cl.NoNorm()) 
      plt.show()
    else:
      plt.figure()
      plt.imshow(imInArr, cmap = randcmap)
      plt.show()

#
#
#
def X_singlePlot(imIn, ax, label):
  if (imIn.getTypeAsString() == "RGB"):
    im3ch = sp.Image()
    sp.splitChannels(imIn, im3ch)
    imArr = im3ch.getNumArray()
    imArr = np.rot90(imArr, -1)
    imArr = np.fliplr(imArr)
    ax.imshow(imArr)
  else:
    imInArr = imIn.getNumArray()
    imInArr = np.rot90(imInArr, -1)
    imInArr = np.fliplr(imInArr)
    if not label:
      ax.imshow(imInArr, cmap = cm.Greys_r, norm = cl.NoNorm())
    else:
      ax.imshow(imInArr, cmap = randcmap)

#
#
#
def smilPlot(imIn = [], label = [], title = []):
  #
  #
  def singlePlot(imIn, ax, label):
    if (imIn.getTypeAsString() == "RGB"):
      im3ch = sp.Image()
      sp.splitChannels(imIn, im3ch)
      imArr = im3ch.getNumArray()
      imArr = np.rot90(imArr, -1)
      imArr = np.fliplr(imArr)
      ax.imshow(imArr)
    else:
      imInArr = imIn.getNumArray()
      imInArr = np.rot90(imInArr, -1)
      imInArr = np.fliplr(imInArr)
      if not label:
        ax.imshow(imInArr, cmap = cm.Greys_r, norm = cl.NoNorm())
      else:
        ax.imshow(imInArr, cmap = randcmap)

  #
  #
  nb = len(imIn)

  multirow = False

  #fig = plt.figure(constrained_layout = multirow)
  fig = plt.figure(constrained_layout=True)
  #fig = plt.figure()

  if multirow:
    Nc = 2
    Nr = nb // Nc + 1
  else:
    Nc = nb
    Nr = 1

  gs = gridspec.GridSpec(nrows = Nr, ncols = Nc)
#  gs = gridspec.GridSpec(nrows = Nr, ncols = Nc, figure = fig)
  gs.update(left = 0.05, right = 1.7, wspace = 0.4)
  ax = []
  while len(label) < nb:
    label.append(False)
  while len(title) < nb:
    title.append("")
  for i in range(0, nb):
    ir = i // Nc
    ic = i % Nc
    if multirow:
        ax.append(plt.subplot(gs[ir, ic], title = title[i]))
    else:
        ax.append(plt.subplot(gs[0, i], title = title[i]))
    singlePlot(imIn[i], ax[i], label[i])

  plt.show()

#
#
#
def smilToNumpyPlot(imIn, labelImage = [False]):
    smilPlot([imIn], labelImage)

def smilToNumpyPlot2(imIn, imIn2, labelImage = [False, False]):
    smilPlot([imIn, imIn2], labelImage)

def smilToNumpyPlot3(imIn, imIn2, imIn3, labelImage = [False, False, False]):
    smilPlot([imIn, imIn2, imIn3], labelImage)

def smilToNumpyPlot4(imIn1, imIn2, imIn3, imIn4,
                     labelImage = [False, False, False, False]):
    smilPlot([imIn, imIn2, imIn3, imIn4], labelImage)


