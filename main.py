import os, json5, argparse, sys, threading

import generators.Minetest, generators.Minecraft_Fabric_1_19_3
from functions import *
import UIFramework as UI

#region args
parser = argparse.ArgumentParser(prog='ModGenerator', description='What the program does', epilog='Text at the bottom of help')
parser.add_argument('-g', '--game', help='Specify the game to generate a mod for')
parser.add_argument('-r', '--run', action='store_true', help='Specify wether to run the game client')
parser.add_argument('-m', '--mod', help='Specify the path to the mod definition JSON5 file')
parser.add_argument('--gui', action='store_true', help='Start with the GUI')
parser.add_argument('--game-list', action='store_true', help='Lists the available games')
parser.add_argument('--run-command', help='Specify the command used to run the game client')
parser.add_argument('--create-modDef', action='store_true', help='Creates a mod definition file')
args = parser.parse_args()
#endregion

def Main():
    #region args.create_mod
    if args.create_modDef:
        if os.path.exists('./mod.json5'):
            sys.exit('\'mod.json5\' already exists!')

        with open('./mod.json5', 'w') as f:
            f.write('''{
    mod: {
        name: 'Example Mod',
        id: 'example_mod',
        desc: 'Describe your mod',
        author: 'Me!',

        java_package: [
            'example',
            'mod',
        ],
    },
    
    item_definitions: {
        Minetest: {
        },

        'Minecraft Fabric 1.19.3': {
        }
    },

    recipes: {
        shaped: [
            {
                output: '!mod.example_block',
                amount: 1,
                recipe: [
                    ['!mod.example_item', '!mod.example_item', '!mod.example_item'],
                    ['!mod.example_item', '!mod.example_item', '!mod.example_item'],
                    ['!mod.example_item', '!mod.example_item', '!mod.example_item']
                ]
            },
        ],

        shapeless: [
        ],

        smelting: [
            {
                output: '!mod.example_food',
                input: '!mod.example_item'
            },
        ],
    },

    elements: {
        items: [
            {
                id: 'example_item',
                name: 'Example Item',
            },
        ],

        blocks: [
            {
                id: 'example_block',
                name: 'Example Block',
            },
        ],

        food: [
            {
                id: 'example_example',
                name: 'Example Food',
            },
        ],
    },
}''')
            f.close()
        sys.exit()
    #endregion

    #region
    with open('mod-generator.log', 'w') as f:
        f.write('')

    if os.path.exists('output') != True:
        os.mkdir('output')

    if args.mod == None:
        modDef = './mod.json5'
    else:
        modDef = args.mod

    with open(modDef, 'r') as f:
        modData = json5.load(f)
    #endregion

    if args.gui:
        def GUI():
            ui = UI.UI(800, 600, 'Not Mark\'s Mod Generator')

            main_group = UI.ElementGroup()

            text = UI.Text('text', 10, 5, 'Hello World!', group=main_group)
            rectangle = UI.Rectangle('rectangle', 140, 20, 200, 200, (0, 0, 0), group=main_group)
            circle = UI.Circle('circle', 160, 40, 80, (155, 155, 155), group=main_group)
            ellipse = UI.Ellipse('ellipse', 160, 40, 160, 80, (55, 55, 55), group=main_group)
            line = UI.Line('line', (460, 40), (540, 120), group=main_group)
            button = UI.Button('button', 10, 30, 120, 30, text='Hello?', group=main_group)
            text_input = UI.TextInput('text_input', 10, 70, 120, 30, placeholder='Hello?', group=main_group)
            checkbox = UI.Checkbox('checkbox', 10, 200, group=main_group)
            image = UI.Image('image', 150, 250, 'assets/textures/blocks/cobble_1.png', scale=180, group=main_group)
            image_peanut_butter = UI.Image('image/peanut_butter', 430, 250, 'assets/textures/items/peanut_butter_1.png', scale=180, group=main_group)

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

            radio_button_1 = UI.RadioButton('radio_button_1', 10, 110, button_group=radio_buttons, group=main_group)
            radio_button_2 = UI.RadioButton('radio_button_2', 10, 140, button_group=radio_buttons, group=main_group)
            radio_button_3 = UI.RadioButton('radio_button_3', 10, 170, button_group=radio_buttons, group=main_group)

            ui.add_element(radio_button_1)
            ui.add_element(radio_button_2)
            ui.add_element(radio_button_3)
            #endregion

            def DoSomethingButtonClickHandler():
                if main_group.enabled:
                    main_group.disable()
                else:
                    main_group.enable()

            do_something_button = UI.Button('do_something_button', 680, 570, 120, 30, text='Do something', click_handler=DoSomethingButtonClickHandler)
            ui.add_element(do_something_button)

            ui.run()

        ui_thread = threading.Thread(target=GUI)
        ui_thread.start()
        ui_thread.join()
    else:
        if args.game == 'Minetest':
            Log('Started task \'Create Minetest mod\'', 'INFO')
            generators.Minetest.Generate(modData, args)
            Log('Completed task \'Create Minetest mod\'', 'INFO')
        elif args.game == 'Minecraft Fabric 1.19.3':
            Log('Started task \'Create Minecraft Fabric 1.19.3 mod\'', 'INFO')
            generators.Minecraft_Fabric_1_19_3.Generate(modData, args)
            Log('Completed task \'Create Minecraft Fabric 1.19.3 mod\'', 'INFO')
        else:
            Log('Started task \'Create Minetest mod\'', 'INFO')
            generators.Minetest.Generate(modData, args)
            Log('Completed task \'Create Minetest mod\'', 'INFO')
            
            Log('Started task \'Create Minecraft Fabric 1.19.3 mod\'', 'INFO')
            generators.Minecraft_Fabric_1_19_3.Generate(modData, args)
            Log('Completed task \'Create Minecraft Fabric 1.19.3 mod\'', 'INFO')

if __name__ == '__main__' or 'main':
    Main()
