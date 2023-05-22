from functions import *
import UIFramework as UI

import generators.Minetest, generators.Minecraft_Fabric_1_19_3

def GUI():
    ui = UI.UI(800, 600, 'Not Mark\'s Mod Generator')
    ui.parse_xml('ui.xml')

    main_group = UI.ElementGroup('main')

    #region RadioButton
    radio_buttons = UI.RadioButtonGroup('ButtonGroup')

    radio_button_1 = UI.RadioButton('main:radio_button/1', 10, 110, button_group=radio_buttons, group=main_group)
    radio_button_2 = UI.RadioButton('main:radio_button/2', 10, 140, button_group=radio_buttons, group=main_group)
    radio_button_3 = UI.RadioButton('main:radio_button/3', 10, 170, button_group=radio_buttons, group=main_group)
    #endregion

    def ReloadButtonClickHandler():
        ui.clear_elements()
        ui.clear_groups()
        ui.parse_xml('ui.xml')

        ui.add_element(reload_button)

    reload_button = UI.Button('main:button/reload', 0, 570, 90, 30, text='Reload', click_handler=ReloadButtonClickHandler, color=(200,200,200), text_color=(0,0,0))
    ui.add_element(reload_button)

    ui.run()
