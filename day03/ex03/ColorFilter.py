import numpy as np

class ColorFilter:
    def invert(self, array):
        return 255 - array
    def to_blue(self, array):
        res = np.zeros((array.shape[0], array.shape[1], 3), int)
        res[:, :, 2] = array[:, :, 2]
        return res
    def to_green(self, array):
        return array * [0, 1, 0]
    def to_red(self, array):
        return array - self.to_blue(array) - self.to_green(array)
    def celluloid(self, array, threshold=4):
        rgb = np.linspace(0, 255, num=threshold, dtype=int)
        c = array.copy()
        for i in rgb:
            idx = array >= i # cree un tableau 3d de bool valant true la ou array[x][y][z] >= i
            c[idx] = i # apply i partout ou idx vaut true
        return c
    def to_grayscale(self, array, filter):
        if filter == "mean" or filter == "m":
            m = np.sum(array, axis=2) / 3
            m = np.broadcast_to(m[:,:, None], (np.shape(array))) # w[:,:, None] = w[..., None] avec None = np.newaxis (nouvel axe de longueur 1)
            return m.astype(np.int32)
        elif filter == "weighted" or filter == "w":
            w = np.sum(array * [0.299, 0.587, 0.114], axis=2)
            w = np.tile(w[:,:, None], (3))
            return w.astype(np.int32)