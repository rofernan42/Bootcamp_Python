import math
import os

class Error(Exception):
    def __init__(self, string):
        self.string = string

def shuffle(list):
    list_size = len(list)
    n_bytes = math.ceil(math.log(list_size, 2) / 8)
    while list_size - 1:
        rand = int.from_bytes(os.urandom(n_bytes), "big") % list_size
        tmp = list[rand]
        list[rand] = list[list_size - 1]
        list[list_size - 1] = tmp
        list_size -= 1
    return list

def generator(text, sep=" ", option=None):
    """Option is an optional arg, sep is mandatory"""
    try:
        if len(text) == 0:
            raise Error("Text cannot be empty.")
        if option and option not in ["shuffle", "unique", "ordered"]:
            raise Error("Option not available.")
        txt = text.split(sep)
        if (option == "ordered"):
            txt = sorted(txt, key=str.lower)
        elif (option == "unique"):
            txt = list(set(txt))
        elif (option == "shuffle"):
            txt = shuffle(txt)
    except Error as e:
        print(e.string)
    for i in txt:
        yield i

txt = "Le Lorem Ipsum est euh simplement euh du faux euh texte."
for i in generator(txt, " "):
    print(i)
print("")
for i in generator(txt, " ", "ordered"):
    print(i)
print("")
for i in generator(txt, " ", "unique"):
    print(i)
print("")
for i in generator(txt, " ", "shuffle"):
    print(i)