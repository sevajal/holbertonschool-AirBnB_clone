#! /usr/bin/python3

import json
import os.path


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj): 
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            self.__objects = json.dumps(self.__objects, sort_keys=True, default=str)
            file.write(self.__objects)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                self.__objects = json.loads(file.read())
