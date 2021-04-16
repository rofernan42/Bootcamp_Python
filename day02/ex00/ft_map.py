class ft_map(object):
    def __init__(self, function_to_apply, list_of_inputs):
        self.ret = (function_to_apply(i) for i in list_of_inputs)
    def __iter__(self):
        return self.ret
    def __next__(self):
        return next(self.ret)
    def __repr__(self):
        return "<" + self.__class__.__name__ + " object at " + hex(id(self)) + ">"


def calculateSquare(n):
    return n*n

numbers = (1, 2, 3, 4)
result1 = map(calculateSquare, numbers)
result2 = ft_map(calculateSquare, numbers)
print(result1)
print(result2)

print(list(result1))
print(list(result2))

print(set(map(calculateSquare, numbers)))
print(set(ft_map(calculateSquare, numbers)))
