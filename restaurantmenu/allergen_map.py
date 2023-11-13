# A module that handles the mapping between ingredients and allergens

# Import the allergen and ingredient classes from the other modules
from restaurantmenu import allergen
from restaurantmenu import ingredient

# A dictionary that maps each ingredient object to a set of allergen objects
ingredient_to_allergen: dict[ingredient.Ingredient, set[allergen.Allergen]] | dict[None, None] = {}

# A dictionary that maps each allergen object to a set of ingredient objects
allergen_to_ingredient: dict[allergen.Allergen, set[ingredient.Ingredient]] | dict[None, None] = {}

# A function that returns the set of allergen objects for a given ingredient object
def get_allergens(ingredient: ingredient.Ingredient) -> set[allergen.Allergen]:
    return ingredient_to_allergen.get(ingredient, set())

# A function that returns the set of ingredient objects for a given allergen object
def get_ingredients(allergen: allergen.Allergen) -> set[ingredient.Ingredient]:
    return allergen_to_ingredient.get(allergen, set())

# A function that adds a new ingredient object and its allergens to the mapping
def add_ingredient(ingredient: ingredient.Ingredient, *allergens: allergen.Allergen) -> None:
    ingredient_to_allergen[ingredient] = allergens
    for allergen in allergens:
        allergen_to_ingredient.setdefault(allergen, set()).add(ingredient)

# A function that removes an ingredient object and its allergens from the mapping
def remove_ingredient(ingredient: ingredient.Ingredient) -> None:
    allergens = ingredient_to_allergen.pop(ingredient, set())
    for allergen in allergens:
        allergen_to_ingredient[allergen].remove(ingredient)
        if not allergen_to_ingredient[allergen]:
            allergen_to_ingredient.pop(allergen)