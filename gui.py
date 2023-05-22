from functions import *
import UIFramework as UI

import generators.Minetest, generators.Minecraft_Fabric_1_19_3

def GUI():
    ui = UI.UI(800, 600, 'Not Mark\'s Mod Generator')
    ui.parse_xml('ui.xml')

    main_group = UI.ElementGroup('main')
    
    image = UI.Image('main:image/', 150, 250, 'assets/textures/blocks/cobble_1.png', scale=180, group=main_group)
    image_peanut_butter = UI.Image('main:image/peanut_butter', 430, 250, 'assets/textures/items/peanut_butter_1.png', scale=180, group=main_group)

    #region RadioButton
    radio_buttons = UI.RadioButtonGroup('ButtonGroup')

    radio_button_1 = UI.RadioButton('main:radio_button/1', 10, 110, button_group=radio_buttons, group=main_group)
    radio_button_2 = UI.RadioButton('main:radio_button/2', 10, 140, button_group=radio_buttons, group=main_group)
    radio_button_3 = UI.RadioButton('main:radio_button/3', 10, 170, button_group=radio_buttons, group=main_group)
    #endregion

    def DoSomethingButtonClickHandler():
        element = ui.get_element_by_name('main:image/peanut_butter')
        element.SetPosition(element.rect.x + 10, element.rect.y + 10)

    do_something_button = UI.Button('main:button/do_something', 680, 570, 120, 30, text='Do something', click_handler=DoSomethingButtonClickHandler)
    ui.add_element(do_something_button)

    def DoSomethingElseButtonClickHandler():
        if main_group.enabled:
            main_group.disable()
        else:
            main_group.enable()

    do_something_else_button = UI.Button('main:button/do_something_else', 540, 570, 140, 30, text='Do something else', click_handler=DoSomethingElseButtonClickHandler)
    ui.add_element(do_something_else_button)

    def ReloadButtonClickHandler():
        ui.clear_elements()
        ui.clear_groups()
        ui.parse_xml('ui.xml')

        ui.add_element(do_something_button)
        ui.add_element(do_something_else_button)
        ui.add_element(reload_button)

    reload_button = UI.Button('main:button/reload', 0, 570, 90, 30, text='Reload', click_handler=ReloadButtonClickHandler)
    ui.add_element(reload_button)

    ui.run()
