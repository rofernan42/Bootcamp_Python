import sys

def addrec(ingredients, meal, prep_time):
    recipe = {
        'ingredients': ingredients,
        'meal': meal,
        'prep_time': prep_time
    }
    return recipe

def deleterec(cookbook, name):
    del cookbook[name]
    print(">>>>> ", name, "deleted. <<<<<\n")

def recipe(name):
    print(">>>>> Ingredients list:", name['ingredients'])
    print(''.join((">>>>> To be eaten for ", name['meal'], ".")))
    print(''.join((">>>>> Takes ", name['prep_time'], " of cooking.\n")))

def printcb(cookbook):
    for i in cookbook:
        print("-", i)
    print("")

cookbook = {
    'sandwich': {
        'ingredients': ["ham","bread","cheese"],
        'meal': "lunch",
        'prep_time': "10 minutes"
    },
    'cake': {
        'ingredients': ["flour","sugar","eggs"],
        'meal': "dessert",
        'prep_time': "60 minutes"
    },
    'salad': {
        'ingredients': ["avocado","arugula","tomatoes", "spinach"],
        'meal': "lunch",
        'prep_time': "15 minutes"
    }
}

while (1):
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    choice = input()
    if choice == "1":
        name = input(">>> Name of the recipe: ")
        if name in cookbook:
            print("\t>>>>> This recipe already exists. <<<<<\n")
        else:
            ingredients = input(">>> Ingredients: ")
            meal = input(">>> Type of meal: ")
            prep_time = input(">>> Preparation time: ")
            cookbook[name] = addrec(ingredients, meal, prep_time)
            print("\n>>>>> Recipe created ! <<<<<\n")
    elif choice == "2":
        print(">>> Which recipe would you like to delete?")
        try:
            name = input()
            deleterec(cookbook, name)
        except:
            print(">>>>> Recipe not in the cookbook. <<<<<\n")
    elif choice == "3":
        print(">>> Please enter the recipe's name to get its details:")
        try:
            name = input()
            recipe(cookbook[name])
        except:
            print(">>>>> Recipe not in the cookbook. <<<<<\n")
    elif choice == "4":
        printcb(cookbook)
    elif choice == "5":
        sys.exit("Cookbook closed.")
    else:
        print(">>>>> This option does not exist, please type the corresponding number.\nTo exit, enter 5. <<<<<\n")
