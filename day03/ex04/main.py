from ImageProcessor import ImageProcessor
from AdvancedFilter import AdvancedFilter
import numpy as np

img = ImageProcessor()
af = AdvancedFilter()

arr = img.load("../resources/mario.jpeg")
img.display(arr)

img.display(af.mean_blur(arr))
img.display(af.gaussian_blur(arr))