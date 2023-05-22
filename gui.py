from functions import *
import UIFramework as UI

def GUI():
    ui = UI.UI(800, 600, 'Not Mark\'s Mod Generator')

    main_group = UI.ElementGroup('main')
    ui.add_group(main_group)

    text = UI.Text('main:text/', 10, 5, 'Hello World!', group=main_group)
    rectangle = UI.Rectangle('main:rectangle/', 140, 20, 200, 200, (0, 0, 0), group=main_group)
    circle = UI.Circle('main:circle/', 160, 40, 80, (155, 155, 155), group=main_group)
    ellipse = UI.Ellipse('main:ellipse/', 160, 40, 160, 80, (55, 55, 55), group=main_group)
    line = UI.Line('main:line/', (460, 40), (540, 120), group=main_group)
    button = UI.Button('main:button/', 10, 30, 120, 30, text='Hello?', group=main_group)
    text_input = UI.TextInput('main:text_input/', 10, 70, 120, 30, placeholder='Hello?', group=main_group)
    checkbox = UI.Checkbox('main:checkbox/', 10, 200, group=main_group)
    image = UI.Image('main:image/', 150, 250, 'assets/textures/blocks/cobble_1.png', scale=180, group=main_group)
    image_peanut_butter = UI.Image('main:image/peanut_butter', 430, 250, 'assets/textures/items/peanut_butter_1.png', scale=180, group=main_group)

    ui.add_element(text)
    ui.add_element(rectangle)
    ui.add_element(circle)
    ui.add_element(ellipse)
    ui.add_element(line)
    ui.add_element(button)
    ui.add_element(text_input)
    ui.add_element(checkbox)
    ui.add_element(image)
    ui.add_element(image_peanut_butter)

    #region RadioButton
    radio_buttons = UI.RadioButtonGroup()

    radio_button_1 = UI.RadioButton('main:radio_button/1', 10, 110, button_group=radio_buttons, group=main_group)
    radio_button_2 = UI.RadioButton('main:radio_button/2', 10, 140, button_group=radio_buttons, group=main_group)
    radio_button_3 = UI.RadioButton('main:radio_button/3', 10, 170, button_group=radio_buttons, group=main_group)

    ui.add_element(radio_button_1)
    ui.add_element(radio_button_2)
    ui.add_element(radio_button_3)
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

    do_something_button_else = UI.Button('main:button/do_something_else', 540, 570, 140, 30, text='Do something else', click_handler=DoSomethingElseButtonClickHandler)
    ui.add_element(do_something_button_else)

    ui.run()
