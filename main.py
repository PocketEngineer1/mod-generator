import os, json5

import generators.Minetest

def Main():
    global modData

    if os.path.exists('output') != True:
        os.mkdir('output')

    with open('./mod.json5', 'r') as f:
        modData = json5.load(f)

    generators.Minetest.Generate(modData)

if __name__ == '__main__' or 'main':
    Main()
