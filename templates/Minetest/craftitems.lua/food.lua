minetest.register_craftitem(name..":!item.id", {
	description = "!item.name",
	inventory_image = "!item.id.png",
	stack_max = stack,
	on_use = minetest.item_eat(1),
})