#!/usr/bin/python3
"""
Create the console
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """ Console """
    prompt = '(hbnb) '
    file = None

    def do_EOF(self, line):
        """Function that do EOF"""
        return True

    def do_quit(self, line):
        """Function that close the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt"""
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
