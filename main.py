import os, json5, argparse, sys, threading, shutil, subprocess

import generators.Minetest, generators.Minecraft_Fabric_1_19_3
from functions import *

#region args
parser = argparse.ArgumentParser(prog='ModGenerator', description='What the program does', epilog='Text at the bottom of help')
parser.add_argument('-g', '--game', help='Specify the game to generate a mod for')
parser.add_argument('-r', '--run', action='store_true', help='Specify wether to run the game client')
parser.add_argument('--regenerate', action='store_true', help='Specify to regenerate the code before running the client (Must be used with --run)')
parser.add_argument('-m', '--mod', help='Specify the path to the mod definition JSON5 file')
parser.add_argument('--run-def', help='Specify the path to the run definition JSON5 file')
parser.add_argument('--gui', action='store_true', help='Start with the GUI')
# parser.add_argument('--game-list', action='store_true', help='Lists the available games')
args = parser.parse_args()
#endregion

def Main():
    #region args.run
    if args.run:
        if args.mod == None:
            runDef = './run.json5'
        else:
            runDef = args.run_def

        with open(runDef, 'r') as f:
            runDef = json5.load(f)
        
        if args.game == None:
            sys.exit('Please specify a game to run')
        elif args.game == 'Minetest':
            if args.regenerate:
                if args.mod == None:
                    modDef = './mod.json5'
                else:
                    modDef = args.mod

                with open(modDef, 'r') as f:
                    modData = json5.load(f)
            
                Log('Started task \'Generate Minetest mod\'', 'INFO')
                generators.Minetest.Generate(modData, args)
                Log('Completed task \'Generate Minetest mod\'', 'INFO')
            
            if os.path.exists(runDef['Minetest']['Were to copy generated source to']):
                shutil.rmtree(runDef['Minetest']['Were to copy generated source to'])
            shutil.copytree('output/Minetest', runDef['Minetest']['Were to copy generated source to'])
            subprocess.Popen(runDef['Minetest']['What command to execute to test the mod'], shell=True)
        
        elif args.game == 'Minecraft Fabric 1.19.3':
            if args.regenerate:
                if args.mod == None:
                    modDef = './mod.json5'
                else:
                    modDef = args.mod

                with open(modDef, 'r') as f:
                    modData = json5.load(f)
                
                Log('Started task \'Generate Minecraft Fabric 1.19.3 mod\'', 'INFO')
                generators.Minecraft_Fabric_1_19_3.Generate(modData, args)
                Log('Completed task \'Generate Minecraft Fabric 1.19.3 mod\'', 'INFO')
            
            if os.path.exists(runDef['Minecraft Fabric 1.19.3']['Were to copy generated source to']):
                shutil.rmtree(runDef['Minecraft Fabric 1.19.3']['Were to copy generated source to'])
            shutil.copytree('output/Minecraft Fabric 1.19.3/src', runDef['Minecraft Fabric 1.19.3']['Were to copy generated source to'])
            subprocess.Popen(runDef['Minecraft Fabric 1.19.3']['What command to execute to test the mod'], shell=True)
        else:
            sys.exit('Unknown game')

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
        from gui import GUI
        ui_thread = threading.Thread(target=GUI, args=[args])
        ui_thread.start()
        ui_thread.join()
    else:
        if args.game == 'Minetest':
            Log('Started task \'Generate Minetest mod\'', 'INFO')
            generators.Minetest.Generate(modData, args)
            Log('Completed task \'Generate Minetest mod\'', 'INFO')
        elif args.game == 'Minecraft Fabric 1.19.3':
            Log('Started task \'Generate Minecraft Fabric 1.19.3 mod\'', 'INFO')
            generators.Minecraft_Fabric_1_19_3.Generate(modData, args)
            Log('Completed task \'Generate Minecraft Fabric 1.19.3 mod\'', 'INFO')
        else:
            Log('Started task \'Generate Minetest mod\'', 'INFO')
            generators.Minetest.Generate(modData, args)
            Log('Completed task \'Generate Minetest mod\'', 'INFO')
            
            Log('Started task \'Generate Minecraft Fabric 1.19.3 mod\'', 'INFO')
            generators.Minecraft_Fabric_1_19_3.Generate(modData, args)
            Log('Completed task \'Generate Minecraft Fabric 1.19.3 mod\'', 'INFO')

if __name__ == '__main__' or 'main':
    Main()
