
import smilPython as sp
from   smilPyPlot import *

import numpy as np

#import matplotlib        as mpl
#import matplotlib.pyplot as plt
#import matplotlib.image  as mpimg

#import matplotlib.cm       as cm
#import matplotlib.colors   as cl

import random

setBackend('qt5agg')

if True:
  i = 1
  # Display a color image
  imc = sp.Image("images/Color/astronaut.png")
  imc.setName("Astronaut")
  gui0 = ImShow(imc)
  input("{:2d} - Press Enter to continue...".format(i))
  i += 1

  # Display two images, side by side
  im = sp.Image("images/Gray/astronaut.png")
  gui1 = ImShow([im, im], titles = ["Image 1", "Image 2"])
  input("{:2d} - Press Enter to continue...".format(i))
  i += 1
  
  # The same but reuse previous window
  gui2 = ImShow([im, im], titles = ["Image 3", "Image 4"], onGui = gui1)
  input("{:2d} - Press Enter to continue...".format(i))
  i += 1
  
  # The same but in a new window
  imb = sp.Image("images/Bin/balls.png")
  img = sp.Image(imb)
  iml = sp.Image(imb)
  sp.copy(imb, img)
  sp.copy(imb, iml)
  gui3 = ImShow([imb, img, iml], 
                   titles = ["Original", "Watershed", "Bassins"], 
                   fakeColor = [False, True, True])
  input("{:2d} - Press Enter to continue...".format(i))
  i += 1
  
  # Refresh the window after a image was modified
  sp.gradient(imb, img)
  sp.label(imb, iml)
  gui3.refresh()
  input("{:2d} - Press Enter to continue...".format(i))
  i += 1
  
  # Play with a window with 8 images displayed in 2 rows of 4 columns
  se = sp.CrossSE()
  sz = 3

  img = []
  img.append(sp.Image("images/Gray/lena.png"))

  for i in range(1, 8):
    img.append(sp.Image(img[0]))

  titles = ["Original", "Dilate", "Erode", "Open", 
            "Close", "Gradient", "Inverse", "Threshold"]
  gui = ImShow(img, ncols = 4, titles = titles)
  input("{:2d} - Press Enter to continue...".format(i))
  i += 1
      
  sp.dilate(img[0],    img[1], se(sz))
  gui.refresh()
  input("{:2d} - Press Enter to continue...".format(i))
  i += 1
  sp.erode(img[0],     img[2], se(sz))
  gui.refresh()
  input("{:2d} - Press Enter to continue...".format(i))
  i += 1
  sp.open(img[0],      img[3], se(sz))
  gui.refresh()
  input("{:2d} - Press Enter to continue...".format(i))
  i += 1
  sp.close(img[0],     img[4], se(sz))
  gui.refresh()
  input("{:2d} - Press Enter to continue...".format(i))
  i += 1
  sp.gradient(img[0],  img[5])
  gui.refresh()
  input("{:2d} - Press Enter to continue...".format(i))
  i += 1
  sp.inv(img[0],       img[6])
  gui.refresh()
  input("{:2d} - Press Enter to continue...".format(i))
  i += 1
  sp.threshold(img[0], img[7])
  gui.refresh()
  input("{:2d} - Press Enter to continue...".format(i))
  



