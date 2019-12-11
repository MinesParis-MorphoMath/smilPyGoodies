#
# Inspired by a previous script by Amin Fehri to show Smil Images inside
# Jupyter notebooks. This is a full rewrite using Python classes with many
# improvements
#
# History : 
#   2019/11/29 - José-Marcio Martins da Cruz
#       Created
#
#
#
#
#
import smilPython as sp

import numpy             as np
import matplotlib        as mpl
import matplotlib.pyplot as plt
import matplotlib.image  as mpimg
import matplotlib.colors as cl

import random

#
#
#
__blackbg = True
def randColorMap(seed = 449):
  random.seed(seed)
  randarray = np.random.rand(255, 3)
  if __blackbg:
    randarray[0] = [0, 0, 0]
  else:
    randarray[0] = [1, 1, 1]
  cmap = cl.ListedColormap(randarray)
  return cmap

gcmap = None

#
#
#
class mplGui:
  """
  class mplGui :
    Parameters :
      im        : an image or a list of images
      ncols     : number of columns
      titles    : A list of names to be shown. If empty, names will be taken
                  from the images by calling "im.getName()"
      onGui     : if present, will be shown in a previously defined 
                  mplGui instance
      fakeColor : with gray images use a randColorMap - useful to present
                  different regions in labelled images.
    Methods :
      refresh : update display window when some images were modified
  """

  #
  #
  #
  def __init__(self, im, ncols = 4, titles = [], onGui = None, fakeColor = False):    
    global gcmap
    if gcmap is None:
      gcmap = randColorMap()
    self.gcmap = gcmap

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
      if not titles is None:
        self.titles.append(titles)
    for i in range(len(self.titles), nb):
      self.titles.append(self.img[i].getName())

    self.fakeColor = []
    if isinstance(fakeColor, list):
      self.fakeColor = fakeColor
    else:
      if type(fakeColor).__name__ != 'bool':
        fakeColor = False
      self.fakeColor.append(fakeColor)
    for i in range(len(self.fakeColor), nb):
      self.fakeColor.append(False)

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
      if type(onGui).__name__ == 'mplGui':
        self.fignum = onGui.fignum
        self.fig = plt.figure(self.fignum)
        self.fig.clf()
    if self.fignum == 0:
      self.fig = plt.figure()
      self.fignum = plt.gcf().number

    self.shown = False
    self.__show()

  #
  #
  def refresh(self):
    nb = len(self.img)
    for i in range(0, nb):
      self.__showImage(i)

  # Private methods
  #
  def __show(self):
    self.ax = []
    nb = len(self.img)    
    for i in range(0, nb):
      a = plt.subplot(self.nrows, self.ncols, i + 1, title = self.titles[i])
      self.ax.append(a)
      self.__showImage(i)
    self.shown = True

  #
  #
  def __showImage(self, i):
      self.ax[i].axis('off')
      cmap = None
      imType = self.img[i].getTypeAsString()
      if (imType == "RGB"):
        imc = sp.Image()
        sp.splitChannels(self.img[i], imc)
      else:
        imc = self.img[i]
        if self.fakeColor[i]:
          cmap = self.gcmap
        else:
          cmap = "gray"

      im = imc.getNumArray()
      im = np.rot90(im, -1)
      im = np.fliplr(im)
      self.ax[i].imshow(im, cmap = cmap)

# End of mplGui


#
#
#
if __name__ == '__main__':
  print("Running as main...")

  # Display a color image
  imc = sp.Image("images/Color/astronaut.png")
  imc.setName("Astronaut")
  gui0 = mplGui(imc)
  input("Press Enter to continue...")

  # Display two images, side by side
  im = sp.Image("images/Gray/astronaut.png")
  gui1 = mplGui([im, im], titles = ["Image 1", "Image 2"])
  input("Press Enter to continue...")



