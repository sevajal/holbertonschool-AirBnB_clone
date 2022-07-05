#!/usr/bin/python3
"""
contains the entry point of
the command interpreter
"""
import cmd
import re

from urllib3 import Retry
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ class command interpreter """
    prompt = '(hbnb) '

    def split_args(self, line):
        """ Split arguments by spaces """
        list = []
        for arg in line.split(" "):
            list.append(arg)
        return list

    def do_EOF(self, arg):
        'EOF command to exit the program'
        print ("")
        return True

    def do_quit(self, arg):
        'Quit command to exit the program'
        print ("")
        return True

    def do_create(self, arg):
        'Create command creates new instance'
        if not arg:
            print("** class name missing **")
            return
        if arg != "BaseModel":
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        new_instance.save()
        storage.reload()
        print(new_instance.id)

    def do_show(self, arg):
        'Prints the string representation of an instance(class/id)'
        args = self.split_args(arg)
        if not args[0]:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        dir_class = storage.all()
        for key, value in dir_class.items():
            if key == args[0] + '.' + args[1]:
                print(BaseModel(**value))
                return
        print("** no instance found **")

    def do_destroy(self, arg):
        'command to destroy an instance'
        args = self.split_args(arg)
        if not args[0]:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        dir_class = storage.all()
        for key in dir_class.keys():
            if key == args[0] + '.' + args[1]:
                dir_class.pop(key)
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, arg):
        'command to show all instances'
        if not arg or arg == "BaseModel":
            string_all = []
            dir_class = storage.all()
            for key, value in dir_class.items():
                string_all.append(str(BaseModel(**value)))
            print(string_all)
            return
        print("** class doesn't exist **")

    def do_update(self, arg):
        'command to update an instance'
        args = self.split_args(arg)
        if not args[0]:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
        if len(args) == 3:
            print("** value missing **")

        dir_class = storage.all()
        for key, value in dir_class.items():
            if key == args[0] + '.' + args[1]:
                value[args[2]] = args[3].strip('"')
                storage.save()
                return
        print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
