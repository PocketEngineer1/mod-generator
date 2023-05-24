import json5

from functions import *
import UIFramework as UI

import generators.Minetest, generators.Minecraft_Fabric_1_19_3

def GUI(args):
    ui = UI.UI(800, 600, 'Not Mark\'s Mod Generator')

    main_group = UI.ElementGroup('main')

    #region functions
    def Generate_Minetest_Mod():
        if args.mod == None:
            modDef = './mod.json5'
        else:
            modDef = args.mod

        with open(modDef, 'r') as f:
            modData = json5.load(f)

        Log('Started task \'Create Minetest mod\'', 'INFO')
        generators.Minetest.Generate(modData, args)
        Log('Completed task \'Create Minetest mod\'', 'INFO')

    def Generate_Minecraft_Fabric_1_19_3_Mod():
        if args.mod == None:
            modDef = './mod.json5'
        else:
            modDef = args.mod

        with open(modDef, 'r') as f:
            modData = json5.load(f)

        Log('Started task \'Create Minecraft Fabric 1.19.3 mod\'', 'INFO')
        generators.Minecraft_Fabric_1_19_3.Generate(modData, args)
        Log('Completed task \'Create Minecraft Fabric 1.19.3 mod\'', 'INFO')
    #endregion

    title_text = UI.Text('title_text', 40, 10, 'Not Mark\'s Mod Generator', font_size=80, group=main_group)
    header_body_seperator = UI.Line('header_body_seperator', (0, 70), (800, 70), thickness=2, group=main_group)
    generate_minetest_mod_button = UI.Button('generate_minetest_mod_button', 0, 80, 800, 30, click_handler=Generate_Minetest_Mod, text='Generate Minetest Mod', group=main_group)
    generate_minecraft_fabric_1_19_3_mod = UI.Button('generate_minecraft_fabric_1_19_3_mod', 0, 120, 800, 30, click_handler=Generate_Minecraft_Fabric_1_19_3_Mod, text='Generate Minecraft Fabric 1.19.3 Mod', group=main_group)

    ui.add_element(title_text)
    ui.add_element(header_body_seperator)
    ui.add_element(generate_minetest_mod_button)
    ui.add_element(generate_minecraft_fabric_1_19_3_mod)
    
    ui.add_group(main_group)

    ui.run()
