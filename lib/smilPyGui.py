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

import matplotlib.gridspec as gs

import random

#
#
#
class smilGuiClass:
  def __init__(self, im, ncols = 4, titles = [], 
               newfig = True, follow = False, ongui = None):
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

    self.newfig = newfig
    self.follow = follow

    plt.ion()
    self.ax = []

    self.fignum = 1
    self.showit = False
    
    print(type(self).__name__)

    self.show()

  def show(self):
    self.ax = []
    
    fignum = self.__getNextFreeSlot()
    if self.newfig:
      fig = plt.figure(fignum)
      self.fignum = fignum
    else:
      fig = plt.figure(self.fignum)
      plt.gcf()
      plt.clf()

    #self.fignum = fignum
    nb = len(self.img)    
    for i in range(0, nb):
      print("Will show image {:d} {:d} {:d}".format(i, self.nrows, self.ncols))

      print("  {:d} {:d}".format(self.img[i].getWidth(), self.img[i].getHeight()))
      a = plt.subplot(self.nrows, self.ncols, i + 1, title = self.titles[i])
      a.axis('off')
      self.ax.append(a)
      #showSmilImage(img[i], i)
  
      im = self.img[i].getNumArray()
      im = im.T
      a.imshow(im, cmap = "gray")


  def refresh(self):
    pass
 
  # "private" methods
  def __getNextFreeSlot(self):
    figs = plt.get_fignums()
    for i in range(1, 200):
      if not i in figs:
        return i
    return None




#
#
#
def smilGui(im, ncols = 4, titles = [], newfig = True):
  gui = smilGuiClass(im, ncols, titles, newfig)
  return gui

#
#
#
if __name__ == '__main__':
  print("Running as main...")
  im = sp.Image("images/Gray/astronaut.png")
  gui1 = smilGui([im, im], titles = ["astronaut 1", "astronaut 2"])
  input("Press Enter to continue...")
  gui2 = smilGui([im, im], titles = ["astronaut 3", "astronaut 4"], newfig = False)
  input("Press Enter to continue...")
  
  if True:
    se = sp.CrossSE()
    sz = 3

    img = []

    for i in range(0, 1):
      img.append(sp.Image("images/Gray/lena.png"))

    for i in range(1, 8):
      img.append(sp.Image(img[0]))
 
    sp.dilate(img[0], img[1], se(sz))
    sp.erode(img[0], img[2], se(sz))
    sp.open(img[0], img[3], se(sz))
    sp.close(img[0], img[4], se(sz))
    sp.gradient(img[0], img[5])
    sp.inv(img[0], img[6])
    sp.threshold(img[0], img[7])

    titles = ["Original", "Dilate", "Erode", "Open", 
              "Close", "Gradient", "Inverse", "Threshold"]

    smilGui(img, ncols = 4, titles = titles)

    input("Press Enter to continue...")

