class ft_filter(object):
    def __init__(self, function_to_apply, list_of_inputs):
        self.ret = (i for i in list_of_inputs if function_to_apply(i) == True)
    def __iter__(self):
        return self.ret
    def __next__(self):
        return next(self.ret)
    def __repr__(self):
        return "<" + self.__class__.__name__ + " object at " + hex(id(self)) + ">"

letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if(letter in vowels):
        return True
    else:
        return False

filtered_vowels1 = filter(filter_vowels, letters)
filtered_vowels2 = ft_filter(filter_vowels, letters)
print(filtered_vowels1)
print(filtered_vowels2)

print(list(filtered_vowels1))
print(list(filtered_vowels2))
