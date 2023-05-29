minetest.register_node(name..":!block.id", {
	description = "!block.name",
	tiles = {"!block.id.png"},
	groups = {cracky = 3},
	stack_max = stack,
})