import numpy as np
import PIL.Image
import matplotlib.pyplot as plt

class ImageProcessor:
    def load(self, path):
        img = PIL.Image.open(path)
        self.width, self.height = img.size
        print(f"Loading image of dimensions {self.width} x {self.height}")
        rgb = np.full([self.height, self.width, 3], 0)
        for y in range(self.height):
            for x in range(self.width):
                rgb[y, x] = img.getpixel((x, y))
        return np.array(rgb)
    def display(self, array):
        plt.imshow(array)
        plt.show()
