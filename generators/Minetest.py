import os, shutil
from functions import *

def Generate(mod, args):
    if os.path.exists('output/Minetest') != True:
        os.mkdir('output/Minetest')

    if os.path.exists('output/Minetest/crafting') != True:
        os.mkdir('output/Minetest/crafting')

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
        if len(mod['elements']['items']) > 0:
            for i in mod['elements']['items']:
                out = template
                out = out.replace('!item.id', i['id'])
                out = out.replace('!item.name', i['name'])
                out += "\n\n"
                f.write(out)
        else:
            f.write('-- No items to register')
        f.close()

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
        if len(mod['elements']['blocks']) > 0:
            for i in mod['elements']['blocks']:
                out = template
                out = out.replace('!block.id', i['id'])
                out = out.replace('!block.name', i['name'])
                out += "\n\n"
                f.write(out)
        else:
            f.write('-- No blocks to register')
        f.close()
    
    with open('output/Minetest/nodes.lua', 'r') as f:
        file = f.read()
        f.close()
    
    with open('output/Minetest/nodes.lua', 'w') as f:
        f.write(file.rstrip())
        f.close()

    # crafting/shaped.lua
    with open('output/Minetest/crafting/shaped.lua', 'w') as f:
        f.write('')
        f.close()

    with open('templates/Minetest/crafting/shaped.lua', 'r') as f:
        template = f.read()
        f.close()

    with open('output/Minetest/crafting/shaped.lua', 'a') as f:
        if len(mod['recipes']['shaped']) > 0:
            for i in mod['recipes']['shaped']:
                out = template
                out = out.replace('!recipe.amount', str(i['amount']))

                write = False

                #region output
                outputItem = i['output']
                outputItem = str(outputItem)

                if outputItem.startswith('!mod.'):
                    outputItem = outputItem.split('!mod.', 1)[1]
                    for j in mod['elements']['items']:
                        if outputItem == j['id']:
                            out = out.replace('!recipe.output', mod['mod']['id'] + ':' + j['id'])
                            write = True
                            break
                    for j in mod['elements']['blocks']:
                        if outputItem == j['id']:
                            out = out.replace('!recipe.output', mod['mod']['id'] + ':' + j['id'])
                            write = True
                            break
                elif outputItem.startswith('!item_definitions.'):
                    outputItem = outputItem.split('!item_definitions.', 1)[1]
                    for j in mod['item_definitions']['Minetest']:
                        if j == outputItem:
                            out = out.replace('!recipe.output', mod['item_definitions']['Minetest'][j])
                            write = True
                            break
                #endregion

                #region ingredients
                #region 1
                outputItem = i['recipe'][0][0]
                outputItem = str(outputItem)

                if outputItem.startswith('!mod.'):
                    outputItem = outputItem.split('!mod.', 1)[1]
                    for j in mod['elements']['items']:
                        if outputItem == j['id']:
                            out = out.replace('!recipe.ingredient_1', mod['mod']['id'] + ':' + j['id'])
                            write = True
                            break
                    for j in mod['elements']['blocks']:
                        if outputItem == j['id']:
                            out = out.replace('!recipe.ingredient_1', mod['mod']['id'] + ':' + j['id'])
                            write = True
                            break
                elif outputItem.startswith('!item_definitions.'):
                    outputItem = outputItem.split('!item_definitions.', 1)[1]
                    for j in mod['item_definitions']['Minetest']:
                        if j == outputItem:
                            out = out.replace('!recipe.ingredient_1', mod['item_definitions']['Minetest'][j])
                            write = True
                            break
                #endregion

                #region 2
                outputItem = i['recipe'][0][1]
                outputItem = str(outputItem)

                if outputItem.startswith('!mod.'):
                    outputItem = outputItem.split('!mod.', 1)[1]
                    for j in mod['elements']['items']:
                        if outputItem == j['id']:
                            out = out.replace('!recipe.ingredient_2', mod['mod']['id'] + ':' + j['id'])
                            write = True
                            break
                    for j in mod['elements']['blocks']:
                        if outputItem == j['id']:
                            out = out.replace('!recipe.ingredient_2', mod['mod']['id'] + ':' + j['id'])
                            write = True
                            break
                elif outputItem.startswith('!item_definitions.'):
                    outputItem = outputItem.split('!item_definitions.', 1)[1]
                    for j in mod['item_definitions']['Minetest']:
                        if j == outputItem:
                            out = out.replace('!recipe.ingredient_2', mod['item_definitions']['Minetest'][j])
                            write = True
                            break
                #endregion
                
                #region 3
                outputItem = i['recipe'][0][2]
                outputItem = str(outputItem)

                if outputItem.startswith('!mod.'):
                    outputItem = outputItem.split('!mod.', 1)[1]
                    for j in mod['elements']['items']:
                        if outputItem == j['id']:
                            out = out.replace('!recipe.ingredient_3', mod['mod']['id'] + ':' + j['id'])
                            write = True
                            break
                    for j in mod['elements']['blocks']:
                        if outputItem == j['id']:
                            out = out.replace('!recipe.ingredient_3', mod['mod']['id'] + ':' + j['id'])
                            write = True
                            break
                elif outputItem.startswith('!item_definitions.'):
                    outputItem = outputItem.split('!item_definitions.', 1)[1]
                    for j in mod['item_definitions']['Minetest']:
                        if j == outputItem:
                            out = out.replace('!recipe.ingredient_3', mod['item_definitions']['Minetest'][j])
                            write = True
                            break
                #endregion
                
                #region 4
                outputItem = i['recipe'][1][0]
                outputItem = str(outputItem)

                if outputItem.startswith('!mod.'):
                    outputItem = outputItem.split('!mod.', 1)[1]
                    for j in mod['elements']['items']:
                        if outputItem == j['id']:
                            out = out.replace('!recipe.ingredient_4', mod['mod']['id'] + ':' + j['id'])
                            write = True
                            break
                    for j in mod['elements']['blocks']:
                        if outputItem == j['id']:
                            out = out.replace('!recipe.ingredient_4', mod['mod']['id'] + ':' + j['id'])
                            write = True
                            break
                elif outputItem.startswith('!item_definitions.'):
                    outputItem = outputItem.split('!item_definitions.', 1)[1]
                    for j in mod['item_definitions']['Minetest']:
                        if j == outputItem:
                            out = out.replace('!recipe.ingredient_4', mod['item_definitions']['Minetest'][j])
                            write = True
                            break
                #endregion

                #region 5
                outputItem = i['recipe'][1][1]
                outputItem = str(outputItem)

                if outputItem.startswith('!mod.'):
                    outputItem = outputItem.split('!mod.', 1)[1]
                    for j in mod['elements']['items']:
                        if outputItem == j['id']:
                            out = out.replace('!recipe.ingredient_5', mod['mod']['id'] + ':' + j['id'])
                            write = True
                            break
                    for j in mod['elements']['blocks']:
                        if outputItem == j['id']:
                            out = out.replace('!recipe.ingredient_5', mod['mod']['id'] + ':' + j['id'])
                            write = True
                            break
                elif outputItem.startswith('!item_definitions.'):
                    outputItem = outputItem.split('!item_definitions.', 1)[1]
                    for j in mod['item_definitions']['Minetest']:
                        if j == outputItem:
                            out = out.replace('!recipe.ingredient_5', mod['item_definitions']['Minetest'][j])
                            write = True
                            break
                #endregion
                
                #region 6
                outputItem = i['recipe'][1][2]
                outputItem = str(outputItem)

                if outputItem.startswith('!mod.'):
                    outputItem = outputItem.split('!mod.', 1)[1]
                    for j in mod['elements']['items']:
                        if outputItem == j['id']:
                            out = out.replace('!recipe.ingredient_6', mod['mod']['id'] + ':' + j['id'])
                            write = True
                            break
                    for j in mod['elements']['blocks']:
                        if outputItem == j['id']:
                            out = out.replace('!recipe.ingredient_6', mod['mod']['id'] + ':' + j['id'])
                            write = True
                            break
                elif outputItem.startswith('!item_definitions.'):
                    outputItem = outputItem.split('!item_definitions.', 1)[1]
                    for j in mod['item_definitions']['Minetest']:
                        if j == outputItem:
                            out = out.replace('!recipe.ingredient_6', mod['item_definitions']['Minetest'][j])
                            write = True
                            break
                #endregion
                
                #region 7
                outputItem = i['recipe'][2][0]
                outputItem = str(outputItem)

                if outputItem.startswith('!mod.'):
                    outputItem = outputItem.split('!mod.', 1)[1]
                    for j in mod['elements']['items']:
                        if outputItem == j['id']:
                            out = out.replace('!recipe.ingredient_7', mod['mod']['id'] + ':' + j['id'])
                            write = True
                            break
                    for j in mod['elements']['blocks']:
                        if outputItem == j['id']:
                            out = out.replace('!recipe.ingredient_7', mod['mod']['id'] + ':' + j['id'])
                            write = True
                            break
                elif outputItem.startswith('!item_definitions.'):
                    outputItem = outputItem.split('!item_definitions.', 1)[1]
                    for j in mod['item_definitions']['Minetest']:
                        if j == outputItem:
                            out = out.replace('!recipe.ingredient_7', mod['item_definitions']['Minetest'][j])
                            write = True
                            break
                #endregion
                
                #region 8
                outputItem = i['recipe'][2][1]
                outputItem = str(outputItem)

                if outputItem.startswith('!mod.'):
                    outputItem = outputItem.split('!mod.', 1)[1]
                    for j in mod['elements']['items']:
                        if outputItem == j['id']:
                            out = out.replace('!recipe.ingredient_8', mod['mod']['id'] + ':' + j['id'])
                            write = True
                            break
                    for j in mod['elements']['blocks']:
                        if outputItem == j['id']:
                            out = out.replace('!recipe.ingredient_8', mod['mod']['id'] + ':' + j['id'])
                            write = True
                            break
                elif outputItem.startswith('!item_definitions.'):
                    outputItem = outputItem.split('!item_definitions.', 1)[1]
                    for j in mod['item_definitions']['Minetest']:
                        if j == outputItem:
                            out = out.replace('!recipe.ingredient_8', mod['item_definitions']['Minetest'][j])
                            write = True
                            break
                #endregion
                
                #region 9
                outputItem = i['recipe'][2][2]
                outputItem = str(outputItem)

                if outputItem.startswith('!mod.'):
                    outputItem = outputItem.split('!mod.', 1)[1]
                    for j in mod['elements']['items']:
                        if outputItem == j['id']:
                            out = out.replace('!recipe.ingredient_9', mod['mod']['id'] + ':' + j['id'])
                            write = True
                            break
                    for j in mod['elements']['blocks']:
                        if outputItem == j['id']:
                            out = out.replace('!recipe.ingredient_9', mod['mod']['id'] + ':' + j['id'])
                            write = True
                            break
                elif outputItem.startswith('!item_definitions.'):
                    outputItem = outputItem.split('!item_definitions.', 1)[1]
                    for j in mod['item_definitions']['Minetest']:
                        if j == outputItem:
                            out = out.replace('!recipe.ingredient_9', mod['item_definitions']['Minetest'][j])
                            write = True
                            break
                #endregion
                #endregion

                out += '\n\n'
                if write:
                    f.write(out)
                else:
                    f.write('-- Broken recipe\n\n')
        else:
            f.write('-- No shaped recipes to register')
        f.close()
    
    with open('output/Minetest/crafting/shaped.lua', 'r') as f:
        file = f.read()
        f.close()
    
    with open('output/Minetest/crafting/shaped.lua', 'w') as f:
        f.write(file.rstrip())
        f.close()

    del template

    # assets
    if os.path.exists('output/Minetest/textures'):
        shutil.rmtree('output/Minetest/textures')
    shutil.copytree('assets/textures', 'output/Minetest/textures')
