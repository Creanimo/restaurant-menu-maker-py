from restaurantmenu import item, ingredient, substance, substance_map

zutat_schmand = ingredient.Ingredient("Schmand")

zutat_erdnusssahnesosse = ingredient.Ingredient("Erdnusssoße")
zutat_ketchup = ingredient.Ingredient("Ketchup")

allergen_milch = substance.Allergen("Milch", "🐮")
allergen_erdnuss = substance.Allergen("Erdnuss", "🥜")

additive_farbstoff = substance.Additive("Farbstoff", "🔴", "E102")

substance_map = substance_map.SubstanceMap()

substance_map.add_ingredient(zutat_schmand, allergen_milch)
substance_map.add_ingredient(zutat_erdnusssahnesosse, allergen_milch, allergen_erdnuss)
substance_map.add_ingredient(zutat_ketchup, additive_farbstoff)

substance_map.print_map()