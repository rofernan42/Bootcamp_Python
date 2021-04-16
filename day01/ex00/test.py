from book import Book
from recipe import Recipe

crepes = Recipe(
    "crepes",
    2,
    15,
    ["flour", "milk", "eggs"],
    "dessert",
    "Trop bon les crepes"
    )
sandwich = Recipe(
    "sandwich",
    1,
    5,
    ["ham", "butter", "bread"],
    "lunch",
    )
salad = Recipe(
    "salad",
    1,
    10,
    ["lettuce", "tomatoes", "avocado", "nuts"],
    "starter",
    )
cake = Recipe(
    "cake",
    4,
    30,
    ["flour", "yogurt", "eggs", "sugar"],
    "dessert",
    )

print("print(crepes):")
print(crepes)
to_print = str(crepes)
print("print(to_print):")
print(to_print)

book = Book("cookbook")
book.add_recipe(crepes)
book.add_recipe(sandwich)
book.add_recipe(salad)
book.add_recipe(cake)

book.get_recipes_by_types("starter")
book.get_recipes_by_types("lunch")
book.get_recipes_by_types("dessert")

rec = book.get_recipe_by_name("cake")
rec = book.get_recipe_by_name("crepes")
rec = book.get_recipe_by_name("sandwich")
rec = book.get_recipe_by_name("lalala")
rec = book.get_recipe_by_name("salad")
