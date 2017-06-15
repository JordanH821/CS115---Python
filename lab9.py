# mandelbrot.py
# Lab 8
#
# Name: Jordan Handwerger
#Pledge: I pledge my honor that I have abided by the
#        Stevens Honor System. JH


# keep this import line...
from cs5png import *
import turtle
from mandelbrot3.png import Image

# start your Lab 8 functions here:
def mult(c, n):
    result = 0
    for x in range(n):
        result += c
    return result

def update(c, n):
    z = 0
    for x in range(n):
        z = z**2 + c
    return z

def inMSet(c, n):
    z = 0
    for x in range(n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True
def WeWantThisPixel(col, row):
    if col % 10 == 0 and row % 10 == 0:
        return True
    return False

def test():
    width = 300
    height = 200
    image = PNGImage(width, height)
    
    for col in range(width):
        for row in range(height):
            if WeWantThisPixel(col, row) == True:
                image.plotPoint(col, row)
    image.saveFile()
    
def scale(pix,pixMax,floatMin,floatMax):
    return floatMin + ((pix / pixMax) * (floatMax - floatMin))

def mset():
    width=300
    height=200
    image = PNGImage(width, height)
    
    for col in range(width):
        x = scale(col, 300, -2, 1)
        for row in range(height):
            y = scale(row, 200, -1, 1)
            c = x + y*1j
            if inMSet(c, 25):
                image.plotPoint(col, row)
    image.saveFile()
    
print(mult(3,4))
print(update(-1,3))
c = 3+4*1j
print(inMSet(c,25))
print(scale(100,300,-2,1))
mset()
