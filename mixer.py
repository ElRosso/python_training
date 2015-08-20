import sys
import os
import hashlib
import ast
import argparse
from time import *


class shuffler: #CodeStyle, code duplication (rename, restore)
                #private opinion: we do not use any specific data set, it will be better to rewrite w/o "Class logic"
    
    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
        mp3s = [] #inden
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3': #file[-4:]
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3, path + '/' + hashname) #( / ==> . ))
        f = open(output, 'r') #indent, unclose
        f.write(str(self.map)) #indent, read -only

    def restore(self, dirname, restore_path):
        with open(dirname, '+') as f: #indent block, unknown name filename
            self.map = ast.literal_eval(f.read())
            mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3': #file[-4:]
                    mp3s.append({root, file})#type(mp3s)==list
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]) #( ))
        os.remove(restore_path)

    # indent, codestyle, dangerous 'seed' - it will be initialized only first call...
    # private opinion: this function should be better defined outside of class
    def generateName(self, seed=time()):
        return hashlib.md5(str(seed)).hexdigest() #indent


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")#should be help='restore help'
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args


#non-python style BEGIN
def main():
    args = parse_arguments()
    print args
    Shuffler = shuffler() #codestyle
    if args.subcommand == 'rename':
          if args.output: #incorrect condition ==> if NOT args.output
                Shuffler.rename(args.dirname, 'restore.info') #error if un-exist folders
          else:
                Shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit() # ???


main()
#non-python style END :))