from datetime import datetime
from recipe import Recipe

class Error(Exception):
    def __init__(self, string):
        self.string = string

class Book:
    def __init__(self, name):
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {
            "starter": [],
            "lunch": [],
            "dessert": []
        }
    def get_recipe_by_name(self, name):
        """Print a recipe with the name 'name' and return the instance"""
        val = self.recipes_list.values()
        for i in val:
            for j in i:
                if name is j.name:
                    print(j)
                    return j
        print("Recipe not found.\n")
    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        if recipe_type not in self.recipes_list:
            raise Error("Recipe type must be 'starter', 'lunch' or 'dessert'.")
        print(">>> List of " + recipe_type + " recipes:")
        for i in self.recipes_list[recipe_type]:
            print("- " + i.name)
        print("")
        pass
    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            raise Error("Entry must be of Recipe type.")
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
        pass