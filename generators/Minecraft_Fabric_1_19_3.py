import os, shutil
from functions import *

def Generate(mod, args):
    #region Directories
    def Task():
        global java_pkg
        global java_pkg_path
        if os.path.exists('output/Minecraft Fabric 1.19.3') != True:
            os.mkdir('output/Minecraft Fabric 1.19.3')

        if os.path.exists('output/Minecraft Fabric 1.19.3/src') != True:
            os.mkdir('output/Minecraft Fabric 1.19.3/src')

        if os.path.exists('output/Minecraft Fabric 1.19.3/src/main') != True:
            os.mkdir('output/Minecraft Fabric 1.19.3/src/main')

        #region java
        if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/java') != True:
            os.mkdir('output/Minecraft Fabric 1.19.3/src/main/java')

        if len(mod['mod']['java_package']) == 3:
            java_pkg_path = mod['mod']['java_package'][0] + '/' + mod['mod']['java_package'][1] + '/' + mod['mod']['java_package'][2]
            java_pkg = mod['mod']['java_package'][0] + '.' + mod['mod']['java_package'][1] + '.' + mod['mod']['java_package'][2]

            if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/java/' + mod['mod']['java_package'][0]) != True:
                os.mkdir('output/Minecraft Fabric 1.19.3/src/main/java/' + mod['mod']['java_package'][0])

            if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/java/' + mod['mod']['java_package'][0] + '/' + mod['mod']['java_package'][1]) != True:
                os.mkdir('output/Minecraft Fabric 1.19.3/src/main/java/' + mod['mod']['java_package'][0] + '/' + mod['mod']['java_package'][1])

            if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/java/' + mod['mod']['java_package'][0] + '/' + mod['mod']['java_package'][1] + '/' + mod['mod']['java_package'][2]) != True:
                os.mkdir('output/Minecraft Fabric 1.19.3/src/main/java/' + mod['mod']['java_package'][0] + '/' + mod['mod']['java_package'][1] + '/' + mod['mod']['java_package'][2])

            if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/java/' + mod['mod']['java_package'][0] + '/' + mod['mod']['java_package'][1] + '/' + mod['mod']['java_package'][2] + '/Blocks') != True:
                os.mkdir('output/Minecraft Fabric 1.19.3/src/main/java/' + mod['mod']['java_package'][0] + '/' + mod['mod']['java_package'][1] + '/' + mod['mod']['java_package'][2] + '/Blocks')

            if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/java/' + mod['mod']['java_package'][0] + '/' + mod['mod']['java_package'][1] + '/' + mod['mod']['java_package'][2] + '/Items') != True:
                os.mkdir('output/Minecraft Fabric 1.19.3/src/main/java/' + mod['mod']['java_package'][0] + '/' + mod['mod']['java_package'][1] + '/' + mod['mod']['java_package'][2] + '/Items')
        elif len(mod['mod']['java_package']) == 2:
            java_pkg_path = mod['mod']['java_package'][0] + '/' + mod['mod']['java_package'][1]
            java_pkg = mod['mod']['java_package'][0] + '.' + mod['mod']['java_package'][1]

            if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/java/' + mod['mod']['java_package'][0]) != True:
                os.mkdir('output/Minecraft Fabric 1.19.3/src/main/java/' + mod['mod']['java_package'][0])

            if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/java/' + mod['mod']['java_package'][0] + '/' + mod['mod']['java_package'][1]) != True:
                os.mkdir('output/Minecraft Fabric 1.19.3/src/main/java/' + mod['mod']['java_package'][0] + '/' + mod['mod']['java_package'][1])

            if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/java/' + mod['mod']['java_package'][0] + '/' + mod['mod']['java_package'][1] + '/Blocks') != True:
                os.mkdir('output/Minecraft Fabric 1.19.3/src/main/java/' + mod['mod']['java_package'][0] + '/' + mod['mod']['java_package'][1] + '/Blocks')

            if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/java/' + mod['mod']['java_package'][0] + '/' + mod['mod']['java_package'][1] + '/Items') != True:
                os.mkdir('output/Minecraft Fabric 1.19.3/src/main/java/' + mod['mod']['java_package'][0] + '/' + mod['mod']['java_package'][1] + '/Items')
        else:
            raise KeyError('Invalid java package length, len(mod[\'mod\'][\'java_package\']) != 2 or 3')
        #endregion

        #region resources
        if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources') != True:
            os.mkdir('output/Minecraft Fabric 1.19.3/src/main/resources')

        #region assets
        if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources/assets') != True:
            os.mkdir('output/Minecraft Fabric 1.19.3/src/main/resources/assets')

        if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources/data') != True:
            os.mkdir('output/Minecraft Fabric 1.19.3/src/main/resources/data')

        if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id']) != True:
            os.mkdir('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'])

        if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/blockstates') != True:
            os.mkdir('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/blockstates')

        if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/lang') != True:
            os.mkdir('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/lang')

        if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/models') != True:
            os.mkdir('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/models')

        if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/textures') != True:
            os.mkdir('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/textures')

        if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/textures/item') != True:
            os.mkdir('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/textures/item')

        if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/textures/block') != True:
            os.mkdir('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/textures/block')

        if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/models/block') != True:
            os.mkdir('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/models/block')

        if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/models/item') != True:
            os.mkdir('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/models/item')
        #endregion

        #region data
        if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources/data/minecraft') != True:
            os.mkdir('output/Minecraft Fabric 1.19.3/src/main/resources/data/minecraft')

        if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources/data/minecraft/tags') != True:
            os.mkdir('output/Minecraft Fabric 1.19.3/src/main/resources/data/minecraft/tags')

        if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources/data/minecraft/tags/blocks') != True:
            os.mkdir('output/Minecraft Fabric 1.19.3/src/main/resources/data/minecraft/tags/blocks')

        if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources/data/minecraft/tags/blocks/mineable') != True:
            os.mkdir('output/Minecraft Fabric 1.19.3/src/main/resources/data/minecraft/tags/blocks/mineable')

        if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources/data/' + mod['mod']['id']) != True:
            os.mkdir('output/Minecraft Fabric 1.19.3/src/main/resources/data/' + mod['mod']['id'])

        if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources/data/' + mod['mod']['id'] + '/recipes') != True:
            os.mkdir('output/Minecraft Fabric 1.19.3/src/main/resources/data/' + mod['mod']['id'] + '/recipes')

        if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources/data/' + mod['mod']['id'] + '/loot_tables') != True:
            os.mkdir('output/Minecraft Fabric 1.19.3/src/main/resources/data/' + mod['mod']['id'] + '/loot_tables')

        if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources/data/' + mod['mod']['id'] + '/loot_tables/blocks') != True:
            os.mkdir('output/Minecraft Fabric 1.19.3/src/main/resources/data/' + mod['mod']['id'] + '/loot_tables/blocks')
        #endregion
        #endregion
    
    RunTask(Task, 'Create gradle files')
    del Task
    #endregion

    #region gradle stuff
    def Task():
        #region gradle.properties
        def SubTask():
            with open('templates/Minecraft Fabric 1.19.3/gradle.properties', 'r') as f:
                file = f.read()
                f.close()

            file = file.replace('!mod.java_pkg1', java_pkg.replace('.', '-'))
            file = file.replace('!mod.java_pkg', java_pkg)

            with open('output/Minecraft Fabric 1.19.3/gradle.properties', 'w') as f:
                f.write(file)
                f.close()
        RunTask(SubTask, 'Create gradle.properties')
        del SubTask
        #endregion
        
        shutil.copyfile('templates/Minecraft Fabric 1.19.3/settings.gradle', 'output/Minecraft Fabric 1.19.3/settings.gradle')
        shutil.copyfile('templates/Minecraft Fabric 1.19.3/build.gradle', 'output/Minecraft Fabric 1.19.3/build.gradle')
    
    RunTask(Task, 'Create gradle files')
    del Task
    #endregion

    #region fabric.mod.json
    def Task():
        global fabric_mod_json
        with open('templates/Minecraft Fabric 1.19.3/src/main/resources/fabric.mod.json', 'r') as f:
            fabric_mod_json = f.read()
            f.close()

        fabric_mod_json = fabric_mod_json.replace('!mod.id', mod['mod']['id'])
        fabric_mod_json = fabric_mod_json.replace('!mod.name', mod['mod']['name'])
        fabric_mod_json = fabric_mod_json.replace('!mod.desc', mod['mod']['desc'])
        fabric_mod_json = fabric_mod_json.replace('!mod.author', mod['mod']['author'])
        fabric_mod_json = fabric_mod_json.replace('!mod.java_pkg', java_pkg)
    
    RunTask(Task, 'Create fabric.mod.json')
    del Task
    #endregion

    #region language files
    def Task():
        global lang
        with open('templates/Minecraft Fabric 1.19.3/src/main/resources/assets/template/lang/lang.json', 'r') as f:
            lang = f.read()
            lang = lang.replace('!mod.id', mod['mod']['id'])
            lang = lang.replace('!mod.name', mod['mod']['name'])
            f.close()
    
    RunTask(Task, 'Create language files')
    del Task
    #endregion
    
    #region Blocks
    def Task():
        global item_group_block_imports
        global item_group_block_entries
        global fabric_mod_json
        global lang
        blocks = ''
        blocks_lang = ''
        item_group_block_imports = ''
        item_group_block_entries = ''

        if len(mod['elements']['blocks']) > 0:
            for i in mod['elements']['blocks']:
                if i['transparent']:
                    Log('Block ' + i['id'] + ' is transparent and transparent blocks hasn\'t been implemented yet', 'WARN')

                with open('templates/Minecraft Fabric 1.19.3/src/main/resources/assets/template/models/item/block.json', 'r') as f:
                    file = f.read()
                    f.close()

                file = file.replace('!block.id', i['id'])
                file = file.replace('!mod.id', mod['mod']['id'])

                with open('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/models/item/' + i['id'] + '.json', 'w') as f:
                    f.write(file)
                    f.close()
                
                with open('templates/Minecraft Fabric 1.19.3/src/main/resources/assets/template/blockstates/block.json', 'r') as f:
                    file = f.read()
                    f.close()

                file = file.replace('!block.id', i['id'])
                file = file.replace('!mod.id', mod['mod']['id'])

                with open('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/blockstates/' + i['id'] + '.json', 'w') as f:
                    f.write(file)
                    f.close()
                
                if i['pillar_like']:
                    # https://bugs.mojang.com/browse/MC-262870
                    if 'bottom_texture' in i:
                        with open('templates/Minecraft Fabric 1.19.3/src/main/resources/assets/template/models/block/pillar_like_dif.json', 'r') as f:
                            file = f.read()
                            f.close()

                        file = file.replace('!block.id', i['id'])
                        file = file.replace('!block.bottom_texture', i['bottom_texture'])
                        file = file.replace('!mod.id', mod['mod']['id'])

                        with open('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/models/block/' + i['id'] + '.json', 'w') as f:
                            f.write(file)
                            f.close()
                    else:
                        with open('templates/Minecraft Fabric 1.19.3/src/main/resources/assets/template/models/block/pillar_like.json', 'r') as f:
                            file = f.read()
                            f.close()

                        file = file.replace('!block.id', i['id'])
                        file = file.replace('!mod.id', mod['mod']['id'])

                        with open('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/models/block/' + i['id'] + '.json', 'w') as f:
                            f.write(file)
                            f.close()
                else:
                    with open('templates/Minecraft Fabric 1.19.3/src/main/resources/assets/template/models/block/block.json', 'r') as f:
                        file = f.read()
                        f.close()

                    file = file.replace('!block.id', i['id'])
                    file = file.replace('!mod.id', mod['mod']['id'])

                    with open('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/models/block/' + i['id'] + '.json', 'w') as f:
                        f.write(file)
                        f.close()

                with open('templates/Minecraft Fabric 1.19.3/src/main/java/package/Blocks.java', 'r') as f:
                    file = f.read()
                    f.close()

                file = file.replace('!block.id', i['id'])
                file = file.replace('!mod.id', mod['mod']['id'])
                file = file.replace('!mod.java_pkg', java_pkg)

                with open('output/Minecraft Fabric 1.19.3/src/main/java/' + java_pkg_path + '/Blocks/' + i['id'] + '.java', 'w') as f:
                    f.write(file)
                    f.close()
                
                blocks += ',\n			"' + java_pkg + '.Blocks.' + i['id'] + '"'
                blocks_lang += ',\n  "block.' + mod['mod']['id'] + '.' + i['id'] + '": "' + i['name'] + '"'
                item_group_block_imports += '\nimport ' + java_pkg + '.Blocks.' + i['id'] + ';'
                item_group_block_entries += '\n        entries.add(' + i['id'] + '.THIS_BLOCK);'

        blocks = blocks.rstrip()
        fabric_mod_json = fabric_mod_json.replace('!blocks', blocks)
        lang = lang.replace('!blocks', blocks_lang)
    
    RunTask(Task, 'Create Blocks.java')
    del Task
    #endregion
    
    #region Items
    def Task():
        global fabric_mod_json
        global lang
        global item_group_item_imports
        global item_group_item_entries
        items = ''
        items_lang = ''
        item_group_item_imports = ''
        item_group_item_entries = ''

        if len(mod['elements']['items']) > 0:
            for i in mod['elements']['items']:
                with open('templates/Minecraft Fabric 1.19.3/src/main/resources/assets/template/models/item/item.json', 'r') as f:
                    file = f.read()
                    f.close()

                file = file.replace('!item.id', i['id'])
                file = file.replace('!mod.id', mod['mod']['id'])

                with open('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/models/item/' + i['id'] + '.json', 'w') as f:
                    f.write(file)
                    f.close()

                with open('templates/Minecraft Fabric 1.19.3/src/main/java/package/Items.java', 'r') as f:
                    file = f.read()
                    f.close()

                file = file.replace('!item.id', i['id'])
                file = file.replace('!mod.id', mod['mod']['id'])
                file = file.replace('!mod.java_pkg', java_pkg)
                if i['edible']:
                    file = file.replace('!item.edible', '.food(FoodComponents.TROPICAL_FISH)')
                else:
                    file = file.replace('import net.minecraft.item.FoodComponents;\n', '')
                    file = file.replace('!item.edible', '')

                with open('output/Minecraft Fabric 1.19.3/src/main/java/' + java_pkg_path + '/Items/' + i['id'] + '.java', 'w') as f:
                    f.write(file)
                    f.close()
                
                items += ',\n			"' + java_pkg + '.Items.' + i['id'] + '"'
                items_lang += ',\n  "item.' + mod['mod']['id'] + '.' + i['id'] + '":"' + i['name'] + '"'
                item_group_item_imports += '\nimport ' + java_pkg + '.Items.' + i['id'] + ';'
                item_group_item_entries += '\n        entries.add(' + i['id'] + '.THIS_ITEM);'

        items = items.rstrip()
        fabric_mod_json = fabric_mod_json.replace('!items', items)
        lang = lang.replace('!items', items_lang)
    
    RunTask(Task, 'Create Items.java')
    del Task
    #endregion

    #region MainItemGroup.java
    def Task():
        with open('templates/Minecraft Fabric 1.19.3/src/main/java/package/MainItemGroup.java', 'r') as f:
            file = f.read()
            f.close()

        file = file.replace('!mod.id', mod['mod']['id'])
        file = file.replace('!mod.java_pkg', java_pkg)

        file = file.replace('!item.imports', item_group_item_imports)
        file = file.replace('!block.imports', item_group_block_imports)
        
        file = file.replace('!item.entries', item_group_item_entries)
        file = file.replace('!block.entries', item_group_block_entries)

        with open('output/Minecraft Fabric 1.19.3/src/main/java/' + java_pkg_path + '/MainItemGroup.java', 'w') as f:
            f.write(file)
            f.close()
    
    RunTask(Task, 'Create MainItemGroup.java')
    del Task
    #endregion

    #region crafting
    def Task():
        #region shaped
        #region shaped.lua
        def SubTask():
            with open('templates/Minecraft Fabric 1.19.3/src/main/resources/data/template/recipes/shaped.json', 'r') as f:
                template = f.read()
                f.close()

            if len(mod['recipes']['shaped']) > 0:
                for i in mod['recipes']['shaped']:
                    try:
                        path = 'output/Minecraft Fabric 1.19.3/src/main/resources/data/' + mod['mod']['id'] + '/recipes/' + i['output'].split('!mod.', 1)[1] + '.json'
                    except IndexError:
                        path = 'output/Minecraft Fabric 1.19.3/src/main/resources/data/' + mod['mod']['id'] + '/recipes/' + i['output'].split('!item_definitions.', 1)[1] + '.json'

                    with open(path, 'w') as f:
                        out = template
                        out = out.replace('!recipe.amount', str(i['amount']))

                        #region output
                        outputItem = i['output']
                        outputItem = str(outputItem)

                        if outputItem.startswith('!mod.'):
                            outputItem1 = outputItem.split('!mod.', 1)[1]
                            for j in mod['elements']['items']:
                                if outputItem1 == j['id']:
                                    out = out.replace('!recipe.output', mod['mod']['id'] + ':' + j['id'])
                                    break
                            for j in mod['elements']['blocks']:
                                if outputItem1 == j['id']:
                                    out = out.replace('!recipe.output', mod['mod']['id'] + ':' + j['id'])
                                    break
                        elif outputItem.startswith('!item_definitions.'):
                            outputItem1 = outputItem.split('!item_definitions.', 1)[1]
                            for j in mod['item_definitions']['Minetest']:
                                if j == outputItem1:
                                    out = out.replace('!recipe.output', mod['item_definitions']['Minetest'][j])
                                    break
                        #endregion

                        #region ingredients
                        #region 1
                        outputItem = i['recipe'][0][0]
                        ingredient = False
                        if outputItem.startswith('!mod.'):
                            outputItem1 = outputItem.split('!mod.', 1)[1]
                            for j in mod['elements']['items']:
                                if outputItem1 == j['id']:
                                    out = out.replace('!recipe.ingredient_1', mod['mod']['id'] + ':' + j['id'])
                                    ingredient = True
                                    break
                            for j in mod['elements']['blocks']:
                                if outputItem1 == j['id']:
                                    out = out.replace('!recipe.ingredient_1', mod['mod']['id'] + ':' + j['id'])
                                    ingredient = True
                                    break
                        elif outputItem.startswith('!item_definitions.'):
                            outputItem1 = outputItem.split('!item_definitions.', 1)[1]
                            for j in mod['item_definitions']['Minecraft Fabric 1.19.3']:
                                if j == outputItem1:
                                    out = out.replace('!recipe.ingredient_1', mod['item_definitions']['Minecraft Fabric 1.19.3'][j])
                                    ingredient = True
                                    break
                        if ingredient == False:
                            out = out.replace('\n        "A": {\n            "item": "!recipe.ingredient_1"\n        },', '')
                            out = out.replace('A', ' ')
                        #endregion
                        
                        #region 2
                        outputItem = i['recipe'][0][1]
                        ingredient = False
                        if outputItem.startswith('!mod.'):
                            outputItem1 = outputItem.split('!mod.', 1)[1]
                            for j in mod['elements']['items']:
                                if outputItem1 == j['id']:
                                    out = out.replace('!recipe.ingredient_2', mod['mod']['id'] + ':' + j['id'])
                                    ingredient = True
                                    break
                            for j in mod['elements']['blocks']:
                                if outputItem1 == j['id']:
                                    out = out.replace('!recipe.ingredient_2', mod['mod']['id'] + ':' + j['id'])
                                    ingredient = True
                                    break
                        elif outputItem.startswith('!item_definitions.'):
                            outputItem1 = outputItem.split('!item_definitions.', 1)[1]
                            for j in mod['item_definitions']['Minecraft Fabric 1.19.3']:
                                if j == outputItem1:
                                    out = out.replace('!recipe.ingredient_2', mod['item_definitions']['Minecraft Fabric 1.19.3'][j])
                                    ingredient = True
                                    break
                        if ingredient == False:
                            out = out.replace('\n        "B": {\n            "item": "!recipe.ingredient_2"\n        },', '')
                            out = out.replace('B', ' ')
                        #endregion
                        
                        #region 3
                        outputItem = i['recipe'][0][2]
                        ingredient = False
                        if outputItem.startswith('!mod.'):
                            outputItem1 = outputItem.split('!mod.', 1)[1]
                            for j in mod['elements']['items']:
                                if outputItem1 == j['id']:
                                    out = out.replace('!recipe.ingredient_3', mod['mod']['id'] + ':' + j['id'])
                                    ingredient = True
                                    break
                            for j in mod['elements']['blocks']:
                                if outputItem1 == j['id']:
                                    out = out.replace('!recipe.ingredient_3', mod['mod']['id'] + ':' + j['id'])
                                    ingredient = True
                                    break
                        elif outputItem.startswith('!item_definitions.'):
                            outputItem1 = outputItem.split('!item_definitions.', 1)[1]
                            for j in mod['item_definitions']['Minecraft Fabric 1.19.3']:
                                if j == outputItem1:
                                    out = out.replace('!recipe.ingredient_3', mod['item_definitions']['Minecraft Fabric 1.19.3'][j])
                                    ingredient = True
                                    break
                        if ingredient == False:
                            out = out.replace('\n        "C": {\n            "item": "!recipe.ingredient_3"\n        },', '')
                            out = out.replace('C', ' ')
                        #endregion
                        
                        #region 4
                        outputItem = i['recipe'][1][0]
                        ingredient = False
                        if outputItem.startswith('!mod.'):
                            outputItem1 = outputItem.split('!mod.', 1)[1]
                            for j in mod['elements']['items']:
                                if outputItem1 == j['id']:
                                    out = out.replace('!recipe.ingredient_4', mod['mod']['id'] + ':' + j['id'])
                                    ingredient = True
                                    break
                            for j in mod['elements']['blocks']:
                                if outputItem1 == j['id']:
                                    out = out.replace('!recipe.ingredient_4', mod['mod']['id'] + ':' + j['id'])
                                    ingredient = True
                                    break
                        elif outputItem.startswith('!item_definitions.'):
                            outputItem1 = outputItem.split('!item_definitions.', 1)[1]
                            for j in mod['item_definitions']['Minecraft Fabric 1.19.3']:
                                if j == outputItem1:
                                    out = out.replace('!recipe.ingredient_4', mod['item_definitions']['Minecraft Fabric 1.19.3'][j])
                                    ingredient = True
                                    break
                        if ingredient == False:
                            out = out.replace('\n        "D": {\n            "item": "!recipe.ingredient_4"\n        },', '')
                            out = out.replace('D', ' ')
                        #endregion
                        
                        #region 5
                        outputItem = i['recipe'][1][1]
                        ingredient = False
                        if outputItem.startswith('!mod.'):
                            outputItem1 = outputItem.split('!mod.', 1)[1]
                            for j in mod['elements']['items']:
                                if outputItem1 == j['id']:
                                    out = out.replace('!recipe.ingredient_5', mod['mod']['id'] + ':' + j['id'])
                                    ingredient = True
                                    break
                            for j in mod['elements']['blocks']:
                                if outputItem1 == j['id']:
                                    out = out.replace('!recipe.ingredient_5', mod['mod']['id'] + ':' + j['id'])
                                    ingredient = True
                                    break
                        elif outputItem.startswith('!item_definitions.'):
                            outputItem1 = outputItem.split('!item_definitions.', 1)[1]
                            for j in mod['item_definitions']['Minecraft Fabric 1.19.3']:
                                if j == outputItem1:
                                    out = out.replace('!recipe.ingredient_5', mod['item_definitions']['Minecraft Fabric 1.19.3'][j])
                                    ingredient = True
                                    break
                        if ingredient == False:
                            out = out.replace('\n        "E": {\n            "item": "!recipe.ingredient_5"\n        },', '')
                            out = out.replace('E', ' ')
                        #endregion
                        
                        #region 6
                        outputItem = i['recipe'][1][2]
                        ingredient = False
                        if outputItem.startswith('!mod.'):
                            outputItem1 = outputItem.split('!mod.', 1)[1]
                            for j in mod['elements']['items']:
                                if outputItem1 == j['id']:
                                    out = out.replace('!recipe.ingredient_6', mod['mod']['id'] + ':' + j['id'])
                                    ingredient = True
                                    break
                            for j in mod['elements']['blocks']:
                                if outputItem1 == j['id']:
                                    out = out.replace('!recipe.ingredient_6', mod['mod']['id'] + ':' + j['id'])
                                    ingredient = True
                                    break
                        elif outputItem.startswith('!item_definitions.'):
                            outputItem1 = outputItem.split('!item_definitions.', 1)[1]
                            for j in mod['item_definitions']['Minecraft Fabric 1.19.3']:
                                if j == outputItem1:
                                    out = out.replace('!recipe.ingredient_6', mod['item_definitions']['Minecraft Fabric 1.19.3'][j])
                                    ingredient = True
                                    break
                        if ingredient == False:
                            out = out.replace('\n        "F": {\n            "item": "!recipe.ingredient_6"\n        },', '')
                            out = out.replace('F', ' ')
                        #endregion
                        
                        #region 7
                        outputItem = i['recipe'][2][0]
                        ingredient = False
                        if outputItem.startswith('!mod.'):
                            outputItem1 = outputItem.split('!mod.', 1)[1]
                            for j in mod['elements']['items']:
                                if outputItem1 == j['id']:
                                    out = out.replace('!recipe.ingredient_7', mod['mod']['id'] + ':' + j['id'])
                                    ingredient = True
                                    break
                            for j in mod['elements']['blocks']:
                                if outputItem1 == j['id']:
                                    out = out.replace('!recipe.ingredient_7', mod['mod']['id'] + ':' + j['id'])
                                    ingredient = True
                                    break
                        elif outputItem.startswith('!item_definitions.'):
                            outputItem1 = outputItem.split('!item_definitions.', 1)[1]
                            for j in mod['item_definitions']['Minecraft Fabric 1.19.3']:
                                if j == outputItem1:
                                    out = out.replace('!recipe.ingredient_7', mod['item_definitions']['Minecraft Fabric 1.19.3'][j])
                                    ingredient = True
                                    break
                        if ingredient == False:
                            out = out.replace('\n        "G": {\n            "item": "!recipe.ingredient_7"\n        },', '')
                            out = out.replace('G', ' ')
                        #endregion
                        
                        #region 8
                        outputItem = i['recipe'][2][1]
                        ingredient = False
                        if outputItem.startswith('!mod.'):
                            outputItem1 = outputItem.split('!mod.', 1)[1]
                            for j in mod['elements']['items']:
                                if outputItem1 == j['id']:
                                    out = out.replace('!recipe.ingredient_8', mod['mod']['id'] + ':' + j['id'])
                                    ingredient = True
                                    break
                            for j in mod['elements']['blocks']:
                                if outputItem1 == j['id']:
                                    out = out.replace('!recipe.ingredient_8', mod['mod']['id'] + ':' + j['id'])
                                    ingredient = True
                                    break
                        elif outputItem.startswith('!item_definitions.'):
                            outputItem1 = outputItem.split('!item_definitions.', 1)[1]
                            for j in mod['item_definitions']['Minecraft Fabric 1.19.3']:
                                if j == outputItem1:
                                    out = out.replace('!recipe.ingredient_8', mod['item_definitions']['Minecraft Fabric 1.19.3'][j])
                                    ingredient = True
                                    break
                        if ingredient == False:
                            out = out.replace('\n        "H": {\n            "item": "!recipe.ingredient_8"\n        },', '')
                            out = out.replace('H', ' ')
                        #endregion
                        
                        #region 9
                        outputItem = i['recipe'][2][2]
                        ingredient = False
                        if outputItem.startswith('!mod.'):
                            outputItem1 = outputItem.split('!mod.', 1)[1]
                            for j in mod['elements']['items']:
                                if outputItem1 == j['id']:
                                    out = out.replace('!recipe.ingredient_9', mod['mod']['id'] + ':' + j['id'])
                                    ingredient = True
                                    break
                            for j in mod['elements']['blocks']:
                                if outputItem1 == j['id']:
                                    out = out.replace('!recipe.ingredient_9', mod['mod']['id'] + ':' + j['id'])
                                    ingredient = True
                                    break
                        elif outputItem.startswith('!item_definitions.'):
                            outputItem1 = outputItem.split('!item_definitions.', 1)[1]
                            for j in mod['item_definitions']['Minecraft Fabric 1.19.3']:
                                if j == outputItem1:
                                    out = out.replace('!recipe.ingredient_9', mod['item_definitions']['Minecraft Fabric 1.19.3'][j])
                                    ingredient = True
                                    break
                        if ingredient == False:
                            out = out.replace('\n        "I": {\n            "item": "!recipe.ingredient_9"\n        },', '')
                            out = out.replace('I', ' ')
                        #endregion
                        #endregion

                        f.write(out)
                f.close()
        
        RunTask(SubTask, 'Create shaped recipe files', True)
        del SubTask
        #endregion
    
        #region shapeless
        def SubTask():
            if len(mod['recipes']['shapeless']) > 0:
                Log('Shapeless recipes not implemented', 'WARN')

        RunTask(SubTask, 'Create shapeless recipe files', True)
        del SubTask
        #endregion

        #region smelting
        def SubTask():
            if len(mod['recipes']['smelting']) > 0:
                Log('Smelting recipes not implemented', 'WARN')

        RunTask(SubTask, 'Create smelting recipe files', True)
        del SubTask
        #endregion
    
    RunTask(Task, 'Create recipe files')
    del Task
    #endregion

    #region resources
    def Task():
        def SubTask():
            with open('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/lang/' + mod['mod']['main_lang'] + '.json', 'w') as f:
                f.write(lang)
                f.close()
        
        RunTask(SubTask, 'Write language files', True)
        del SubTask

        def SubTask():
            with open('output/Minecraft Fabric 1.19.3/src/main/resources/fabric.mod.json', 'w') as f:
                f.write(fabric_mod_json)
                f.close()

        RunTask(SubTask, 'Write fabric.mod.json', True)
        del SubTask

        def SubTask():
            if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/textures/item'):
                shutil.rmtree('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/textures/item')
            
            if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/textures/block'):
                shutil.rmtree('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/textures/block')
            
            shutil.copytree('assets/textures/items', 'output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/textures/item')
            shutil.copytree('assets/textures/blocks', 'output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/textures/block')

        RunTask(SubTask, 'Copy textures to output', True)
        del SubTask
        
        shutil.copyfile('templates/Minecraft Fabric 1.19.3/src/main/resources/assets/template/icon.png', 'output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/icon.png')
    
    RunTask(Task, 'Copy resources to output')
    del Task
    #endregion
