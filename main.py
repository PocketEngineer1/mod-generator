import os, json5, argparse, sys

import generators.Minetest

parser = argparse.ArgumentParser(prog='ModGenerator', description='What the program does', epilog='Text at the bottom of help')
parser.add_argument('-s', '--silence', action='store_true')
parser.add_argument('-g', '--game', help='Specify the game to generate a mod for')
parser.add_argument('-r', '--run', action='store_true', help='Specify wether to run the game client')
parser.add_argument('-m', '--mod', help='Specify the path to the mod definition JSON5 file')
parser.add_argument('--game-list', action='store_true', help='Lists the available games')
parser.add_argument('--run-command', help='Specify the command used to run the game client')
parser.add_argument('--create-mod', action='store_true', help='Creates a mod definition file')
args = parser.parse_args()

def Main():
    print(args)

    if os.path.exists('output') != True:
        os.mkdir('output')

    if args.mod == None:
        modDef = './mod.json5'
    else:
        modDef = args.mod

    with open(modDef, 'r') as f:
        modData = json5.load(f)

    generators.Minetest.Generate(modData, args)

if __name__ == '__main__' or 'main':
    #region args.create_mod
    if args.create_mod:
        if os.path.exists('./mod.json5'):
            sys.exit('\'mod.json5\' already exists!')

        with open('./mod.json5', 'w') as f:
            f.write('''{
    mod: {
        name: 'Example Mod',
        id: 'example_mod',
        desc: 'Describe your mod',
        author: 'Me!',
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
    },
}''')
            f.close()
        sys.exit()
    #endregion

    Main()
