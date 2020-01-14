import sys	

def print_choices():
	print("Please select an option by typing the corresponding number:")
	print("1:\t Add a recipe")
	print("2:\t Delete a recipe")
	print("3:\t Print a recipe")
	print("4:\t Print the cookbook")
	print("5:\t Quit")

def add_recipe(cookbook):
	rec = input("Enter recipe name:\n")
	cookbook[rec] = {'ingredients' : list, 'meal' : str, 'prep_time' : str}
	for itm in cookbook[rec]:
		if itm == 'ingredients':
			chaine = input("{}: ".format(itm))
			for c in chaine:
				if (c.isalnum()) is False:
					chaine = chaine.replace(c, ' ')
				cookbook[rec][itm] = chaine.split()
		else:
			cookbook[rec][itm] = input("{}: ".format(itm))

def del_recipe(cookbook):
	try:
		rec = input("Enter recipe name to delete:\n")
		cookbook.pop(rec)
		print(rec.capitalize(), "recipe removed from cookbook.\n")
	except KeyError:
		print("Recipe not in the cookbook.\n")

def print_recipe(cookbook):
	try:
		rec = input("Please enter the recipe name to get its details:\n")
		print("Recipe for %s:" % rec)
		print("Ingredients list: ", cookbook[rec]['ingredients'])
		print("To be eaten for %s." % cookbook[rec]['meal'])
		print("Takes %s of cooking.\n" % cookbook[rec]['prep_time'])
	except KeyError:
		print("Recipe not in the cookbook.\n")

def print_cookbook(cookbook):
	for rec in cookbook:
		print("-", rec.capitalize())
	print("")


cookbook = {
	'sandwich' : {'ingredients' : ['ham', 'bread', 'cheese','tomatoes'], 'meal' : 'lunch', 'prep_time' : '10 minutes'},
	'cake' : {'ingredients' : ['flour', 'sugar', 'eggs'], 'meal' : 'dessert', 'prep_time' : '60 minutes'},
	'salad' : {'ingredients' : ['avocado', 'arugula', 'tomatoes','spinach'], 'meal' : 'lunch', 'prep_time' : '15 minutes'}
}
while 1:
	print_choices()
	choix = input()
	if choix == '1':
		add_recipe(cookbook)
	elif choix == '2':
		del_recipe(cookbook)
	elif choix == '3':
		print_recipe(cookbook)
	elif choix == '4':
		print_cookbook(cookbook)
	elif choix == '5':
		sys.exit("Cookbook closed.")
	else:
		print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.\n")
