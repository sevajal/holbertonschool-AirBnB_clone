#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to AirBnBClone'
    prompt = '(hbnb) '

    def split_args(self, line):
        list = []
        for arg in line.split(" "):
            list.append(arg)
        return list

    def do_EOF(self, arg):
        'EOF command to exit the program\n'
        exit(0)

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        exit(0)

    def do_create(self, arg):
        'Create command creates new instance\n'
        if not arg:
            print("** class name missing **")
            return
        if arg != "BaseModel":
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance(class/id)"""
        args = self.split_args(arg)
        if not args[0]:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if not args[1]:
            print("** instance id missing **")
            return
        dir_class = storage.all()
        for key, value in dir_class.items():
            if key == args[0] + '.' + args[1]:
                print(BaseModel(**value))
                return
        print("** no instance found **")

    def do_destroy(self, arg):
        args = self.split_args(arg)
        if not args[0]:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if not args[1]:
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
        if arg != "BaseModel":
            print("** class doesn't exist **")
            return
        string_all = []
        dir_class = storage.all()
        for key, value in dir_class.items():
            string_all.append(str(BaseModel(**value)))
        print(string_all)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
