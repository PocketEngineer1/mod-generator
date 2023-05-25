import json5

from functions import *
import UIFramework as UI

import generators.Minetest, generators.Minecraft_Fabric_1_19_3

def GUI(args):
    ui = UI.UI(800, 600, 'Not Mark\'s Mod Generator')

    main_group = UI.ElementGroup('main')

    #region Click handelers
    def Generate_Mod():
        if args.mod == None:
            modDef = './mod.json5'
        else:
            modDef = args.mod

        with open(modDef, 'r') as f:
            modData = json5.load(f)
        
        if generate_minetest_mod.checked:
            Log('Started task \'Create Minetest mod\'', 'INFO')
            generators.Minetest.Generate(modData, args)
            Log('Completed task \'Create Minetest mod\'', 'INFO')

        if generate_minecraft_fabric_1_19_3_mod.checked:
            Log('Started task \'Create Minecraft Fabric 1.19.3 mod\'', 'INFO')
            generators.Minecraft_Fabric_1_19_3.Generate(modData, args)
            Log('Completed task \'Create Minecraft Fabric 1.19.3 mod\'', 'INFO')
    #endregion

    title_text = UI.Text('title_text', 40, 10, 'Not Mark\'s Mod Generator', font_size=80, group=main_group)
    header_body_seperator = UI.Line('header_body_seperator', (0, 70), (800, 70), thickness=2, group=main_group)
    generate_minetest_mod = UI.Checkbox('generate_minetest_mod', 10, 85, label='Minetest', group=main_group)
    generate_minecraft_fabric_1_19_3_mod = UI.Checkbox('generate_minecraft_fabric_1_19_3_mod', 10, 115, label='Minecraft Fabric 1.19.3', group=main_group)
    generate_button = UI.Button('generate_mods', 0, 570, 800, 30, click_handler=Generate_Mod, text='Generate Mods', group=main_group)

    ui.add_element(title_text)
    ui.add_element(header_body_seperator)
    ui.add_element(generate_button)
    ui.add_element(generate_minetest_mod)
    ui.add_element(generate_minecraft_fabric_1_19_3_mod)
    
    ui.add_group(main_group)

    ui.run()
