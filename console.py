#!/usr/bin/python3
"""
Create the console
"""

import models
import cmd
from models import storage
import sys
from models.base_model import BaseModel
from datetime import datetime
import shlex

classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """ Console """
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Function that do EOF"""
        return True

    def do_quit(self, line):
        """Function that close the program"""
        return True

    def do_create(self, arg):
        """Create a new instace of basemodel"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            instance = classes[args[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """Prints ths string representation of an
instace based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist**")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or
not on the class name"""
        args = shlex.split(arg)
        lt_obj = []
        if len(args) == 0:
            for value in models.storage.all().values():
                lt_obj.append(str(value))
            print("[", end="")
            print(", ".join(lt_obj), end="")
            print("]")
        elif args[0] in classes:
            for key in models.storage.all():
                if args[0] in key:
                    lt_obj.append(str(models.storage.all()[key]))
            print("[", end="")
            print(", ".join(lt_obj), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attributes"""
        # args = shlex.split(arg)
        # if len(args) == 0:
        #   print("** class name missing **")
        # elif args[0] in classes:
        #   if len(args) > 1:
        #      k = args[0] + "." + args[1]

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt"""
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
