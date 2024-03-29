import sys
sos = {
    'a': '.−',
    'b': '−...',
    'c': '−.−.',
    'd': '−..',
    'e': '.',
    'f': '..−.',
    'g': '−−.',
    'h': '....',
    'i': '..',
    'j': '.−−−',
    'k': '−.−',
    'l': '.−..',
    'm': '−−',
    'n': '−.',
    'o': '−−−',
    'p': '.−−.',
    'q': '−−.−',
    'r': '.−.',
    's': '...',
    't': '−',
    'u': '..−',
    'v': '...−',
    'w': '.−−',
    'x': '−..−',
    'y': '−.−−',
    'z': '−−..',
    '0': '−−−−−',
    '1': '.−−−−',
    '2': '..−−−',
    '3': '...−−',
    '4': '....−',
    '5': '.....',
    '6': '−....',
    '7': '−−...',
    '8': '−−−..',
    '9': '−−−−.',
    ' ': '/'
}

try:
    string = ' '.join(sys.argv[1:]).lower()
    print(' '.join([sos[c] for c in string]))
except:
    sys.exit("ERROR")