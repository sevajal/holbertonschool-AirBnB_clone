#!/usr/bin/python3
"""
contains the entry point of
the command interpreter
"""

import cmd
from hashlib import new

from click import command
from models.base_model import BaseModel
from models import storage
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ class command interpreter """
    prompt = '(hbnb) '
    dict_class = {'BaseModel': BaseModel, 'User': User, 'State': State,
                  'City': City, 'Amenity': Amenity, 'Place': Place,
                  'Review': Review}

    def split_args(self, line):
        """ Split arguments by spaces """
        list = []
        for arg in line.split(" "):
            list.append(arg)
        return list

    def get_class(self, list_args):
        """ Get the class"""
        for key, value in self.dict_class.items():
            if key == list_args[0]:
                return value

    def precmd(self, arg):
        ' checks if arg is a method '
        if "()" in arg:
            class_name = arg.split('.')[0]
            command = arg.split('.')[1]
            command = command.split('()')[0]
            new_arg = command + ' ' + class_name
            return new_arg
        return arg

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def emptyline(self):
        'Empty line'
        pass

    def do_create(self, arg):
        'Create command creates new instance'
        if not arg:
            print("** class name missing **")
            return
        args = self.split_args(arg)
        class_name = self.get_class(args)
        if class_name is None:
            print("** class doesn't exist **")
            return
        new_instance = class_name()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        'Prints the string representation of an instance(class/id)'
        if not arg:
            print("** class name missing **")
            return
        args = self.split_args(arg)
        class_name = self.get_class(args)
        if class_name is None:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        dir_class = storage.all()
        for key, objects in dir_class.items():
            if key == args[0] + '.' + args[1]:
                print(objects)
                return
        print("** no instance found **")

    def do_destroy(self, arg):
        'command to destroy an instance'
        if not arg:
            print("** class name missing **")
            return
        args = self.split_args(arg)
        class_name = self.get_class(args)
        if class_name is None:
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
        class_name = ""
        args = self.split_args(arg)
        for key in self.dict_class.keys():
            if key == args[0]:
                class_name = key
        if not arg:
            string_all = []
            dir_class = storage.all()
            for key, value in dir_class.items():
                string_all.append(str(value))
            print(string_all)
            return
        if arg == class_name:
            string_all = []
            dir_class = storage.all()
            for key, value in dir_class.items():
                if key.split('.')[0] == class_name:
                    string_all.append(str(value))
            print(string_all)
            return
        print("** class doesn't exist **")

    def do_update(self, arg):
        'command to update an instance'
        if not arg:
            print("** class name missing **")
            return
        args = self.split_args(arg)
        class_name = self.get_class(args)
        if class_name is None:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        dir_class = storage.all()
        for key, value in dir_class.items():
            if key == args[0] + '.' + args[1]:
                dict_class = value.__dict__
                dict_class[args[2]] = args[3].strip('"')
                storage.save()
                return
        print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
