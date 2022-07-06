#! /usr/bin/python3
"""
Serializes instances to a JSON file and
deserializes JSON file to instances
"""

import json
import os.path


class FileStorage:
    """ class FileStorage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with the new key """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        dictionary = {}

        for key, value in self.__objects.items():
            dictionary[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(dictionary, file)

    def reload(self):
        """ Deserializes the JSON file to """
        from models.base_model import BaseModel
        from models.state import State
        from models.city import City
        from models.user import User
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        dict_class = {'BaseModel': BaseModel, 'User': User, 'State': State,
                      'City': City, 'Amenity': Amenity, 'Place': Place,
                      'Review': Review}

        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                for key, value in json.load(file).items():
                    self.__objects[key] = dict_class[value['__class__']](
                        **value)
