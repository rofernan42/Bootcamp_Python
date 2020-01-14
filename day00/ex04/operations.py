import sys

def operations(x, y):	
	print("Sum:\t\t", x + y)
	print("Difference:\t", x - y)
	print("Product:\t", x * y)
	if y == 0:
		print("Quotient:\t ERROR (div by zero)")
		print("Remainder:\t ERROR (modulo by zero)")
	else:
		print("Quotient:\t", x / y)
		print("Remainder:\t", x % y)

txterror = "Usage:\tpython operations.py\nExample:\n\tpython " + sys.argv[0] + " 10 3"
if len(sys.argv) < 3:
	sys.exit(txterror)
elif len(sys.argv) > 3:
	print("InputError: too many arguments\n")
	sys.exit(txterror)
else:
	try:
		nbr1 = int(sys.argv[1])
		nbr2 = int(sys.argv[2])
	except:
		print("InputError: only numbers\n")
		sys.exit(txterror)
	operations(nbr1, nbr2)