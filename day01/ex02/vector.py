class Error(Exception):
    def __init__(self, string):
        self.string = string

class Vector:
    def __init__(self, values):
        try:
            if isinstance(values, list) or isinstance(values, range):
                self.values = [float(i) for i in values]
            elif isinstance(values, int):
                self.values = [float(i) for i in range(values)]
        except:
            print("Error argument.")

    def __len__(self):
        return len(self.values)

    def __add__(self, other):
        try:
            if isinstance(other, Vector) and len(other) == len(self):
                new_vec = [x + y for x, y in zip(self.values, other.values)]
                return Vector(new_vec)
            else:
                raise Error("Operator must be a vector and have the same size.")
        except Error as e:
            print(e.string)

    __radd__ = __add__

    def __mul__(self, other):
        try:
            if isinstance(other, Vector) and len(other) == len(self):
                scal = sum([x * y for x, y in zip(self.values, other.values)])
                return scal
            elif isinstance(other, int) or isinstance(other, float):
                new_vec = [x * float(other) for x in self.values]
                return new_vec
            else:
                raise Error("Operator should be a scalar or a vector with the same size.")
        except Error as e:
            print(e.string)

    __rmul__ = __mul__

    def __sub__(self, other):
        try:
            if isinstance(other, Vector) and len(other) == len(self):
                new_vec = [x - y for x, y in zip(self.values, other.values)]
                return Vector(new_vec)
            else:
                raise Error("Operator must be a vector and have the same size.")
        except Error as e:
            print(e.string)

    __rsub__ = __sub__

    def __truediv__(self, other):
        try:
            if isinstance(other, int) or isinstance(other, float):
                new_vec = [x / float(other) for x in self.values]
                return new_vec
            else:
                raise Error("Operator must be a scalar.")
        except Error as e:
            print(e.string)
    
    def __rtruediv__(self, other):
        try:
            raise Error("Cannot divide by another vector.")
        except Error as e:
            print(e.string)

    def __str__(self):
        return f"(Vector {self.values})"
    
    def __repr__(self):
        return f"Vector({self.values})"