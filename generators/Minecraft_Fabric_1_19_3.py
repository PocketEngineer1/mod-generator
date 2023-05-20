import os, shutil

def Generate(mod, args):
    #region Directories
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

    if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources/data/' + mod['mod']['id'] + '/loot_tables') != True:
        os.mkdir('output/Minecraft Fabric 1.19.3/src/main/resources/data/' + mod['mod']['id'] + '/loot_tables')

    if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources/data/' + mod['mod']['id'] + '/loot_tables/blocks') != True:
        os.mkdir('output/Minecraft Fabric 1.19.3/src/main/resources/data/' + mod['mod']['id'] + '/loot_tables/blocks')
    #endregion
    #endregion

    #region gradle stuff
    #region gradle.properties
    with open('templates/Minecraft Fabric 1.19.3/gradle.properties', 'r') as f:
        file = f.read()
        f.close()

    file = file.replace('!mod.java_pkg1', java_pkg.replace('.', '-'))
    file = file.replace('!mod.java_pkg', java_pkg)

    with open('output/Minecraft Fabric 1.19.3/gradle.properties', 'w') as f:
        f.write(file)
        f.close()

    del file
    #endregion
    
    shutil.copyfile('templates/Minecraft Fabric 1.19.3/settings.gradle', 'output/Minecraft Fabric 1.19.3/settings.gradle')
    shutil.copyfile('templates/Minecraft Fabric 1.19.3/build.gradle', 'output/Minecraft Fabric 1.19.3/build.gradle')
    #endregion

    #region fabric.mod.json
    with open('templates/Minecraft Fabric 1.19.3/src/main/resources/fabric.mod.json', 'r') as f:
        fabric_mod_json = f.read()
        f.close()

    fabric_mod_json = fabric_mod_json.replace('!mod.id', mod['mod']['id'])
    fabric_mod_json = fabric_mod_json.replace('!mod.name', mod['mod']['name'])
    fabric_mod_json = fabric_mod_json.replace('!mod.desc', mod['mod']['desc'])
    fabric_mod_json = fabric_mod_json.replace('!mod.author', mod['mod']['author'])
    fabric_mod_json = fabric_mod_json.replace('!mod.java_pkg', java_pkg)
    #endregion

    #region MainItemGroup.java
    with open('templates/Minecraft Fabric 1.19.3/src/main/java/package/MainItemGroup.java', 'r') as f:
        file = f.read()
        f.close()

    file = file.replace('!mod.id', mod['mod']['id'])
    file = file.replace('!mod.java_pkg', java_pkg)
    file += "\n\n"

    with open('output/Minecraft Fabric 1.19.3/src/main/java/' + java_pkg_path + '/MainItemGroup.java', 'w') as f:
        f.write(file)
        f.close()
    #endregion
    
    #region Blocks.java
    blocks = ''

    if len(mod['elements']['blocks']) > 0:
        for i in mod['elements']['blocks']:
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

    blocks = blocks.rstrip()
    fabric_mod_json = fabric_mod_json.replace('!blocks', blocks)
    #endregion
    
    #region Items.java
    items = ''

    if len(mod['elements']['items']) > 0:
        for i in mod['elements']['items']:
            with open('templates/Minecraft Fabric 1.19.3/src/main/java/package/Items.java', 'r') as f:
                file = f.read()
                f.close()

            file = file.replace('!item.id', i['id'])
            file = file.replace('!mod.id', mod['mod']['id'])
            file = file.replace('!mod.java_pkg', java_pkg)

            with open('output/Minecraft Fabric 1.19.3/src/main/java/' + java_pkg_path + '/Items/' + i['id'] + '.java', 'w') as f:
                f.write(file)
                f.close()
            
            items += ',\n			"' + java_pkg + '.Items.' + i['id'] + '"'

    items = items.rstrip()
    fabric_mod_json = fabric_mod_json.replace('!items', items)
    #endregion

    #region assets
    with open('output/Minecraft Fabric 1.19.3/src/main/resources/fabric.mod.json', 'w') as f:
        f.write(fabric_mod_json)
        f.close()

    if os.path.exists('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/textures'):
        shutil.rmtree('output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/textures')
    shutil.copytree('assets/textures', 'output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/textures')
    
    shutil.copyfile('templates/Minecraft Fabric 1.19.3/src/main/resources/assets/template/icon.png', 'output/Minecraft Fabric 1.19.3/src/main/resources/assets/' + mod['mod']['id'] + '/icon.png')
    #endregion
