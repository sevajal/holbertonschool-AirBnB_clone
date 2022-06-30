#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    id = str(uuid.uuid4())
    created_at = datetime.now() 
    updated_at = datetime.now()
    
    def save(self):
        self.updated_at = datetime.now()

    def __str__(self):
        """ Returns a string representation"""
        self.id = BaseModel.id
        self.created_at = BaseModel.created_at
        self.updated_at = self.updated_at
        string_str = "[BaseModel] "
        string_str += "({}) {}".format(self.id, self.__dict__)
        return string_str   

    def to_dict(self):
        self.created_at = self.created_at.isoformat('T','auto')
        self.updated_at = self.updated_at.isoformat('T','auto')
        self.__dict__["__class__"] = BaseModel.__name__
        return self.__dict__
    
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            if key == "created_at":
                self.created_at = datetime.fromisoformat(value)
            if key == "updated_at":
                self.updated_at = datetime.fromisoformat(value)
            if key == "updated_at":
                self.updated_at = value
            if key == "name":
                self.name = value
            if key == "my_number":
                self.my_number = value
