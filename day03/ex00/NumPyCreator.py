import numpy as np

class NumPyCreator:
    def from_list(self, lst):
        return np.array(lst)
    def from_tuple(self, tpl):
        return np.array(tpl)
    def from_iterable(self, itr, dtype=float):
        return np.fromiter(itr, dtype)
    def from_shape(self, shape, value=0):
        return np.full(shape, value)
    def random(self, *shape):
        return np.random.rand(*shape)
    def identity(self, n, dtype=float):
        return np.identity(n, dtype)

nump = NumPyCreator()
print(nump.from_list([1, 3, 5, 2, 9, 4]))
print(nump.from_tuple((1, 3, 5, 2, 9, 4)))

iterable = (x*x for x in range(5))
print(nump.from_iterable(iterable))

shape=(3, 5)
print(nump.from_shape(shape))

print(nump.random(3, 2))
print(nump.random(5))

print(nump.identity(4))