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

            text = UI.Text(10, 5, 'Hello World!')
            rectangle = UI.Rectangle(140, 20, 200, 200, (0, 0, 0))
            circle = UI.Circle(200, 80, 200, 200, 100, (155, 155, 155))
            button = UI.Button(10, 30, 120, 30, text='Hello?')
            text_input = UI.TextInput(10, 70, 120, 30, placeholder='Hello?')
            checkbox = UI.Checkbox(10, 200)

            ui.add_element(text)
            ui.add_element(rectangle)
            ui.add_element(circle)
            ui.add_element(button)
            ui.add_element(text_input)
            ui.add_element(checkbox)

            #region RadioButton
            radio_buttons = UI.RadioButtonGroup()

            radio_button_1 = UI.RadioButton(10, 110, group=radio_buttons)
            radio_button_2 = UI.RadioButton(10, 140, group=radio_buttons)
            radio_button_3 = UI.RadioButton(10, 170, group=radio_buttons)

            ui.add_element(radio_button_1)
            ui.add_element(radio_button_2)
            ui.add_element(radio_button_3)
            #endregion

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
