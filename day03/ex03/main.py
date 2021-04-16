from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter
import numpy as np

img = ImageProcessor()
cf = ColorFilter()

arr = img.load("../resources/mario.jpeg")
img.display(arr)

inverted = cf.invert(arr)
img.display(inverted)

blued = cf.to_blue(arr)
img.display(blued)

greened = cf.to_green(arr)
img.display(greened)

reded = cf.to_red(arr)
img.display(reded)

img.display(cf.celluloid(arr))

img.display(cf.to_grayscale(arr, "m"))

img.display(cf.to_grayscale(arr, "w"))