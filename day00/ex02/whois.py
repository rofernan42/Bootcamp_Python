import sys
if len(sys.argv) > 2:
	sys.exit("ERROR")
elif len(sys.argv) == 2:
	try:
		nbr = int(sys.argv[1])
	except:
		sys.exit("ERROR")
	if nbr == 0:
		sys.exit("I'm Zero.")
	elif nbr % 2 == 0:
		sys.exit("I'm Even.")
	else:
		sys.exit("I'm Odd.")