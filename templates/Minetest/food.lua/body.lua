minetest.register_craftitem(name..":!food.id", {
	description = "!food.name",
	inventory_image = "!food.id.png",
	stack_max = stack,
	on_use = minetest.item_eat(1),
})