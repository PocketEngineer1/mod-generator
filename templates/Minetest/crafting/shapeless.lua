minetest.register_craft({
	type = "shapeless",
	output = "!recipe.output !recipe.amount",
	recipe = {!recipe.ingredients
	}
})