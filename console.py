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

    def do_create(self, line):
        """Creates a new instace of basemodel"""
        print("this is a funny method")

    def do_show(self, line):
        """Prints ths string representation of an
instace based on the class and id"""
        print("this is a funny method")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        print("this is a funny method")

    def do_all(self, line):
        """Prints all string representation of all instances based or
not on the class name"""
        print("this is a funny method")

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
or updating attributes"""
        print("this is a funny method")

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt"""
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
