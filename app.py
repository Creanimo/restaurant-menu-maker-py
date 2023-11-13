from restaurantmenu import item, ingredient, allergen, allergen_map

zutat_schmand = ingredient.Ingredient("Schmand")
zutat_erdnusssahnesosse = ingredient.Ingredient("Erdnusssoße")

allergen_milch = allergen.Allergen("Milch", "🐮")
allergen_erdnuss = allergen.Allergen("Erdnuss", "🥜")

allergen_map.add_ingredient(zutat_schmand, allergen_milch)
allergen_map.add_ingredient(zutat_erdnusssahnesosse, allergen_milch, allergen_erdnuss)

print(allergen_map.ingredient_to_allergen)
print(allergen_map.allergen_to_ingredient)