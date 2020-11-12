
import smilPython as sp
import smilPyPlot as sg
import smilPyRead3D as sg

print("Read a stack of 2D tiff images")
imm = sg.read3DStack("images/3D/balls", expr = "*")

print("Read a stack of 2D png images")
iml = sg.read3DStack("images/3D/lena",  fext = ".png") 

print("Read a stack of raw images")
imb = sg.read3DStack("images/3D/raw", width = 512, height = 512, TYPE = "UINT8", fext = ".raw")

print("Read a 3D raw image")
ims = sg.read3DImage("images/3D/balls.raw", width = 512, height = 512, depth = 512, TYPE = "UINT8")

print("Read a 3D raw image")
imt = sg.read3DImage("images/3D/balls.raw", width = 512, height = 512, depth = 512, TYPE = "UINT8")

imm.show()
imm.setName("Stack of 2D tiff images")
iml.show()
iml.setName("Stack of 2D png images")
imb.show()
imb.setName("Stack of 2D raw images")
ims.show()
ims.setName("Raw 3D image")
imt.show()
imt.setName("Raw 3D image")

input("Enter to continue...")


