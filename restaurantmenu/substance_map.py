from restaurantmenu import substance, ingredient

class SubstanceMap:
    
    def __init__(self):
        # A dictionary that maps each ingredient object to a set of substance objects
        self.ingredient_to_substance: dict[ingredient.Ingredient, set[substance.Substance]] | dict[None, None] = {}
        # A dictionary that maps each substance object to a set of ingredient objects
        self.substance_to_ingredient: dict[substance.Substance, set[ingredient.Ingredient]] | dict[None, None] = {}

    # A method that returns the set of substance objects for a given ingredient object
    def get_substances(self, ingredient: ingredient.Ingredient) -> set[substance.Substance]:
        return self.ingredient_to_substance.get(ingredient, set())

    # A method that returns the set of ingredient objects for a given substance object
    def get_ingredients(self, substance: substance.Substance) -> set[ingredient.Ingredient]:
        return self.substance_to_ingredient.get(substance, set())

    # A method that adds a new ingredient object and its substances to the mapping
    def add_ingredient(self, ingredient: ingredient.Ingredient, *substances: substance.Substance) -> None:
        self.ingredient_to_substance[ingredient] = substances
        for substance in substances:
            self.substance_to_ingredient.setdefault(substance, set()).add(ingredient)

    # A method that removes an ingredient object and its substances from the mapping
    def remove_ingredient(self, ingredient: ingredient.Ingredient) -> None:
        substances = self.ingredient_to_substance.pop(ingredient, set())
        for substance in substances:
            self.substance_to_ingredient[substance].remove(ingredient)
            if not self.substance_to_ingredient[substance]:
                self.substance_to_ingredient.pop(substance)

    # A method that prints the mapping in a human-readable format
    def print_map(self) -> None:
        for ingredient, substances in self.ingredient_to_substance.items():
            print(f"{ingredient.names[0]} contains:")
            for subst in substances:
                # Check the type of the substance object and print accordingly
                if isinstance(subst, substance.Allergen):
                    print(f"- {subst.name} ({subst.inline_icon})")
                elif isinstance(subst, substance.Additive):
                    print(f"- {subst.name} ({subst.code})")
                else:
                    print(f"- {subst.name}")
            print()