import sys
error = "Usage: python " + sys.argv[0] + "\nExample:\n\tpython " + sys.argv[0] + " 10 3"
if len(sys.argv) == 3:
    try:
        nb1 = int(sys.argv[1])
        nb2 = int(sys.argv[2])
    except:
        sys.exit("InputError: only numbers\n\n" + error)
    print("Sum:\t\t" + "%s" % (nb1 + nb2))
    print("Difference:\t" + "%s" % (nb1 - nb2))
    print("Product:\t" + "%s" % (nb1 * nb2))
    if nb2 == 0:
        print("Quotient:\tERROR (div by zero)")
        print("Remainder:\tERROR (modulo by zero)")
    else:
        print("Quotient:\t" + "%s" % (nb1 / float(nb2)))
        print("Remainder:\t" + "%s" % (nb1 % nb2))
elif len(sys.argv) < 3:
    sys.exit(error)
else:
    sys.exit("InputError: too many arguments\n\n" + error)