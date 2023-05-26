import json5

from functions import *
import UIFramework as UI

import generators.Minetest, generators.Minecraft_Fabric_1_19_3

def GUI(args):
    ui = UI.UI(800, 600, 'Not Mark\'s Mod Generator')

    #region global Group
    global_group = UI.ElementGroup('global')

    #region Click handelers
    #endregion

    title_text = UI.Text('title_text', 40, 10, 'Not Mark\'s Mod Generator', font_size=80, group=global_group)

    ui.add_element(title_text)
    
    ui.add_group(global_group)
    #endregion

    #region mod_generation Group
    mod_generation_group = UI.ElementGroup('mod_generation')

    #region Click handelers
    def generate_mod():
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

    generate_minetest_mod = UI.Checkbox('generate_minetest_mod', 10, 110, label='Minetest', group=mod_generation_group)
    generate_minecraft_fabric_1_19_3_mod = UI.Checkbox('generate_minecraft_fabric_1_19_3_mod', 10, 140, label='Minecraft Fabric 1.19.3', group=mod_generation_group)
    generate_button = UI.Button('generate_mods', 0, 570, 800, 30, click_handler=generate_mod, text='Generate Mods', group=mod_generation_group)

    ui.add_element(generate_button)
    ui.add_element(generate_minetest_mod)
    ui.add_element(generate_minecraft_fabric_1_19_3_mod)
    
    ui.add_group(mod_generation_group)
    #endregion

    #region mod_testing Group
    mod_testing_group = UI.ElementGroup('mod_testing')

    #region Click handelers
    def test_mod():
        if args.mod == None:
            modDef = './mod.json5'
        else:
            modDef = args.mod

        with open(modDef, 'r') as f:
            modData = json5.load(f)
    #endregion

    radio_button_group = UI.RadioButtonGroup()

    test_minetest_mod = UI.RadioButton('test_minetest_mod', 10, 110, label='Minetest', button_group=radio_button_group, group=mod_testing_group)
    test_minecraft_fabric_1_19_3_mod = UI.RadioButton('test_minecraft_fabric_1_19_3_mod', 10, 140, label='Minecraft Fabric 1.19.3', button_group=radio_button_group, group=mod_testing_group)

    test_button = UI.Button('test_mod', 0, 570, 800, 30, click_handler=test_mod, text='Test Mod', group=mod_testing_group)

    ui.add_element(test_button)
    ui.add_element(test_minetest_mod)
    ui.add_element(test_minecraft_fabric_1_19_3_mod)

    mod_testing_group.disable()
    ui.add_group(mod_testing_group)
    #endregion

    #region tabs
    tabs = UI.TabGroup()
    tabs.add_group(mod_generation_group)
    tabs.add_group(mod_testing_group)
    mod_generation_button = UI.Tab('mod_generation_button', 0, 70, 400, 30, tab_group=tabs, group=mod_generation_group, text='Mod Generation', enabled=False, global_group=global_group)
    mod_testing_button = UI.Tab('mod_testing_button', 400, 70, 400, 30, tab_group=tabs, group=mod_testing_group, text='Mod Testing', global_group=global_group)
    ui.add_element(mod_generation_button)
    ui.add_element(mod_testing_button)
    #endregion

    ui.run()
