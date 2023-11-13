from __future__ import annotations
from dataclasses import dataclass, field
from restaurantmenu import ingredient
from restaurantmenu import allergen_map

@dataclass
class Item:
    title: str
    description: str
    base_variations: list[ingredient.Ingredient] | list[None] = field(default_factory=list)
    ingredients: list[ingredient.Ingredient] | list[None] = field(default_factory=list)

    # A method that returns the set of allergen objects for the item
    def get_allergens(self) -> set[allergen.Allergen]:
        allergens = set()
        for ing in self.base_variations + self.ingredients:
            if ing is not None:
                allergens.update(allergen_map.get_allergens(ing))
        return allergens