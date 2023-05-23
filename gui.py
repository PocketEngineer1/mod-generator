import json5

from functions import *
import UIFramework as UI

import generators.Minetest, generators.Minecraft_Fabric_1_19_3

def GUI(args):
    ui = UI.UI(800, 600, 'Not Mark\'s Mod Generator')
    ui.parse_xml('ui.xml')

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

    ui.get_element_by_name('main:Button/generate_minetest_mod').click_handler = Generate_Minetest_Mod
    ui.get_element_by_name('main:Button/generate_minecraft_fabric_1_19_3_mod').click_handler = Generate_Minecraft_Fabric_1_19_3_Mod

    #region RadioButton
    # radio_buttons = UI.RadioButtonGroup('ButtonGroup')

    # radio_button_1 = UI.RadioButton('main:radio_button/1', 10, 110, button_group=radio_buttons, group=main_group)
    # radio_button_2 = UI.RadioButton('main:radio_button/2', 10, 140, button_group=radio_buttons, group=main_group)
    # radio_button_3 = UI.RadioButton('main:radio_button/3', 10, 170, button_group=radio_buttons, group=main_group)
    #endregion

    def ReloadButtonClickHandler():
        ui.clear_elements()
        ui.clear_groups()
        ui.parse_xml('ui.xml')

        ui.get_element_by_name('main:Button/generate_minetest_mod').click_handeler = Generate_Minetest_Mod
        ui.get_element_by_name('main:Button/generate_minecraft_fabric_1_19_3_mod').click_handeler = Generate_Minecraft_Fabric_1_19_3_Mod

        ui.add_element(reload_button)

    reload_button = UI.Button('main:button/reload', 0, 570, 90, 30, text='Reload', click_handler=ReloadButtonClickHandler, color=(200,200,200), text_color=(0,0,0))
    ui.add_element(reload_button)

    ui.run()
