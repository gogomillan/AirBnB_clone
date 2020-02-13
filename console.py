#!/usr/bin/python3
"""
Create the console
"""


import cmd, sys


class HBNBCommand(cmd.Cmd):
    """ Console """
    prompt = '(hbnb) '
    file = None

if __name__ == '__main__':
    HBNBCommand().cmdloop()
