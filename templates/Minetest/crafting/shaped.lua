minetest.register_craft({
	output = "!recipe.output !recipe.amount",
	recipe = {
		{"!recipe.ingredient_1", "!recipe.ingredient_2", "!recipe.ingredient_3"},
		{"!recipe.ingredient_4", "!recipe.ingredient_5", "!recipe.ingredient_6"},
		{"!recipe.ingredient_7", "!recipe.ingredient_8", "!recipe.ingredient_9"},
	}
})