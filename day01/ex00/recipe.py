class Error(Exception):
    def __init__(self, string):
        self.string = string

class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description = ""):
        self.name = name
        if cooking_lvl not in range(1, 5):
            raise Error("Cooking level must be between 1 and 5.")
        self.cooking_lvl = cooking_lvl
        if cooking_time < 0:
            raise Error("Cooking time cannot be negative.")
        self.cooking_time = cooking_time
        if type(ingredients) is not list:
            raise Error("Ingredients must be a list.")
        if not all(isinstance(i, str) for i in ingredients):
            raise Error("Ingredients must be strings.")
        self.ingredients = ingredients
        self.description = description
        if recipe_type not in ("starter", "lunch", "dessert"):
            raise Error("Type must be starter, lunch or dessert.")
        self.recipe_type = recipe_type

    def __str__(self): # en C++ equivalent a: std::ostream &operator<<(std::ostream &output, Fixed const &b);
        """Return the string to print with the recipe info"""
        txt = f">>> Recipe name: {self.name}\n"
        txt += f">>> Level of difficulty: {self.cooking_lvl}/5\n"
        txt += f">>> Cooking time: {self.cooking_time} minutes\n"
        txt += f">>> Ingredients: " + ', '.join([i for i in self.ingredients]) + "\n"
        txt += f">>> To be eaten for {self.recipe_type}\n"
        if len(self.description):
            txt += f">>> Description: {self.description}\n"
        return txt
