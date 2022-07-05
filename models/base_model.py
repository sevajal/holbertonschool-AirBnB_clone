#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage

class BaseModel:

    def __init__(self, *args, **kwargs):

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.fromisoformat(value)
                if key == "updated_at":
                    self.updated_at = datetime.fromisoformat(value)
                if key != "__class__" and key != "updated_at" and key != "created_at":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        string_str = "[" + self.__class__.__name__ + "] "
        string_str += "({}) {}".format(self.id, self.__dict__)
        return string_str

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        self.created_at = self.created_at.isoformat('T','auto')
        self.updated_at = self.updated_at.isoformat('T','auto')
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__
