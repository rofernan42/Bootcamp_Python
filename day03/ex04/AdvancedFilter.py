import numpy as np

class AdvancedFilter:
    def mean_blur(self, array):
        mb = array.copy()
        for x in range(array.shape[0]):
            for y in range(array.shape[1]):
                for i in range(3):
                    if x > 0 and x < array.shape[0] - 1 and y > 0 and y < array.shape[1] - 1:
                        mb[x][y][i] = np.sum(array[x-1:x+2, y-1:y+2, i]) / 9
        return mb.astype(np.int32)
    def gaussian_blur(self, array):
        gb = array.copy()
        for x in range(array.shape[0]):
            for y in range(array.shape[1]):
                for i in range(3):
                    if x > 0 and x < array.shape[0] - 1 and y > 0 and y < array.shape[1] - 1:
                        gb[x][y][i] = (4 * np.sum(array[x,y,i]) + 2 * (np.sum(array[x-1,y,i]) + np.sum(array[x+1,y,i]) + np.sum(array[x,y-1,i]) + np.sum(array[x,y+1,i])) + 1 * (np.sum(array[x-1,y-1,i]) + np.sum(array[x-1,y+1,i]) + np.sum(array[x+1,y-1,i]) + np.sum(array[x+1,y+1,i]))) / 16
        return gb