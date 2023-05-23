minetest.register_craft({
	type = "cooking",
	output = "!recipe.output !recipe.amount",
	recipe = "!recipe.ingredient",
})