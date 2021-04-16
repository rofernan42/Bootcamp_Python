class Error(Exception):
    def __init__(self, string):
        self.string = string

class Evaluator:
    def __init__(self, coefs, words):
        try:
            if not isinstance(coefs, list) and not all(isinstance(i, float) for i in coefs):
                raise Error("Coefs must be a list of floats.")
            if not isinstance(words, list) and not all(isinstance(i, str) for i in words):
                raise Error("Words must be a list of strings.")
            self.coefs = coefs
            self.words = words
        except Error as e:
            print(e.string)
    
    def zip_evaluate(self):
        if len(self.coefs) != len(self.words):
            return -1
        return sum([coef * len(word) for coef, word in zip(self.coefs, self.words)])

    def enumerate_evaluate(self):
        if len(self.coefs) != len(self.words):
            return -1
        return sum([self.coefs[i] * len(word) for i, word in enumerate(self.words)])


words = "Le lorem ipsum est simple".split(" ")

coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
eva = Evaluator(coefs, words)
print(eva.zip_evaluate())
print(eva.enumerate_evaluate())

coefs2 = list(range(2, 7))
eva2 = Evaluator(coefs2, words)
print(eva2.zip_evaluate())
print(eva2.enumerate_evaluate())

coefs3 = list(range(2, 6))
eva3 = Evaluator(coefs3, words)
print(eva3.zip_evaluate())
print(eva3.enumerate_evaluate())
