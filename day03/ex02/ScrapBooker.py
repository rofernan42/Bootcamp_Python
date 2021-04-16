import numpy as np

class ScrapBooker:
    def crop(self, array, dimensions, position=(0, 0)):
        ybeg = position[0]
        yend = position[0] + dimensions[0]
        xbeg = position[1]
        xend = position[1] + dimensions[1]
        return array[ybeg:yend, xbeg:xend]
    def thin(self, array, n, axis):
        res = np.delete(np.transpose(array), list(range(-1, np.transpose(array).shape[axis], n)), axis)
        return np.transpose(res)
    def juxtapose(self, array, n, axis):
        res = array
        for i in range(n - 1):
            res = np.concatenate((res, array), axis)
        return res
    def mosaic(self, array, dimensions):
        resx = array
        for i in range(dimensions[0] - 1):
            resx = np.concatenate((resx, array), 0)
        resy = resx
        for j in range(dimensions[1] - 1):
            resy = np.concatenate((resy, resx), 1)
        return resy