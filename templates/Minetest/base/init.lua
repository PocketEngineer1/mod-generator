local name = "!mod.id"
local path = minetest.get_modpath(name)

dofile(path.."/nodes.lua")
dofile(path.."/craftitems.lua")

dofile(path.."/crafting/shaped.lua")
dofile(path.."/crafting/shapeless.lua")
dofile(path.."/crafting/smelting.lua")