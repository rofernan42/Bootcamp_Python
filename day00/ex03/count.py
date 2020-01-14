def text_analyzer(txt):
	"""\nThis function counts the number of upper characters, lower characters, punctuation and spaces in a given text.\n"""
	if not txt:
		txt = input("What is the text to anayze?\n")
	upp = 0
	low = 0
	pct = 0
	spc = 0
	for c in txt:
		if (c.isupper()):
			upp += 1
		if (c.islower()):
			low += 1
		if (c.isalnum() or c.isspace()) == False:
			pct += 1
		if c.isspace():
			spc += 1
	print("The text contains", len(txt), "characters:")
	print("-", upp, "upper letters")
	print("-", low, "lower letters")
	print("-", pct, "punctuation marks")
	print("-", spc, "spaces")
# Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.
