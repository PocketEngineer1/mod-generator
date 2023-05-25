minetest.register_node(name..":!glass.id", {
	description = "!glass.name",
	tiles = {"!glass.id.png"},
	groups = {cracky = 3},
	stack_max = stack,
	drawtype = "glasslike",
	paramtype = "light",
	sunlight_propagates = true,
})