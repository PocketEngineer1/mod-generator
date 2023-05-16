import os, shutil

def Generate(mod):
    if os.path.exists('output/Minetest') != True:
        os.mkdir('output/Minetest')

    # mod.conf
    with open('templates/Minetest/base/mod.conf', 'r') as f:
        file = f.read()
        f.close()

    file = file.replace('!mod.id', mod['mod']['id'])
    file = file.replace('!mod.name', mod['mod']['name'])
    file = file.replace('!mod.desc', mod['mod']['desc'])
    file = file.replace('!mod.author', mod['mod']['author'])

    with open('output/Minetest/mod.conf', 'w') as f:
        f.write(file)
        f.close()

    del file

    # init.lua
    with open('templates/Minetest/base/init.lua', 'r') as f:
        file = f.read()
        f.close()

    file = file.replace('!mod.id', mod['mod']['id'])
    file = file.replace('!mod.name', mod['mod']['name'])
    file = file.replace('!mod.desc', mod['mod']['desc'])
    file = file.replace('!mod.author', mod['mod']['author'])

    with open('output/Minetest/init.lua', 'w') as f:
        f.write(file)
        f.close()

    del file

    # craftitems.lua
    with open('templates/Minetest/craftitems.lua/head.lua', 'r') as f:
        file = f.read()
        f.close()

    file = file.replace('!mod.id', mod['mod']['id'])
    file = file.replace('!mod.name', mod['mod']['name'])
    file = file.replace('!mod.desc', mod['mod']['desc'])
    file = file.replace('!mod.author', mod['mod']['author'])
    file += "\n\n"

    with open('output/Minetest/craftitems.lua', 'w') as f:
        f.write(file)
        f.close()
    
    with open('templates/Minetest/craftitems.lua/body.lua', 'r') as f:
        template = f.read()
        f.close()

    with open('output/Minetest/craftitems.lua', 'a') as f:
        for i in mod['elements']['items']:
            out = template
            out = out.replace('!item.id', i['id'])
            out = out.replace('!item.name', i['name'])
            out += "\n\n"
            f.write(out)
    
    with open('output/Minetest/craftitems.lua', 'r') as f:
        file = f.read()
        f.close()
    
    with open('output/Minetest/craftitems.lua', 'w') as f:
        f.write(file.rstrip())
        f.close()

    del file, template

    # nodes.lua
    with open('templates/Minetest/nodes.lua/head.lua', 'r') as f:
        file = f.read()
        f.close()

    file = file.replace('!mod.id', mod['mod']['id'])
    file = file.replace('!mod.name', mod['mod']['name'])
    file = file.replace('!mod.desc', mod['mod']['desc'])
    file = file.replace('!mod.author', mod['mod']['author'])
    file += "\n\n"

    with open('output/Minetest/nodes.lua', 'w') as f:
        f.write(file)
        f.close()
    
    with open('templates/Minetest/nodes.lua/body.lua', 'r') as f:
        template = f.read()
        f.close()

    with open('output/Minetest/nodes.lua', 'a') as f:
        for i in mod['elements']['blocks']:
            out = template
            out = out.replace('!block.id', i['id'])
            out = out.replace('!block.name', i['name'])
            out += "\n\n"
            f.write(out)
    
    with open('output/Minetest/nodes.lua', 'r') as f:
        file = f.read()
        f.close()
    
    with open('output/Minetest/nodes.lua', 'w') as f:
        f.write(file.rstrip())
        f.close()

    del file, template

    # assets
    if os.path.exists('output/Minetest/textures'):
        shutil.rmtree('output/Minetest/textures')
    shutil.copytree('assets/textures', 'output/Minetest/textures')
