import os, shutil
from functions import *

def Generate(mod, args):
    #region Directories
    def Task():
        if os.path.exists('output/Minetest') != True:
            os.mkdir('output/Minetest')

        if os.path.exists('output/Minetest/crafting') != True:
            os.mkdir('output/Minetest/crafting')

        if os.path.exists('output/Minetest/textures') != True:
            os.mkdir('output/Minetest/textures')

        if os.path.exists('output/Minetest/textures/blocks') != True:
            os.mkdir('output/Minetest/textures/blocks')

        if os.path.exists('output/Minetest/textures/items') != True:
            os.mkdir('output/Minetest/textures/items')
    
    RunTask(Task, 'Create output directories')
    del Task
    #endregion

    #region mod.conf
    def Task():
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
    
    RunTask(Task, 'Create mod.conf')
    del Task
    #endregion

    #region init.lua
    def Task():
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
    
    RunTask(Task, 'Create init.lua')
    del Task
    #endregion

    #region craftitems.lua
    def Task():
        with open('templates/Minetest/craftitems.lua/head.lua', 'r') as f:
            file = f.read()
            f.close()

        file = file.replace('!mod.id', mod['mod']['id'])
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
    
    RunTask(Task, 'Create craftitems.lua')
    del Task
    #endregion

    #region nodes.lua
    def Task():
        with open('templates/Minetest/nodes.lua/head.lua', 'r') as f:
            file = f.read()
            f.close()

        file = file.replace('!mod.id', mod['mod']['id'])
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
    
    RunTask(Task, 'Create nodes.lua')
    del Task
    #endregion

    #region food.lua
    def Task():
        with open('templates/Minetest/food.lua/head.lua', 'r') as f:
            file = f.read()
            f.close()

        file = file.replace('!mod.id', mod['mod']['id'])
        file += "\n\n"

        with open('output/Minetest/food.lua', 'w') as f:
            f.write(file)
            f.close()
        
        with open('templates/Minetest/food.lua/body.lua', 'r') as f:
            template = f.read()
            f.close()

        with open('output/Minetest/food.lua', 'a') as f:
            if len(mod['elements']['food']) > 0:
                for i in mod['elements']['food']:
                    out = template
                    out = out.replace('!food.id', i['id'])
                    out = out.replace('!food.name', i['name'])
                    out += "\n\n"
                    f.write(out)
            else:
                f.write('-- No food to register')
            f.close()
        
        with open('output/Minetest/food.lua', 'r') as f:
            file = f.read()
            f.close()
        
        with open('output/Minetest/food.lua', 'w') as f:
            f.write(file.rstrip())
            f.close()
    
    RunTask(Task, 'Create food.lua')
    del Task
    #endregion

    #region crafting
    def Task():
        #region shaped.lua
        def SubTask():
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
                        out = out.replace('!recipe.ingredient_1', '')
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
                        out = out.replace('!recipe.ingredient_2', '')
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
                        out = out.replace('!recipe.ingredient_3', '')
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
                        out = out.replace('!recipe.ingredient_4', '')
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
                        out = out.replace('!recipe.ingredient_5', '')
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
                        out = out.replace('!recipe.ingredient_6', '')
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
                        out = out.replace('!recipe.ingredient_7', '')
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
                        out = out.replace('!recipe.ingredient_8', '')
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
                        out = out.replace('!recipe.ingredient_9', '')
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
        
        RunTask(SubTask, 'Create shaped.lua', True)
        del SubTask
        #endregion
    
        #region shapeless
        def SubTask():
            if len(mod['recipes']['shapeless']) > 0:
                Log('Shapeless recipes not implemented', 'WARN')

        RunTask(SubTask, 'Create shapeless.lua', True)
        del SubTask
        #endregion

        #region smelting
        def SubTask():
            if len(mod['recipes']['smelting']) > 0:
                Log('Smelting recipes not implemented', 'WARN')

        RunTask(SubTask, 'Create smelting.lua', True)
        del SubTask
        #endregion
    RunTask(Task, 'Create recipe files')
    del Task
    #endregion

    #region assets
    def Task():
        if os.path.exists('output/Minetest/textures/items'):
            shutil.rmtree('output/Minetest/textures/items')
        shutil.copytree('assets/textures/items', 'output/Minetest/textures/items')
        
        if os.path.exists('output/Minetest/textures/blocks'):
            shutil.rmtree('output/Minetest/textures/blocks')
        shutil.copytree('assets/textures/blocks', 'output/Minetest/textures/blocks')
    
    RunTask(Task, 'Copy assets to output')
    del Task
    #endregion
