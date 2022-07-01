#! /usr/bin/python3

import json
import os.path
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        new_obj = str(obj.__name__) + "." + str(obj.id)
        self.__objects[new_obj] = obj

    def save(self):
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            file.write(json.dumps(self.__objects))

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                self.__object = json.loads(file.read())
