import sys
try:
    chaine = str(sys.argv[1])
    n = int(sys.argv[2])
except:
    sys.exit("ERROR")
for c in chaine:
    if c.isalnum() is False:
        chaine = chaine.replace(c, ' ')
lst = chaine.split()
print([elem for elem in lst if len(elem) > n])