from ImageProcessor import ImageProcessor
from ScrapBooker import ScrapBooker
import numpy as np

img = ImageProcessor()
sb = ScrapBooker()

arr = img.load("../resources/mario.jpeg")
img.display(arr)

cropped = sb.crop(arr, (50, 50), (100, 100))
img.display(cropped)

tothin = np.array(['A','B','C','D','E','F','G','H','I','J','K','L'])
tothin = np.tile(tothin, (7, 1))
print(tothin)
print("")
print(sb.thin(tothin, 3, 0))
print("")
tothin2 = np.transpose(tothin)
print(tothin2)
print("")
print(sb.thin(tothin2, 4, 1))

juxta = sb.juxtapose(arr, 3, 0)
img.display(juxta)
juxta2 = sb.juxtapose(arr, 4, 1)
img.display(juxta2)

mos = sb.mosaic(arr, (2, 3))
img.display(mos)
mos2 = sb.mosaic(arr, (4, 2))
img.display(mos2)
