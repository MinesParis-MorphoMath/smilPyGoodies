#
#
#
import smilPython as sp

import numpy as np

import matplotlib        as mpl
import matplotlib.pyplot as plt
import matplotlib.image  as mpimg

import matplotlib.cm       as cm
import matplotlib.colors   as cl

import random

#
#
#
class smilPyGui:
  #
  #
  #
  def __init__(self, im, ncols = 4, titles = [], onGui = None):
    self.img = []
    if isinstance(im, list):
      self.img = im
    else:
      self.img.append(im)
    nb = len(self.img)

    self.titles = []
    if isinstance(titles, list):
      self.titles = titles
    else:
      for i in range(0, nb):
        self.titles.append(self.img[i].getName())
    
    if nb < ncols:
      ncols = nb
    self.ncols = ncols
    self.nrows = nb // ncols
    if nb % ncols > 0:
      self.nrows += 1

    plt.ion()
    self.ax = []

    self.fignum = 0
    if onGui is not None:
      if type(onGui).__name__ == 'smilPyGui':
        self.fignum = onGui.fignum
        self.fig = plt.figure(self.fignum)
        plt.clf()
    if self.fignum == 0:
      self.fig = plt.figure()
      self.fignum = plt.gcf().number

    self.shown = False
    self.__show()

  #
  #
  #
  def __show(self):
    self.ax = []

    nb = len(self.img)    
    for i in range(0, nb):
      a = plt.subplot(self.nrows, self.ncols, i + 1, title = self.titles[i])
      a.axis('off')
      self.ax.append(a)
  
      im = self.img[i].getNumArray()
      im = im.T
      a.imshow(im, cmap = "gray")
    self.shown = True

  #
  #
  #
  def refresh(self):
    nb = len(self.img)    
    for i in range(0, nb):
      self.ax[i].axis('off')
      im = self.img[i].getNumArray()
      im = im.T
      self.ax[i].imshow(im, cmap = "gray")
# End of smilPyGui



#
#
#
if __name__ == '__main__':
  print("Running as main...")
  im = sp.Image("images/Gray/astronaut.png")
  gui1 = smilPyGui([im, im], titles = ["astronaut 1", "astronaut 2"])
  input("Press Enter to continue...")

  gui2 = smilPyGui([im, im], titles = ["astronaut 3", "astronaut 4"])
  input("Press Enter to continue...")

  im2 = sp.Image(im)
  sp.copy(im, im2)
  gui3 = smilPyGui([im, im2], titles = ["astronaut 5", "astronaut 6"], 
                        onGui = gui1)
  input("Press Enter to continue...")
  sp.gradient(im, im2)
  gui3.refresh()
  input("Press Enter to continue...")

  
  if True:
    se = sp.CrossSE()
    sz = 3

    img = []
    img.append(sp.Image("images/Gray/lena.png"))

    for i in range(1, 8):
      img.append(sp.Image(img[0]))
 
    sp.dilate(img[0],    img[1], se(sz))
    sp.erode(img[0],     img[2], se(sz))
    sp.open(img[0],      img[3], se(sz))
    sp.close(img[0],     img[4], se(sz))
    sp.gradient(img[0],  img[5])
    sp.inv(img[0],       img[6])
    sp.threshold(img[0], img[7])

    titles = ["Original", "Dilate", "Erode", "Open", 
              "Close", "Gradient", "Inverse", "Threshold"]

    gui = smilPyGui(img, ncols = 4, titles = titles)

    input("Press Enter to continue...")

