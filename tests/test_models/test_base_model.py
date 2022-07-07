#!/usr/bin/python3
"""Unittest for BaseModel Class
"""

import uuid
import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from datetime import datetime
import os

class BaseModelTests(unittest.TestCase):
    """Class Test for BaseModel"""

    def test_uuid(self):
        """Test the uuid"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)

    def test_datetime(self):
        """Test the datatime attributes"""
        bm1 = BaseModel()
        self.assertTrue(hasattr(bm1, "created_at"))
        self.assertTrue(hasattr(bm1, "updated_at"))
        self.assertNotEqual(bm1.created_at, bm1.updated_at)

    def test_add_attributes(self):
        """Test new attributes"""
        bm1 = BaseModel()
        bm1.name = "Sebas"
        bm1.number = 90
        self.assertTrue(hasattr(bm1, "name"))
        self.assertEqual(bm1.name, "Sebas")
        self.assertIsInstance(bm1.name, str)
        self.assertTrue(hasattr(bm1, "number"))
        self.assertEqual(bm1.number, 90)
        self.assertIsInstance(bm1.number, int)

    def test_general(self):
        bm1 = BaseModel()
        bm1.name = "Jhon"
        bm1.save()
        bm1_json = bm1.to_dict()
        self.assertEqual(bm1.name, bm1_json["name"])
        self.assertEqual("BaseModel", bm1_json["__class__"])
        self.assertEqual(bm1.id, bm1_json["id"])
        self.assertIsInstance(bm1.created_at, datetime)
        self.assertIsInstance(bm1.updated_at, datetime)

    my_model = BaseModel()

    def testSave(self):
        """ Test for a BaseModel instance """
        self.my_model.first_name = "First"
        self.my_model.save()
        first_dict = self.my_model.to_dict()
        self.my_model.first_name = "Second"
        self.my_model.save()
        sec_dict = self.my_model.to_dict()
        self.assertEqual(first_dict['created_at'], sec_dict['created_at'])
        self.assertNotEqual(first_dict['updated_at'], sec_dict['updated_at'])


    def setUp(self):
        """set environment to start testing"""
        # Empty objects in engine
        FileStorage._FileStorage__objects = {}
        # Remove file.json if exists
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """set enviroment when testing is finished"""
        # Empty objects in engine
        FileStorage._FileStorage__objects = {}
        # Remove file.json if exists
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance_type_id_class(self):
        """
        Checks for a instance of the class
        """
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertFalse(type(model) == type(BaseModel))
        self.assertFalse(id(model) == id(BaseModel))
        model_2 = BaseModel()
        self.assertTrue(type(model) == type(model_2))
        self.assertFalse(id(model) == id(model_2))

    def test_instances_attributes(self):
        """
        Checks attributes created to the new object
        """
        # Checks that base attributes are created for the object
        model = BaseModel()
        my_attrs = ['id', 'created_at', 'updated_at']
        for attr in my_attrs:
            self.assertEqual(attr in model.__dict__.keys(), True)

        # Checks that some falses attributes
        my_attrs = ['name', 'create_time', 'update_time']
        for attr in my_attrs:
            self.assertEqual(attr in model.__dict__.keys(), False)

    def test_unique_id(self):
        """
        Checks for a unique id
        """
        # Checks if two instances has diferents id
        model = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model.id, model_2.id)

    def test_datetime(self):
        """
        Checks for datetime attributes
        """
        # Test if two instnace has diferent datetime
        model = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model.created_at, model_2.created_at)
        self.assertNotEqual(model.updated_at, model_2.updated_at)

        # Test if attribute created_at and updated_at are datetime instance
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_UUID4(self):
        """
        Checks for the ID generation protocol
        """
        # Checks that the ID generated is the version 4
        model = BaseModel()
        version = uuid.UUID(model.id).version
        self.assertEqual(version, 4)

    def test_created_and_updated_at(self):
        """
        Checks if updated_t attribute changes when a new attribute is
        added to the object and created_at is the same all the time.
        """
        # Checks that updated_at changes
        model = BaseModel()
        updated_1 = str(model.updated_at)
        model.name = "Betty"
        model.save()
        updated_2 = str(model.updated_at)
        self.assertNotEqual(updated_1, updated_2)

        # Checks that created_at doesn't change
        model = BaseModel()
        created_1 = str(model.created_at)
        model.last_name = "Holberton"
        model.save()
        created_2 = str(model.created_at)
        self.assertEqual(created_1, created_2)

    def test_add_new_attributes(self):
        """
        Checks that can add new attributes to the objects
        """
        # Checks new attributes are added
        dict_attr = {'name': 'Betty', 'last': 'Holberton', 'age': 40}
        model = BaseModel()
        for key, value in dict_attr.items():
            setattr(model, key, value)
        for key, value in dict_attr.items():
            self.assertTrue(hasattr(model, key))
            self.assertEqual(getattr(model, key), value)

        # Checks for all attributes for the object
        my_attrs = ['id', 'created_at', 'updated_at', 'name', 'last', 'age']
        for attr in my_attrs:
            self.assertEqual(attr in model.__dict__.keys(), True)

    def test_str_method(self):
        """
        Checks str method
        """
        model = BaseModel()
        string = "[{}] ({}) {}".format(model.__class__.__name__, model.id,
                                       model.__dict__)
        self.assertEqual(str(model), string)

    def test_to_dict_method(self):
        """
        Checks dict method
        """
        # Checks if it convert to a dict type
        model = BaseModel()
        model.name = "Holberton"
        model.my_number = 89
        model.my_float = 100.54
        model.my_list = ["Hello", "world", 100]
        model.my_dict = {'name': 'Betty', 'last_name': 'Holberton', 'age': 85}
        model.save()
        model_json = model.to_dict()
        # checks if the method really convert to a dict type all the attributes
        self.assertEqual(type(model_json), dict)
        for key, value in model_json.items():
            # checks if the dict has the same attributes keys that the object
            self.assertTrue(hasattr(model, key))
            # checks if datetime was safe as a iso format and its type
            if key == "created_at" or key == "updated_at":
                _datetime = getattr(model, key).isoformat()
                self.assertEqual(_datetime, value)
                self.assertTrue(type(value) == str)
            # checks the class name attribute and its type
            elif key == "__class__":
                self.assertEqual(model.__class__.__name__, value)
                self.assertTrue(type(value) == str)
            else:
                # checks the value for others attributes
                self.assertEqual(getattr(model, key), value)
                # Checks the types and formats of the attributes
                if key == "id":
                    version = uuid.UUID(value).version
                    self.assertEqual(version, 4)
                    self.assertTrue(type(value), str)
                elif key == "name":
                    self.assertTrue(type(value) == str)
                elif key == "my_number":
                    self.assertTrue(type(value) == int)
                elif key == "my_list":
                    self.assertTrue(type(value) == list)
                elif key == "my_float":
                    self.assertTrue(type(value) == float)
                elif key == "my_dict":
                    self.assertTrue(type(value) == dict)


    def test_init_basemodel_from_dictionary(self):
        """
        Checks when it is passed a dictionary to the init method.
        """
        model = BaseModel()
        model.name = "Holberton"
        model.my_number = 89
        model_json = model.to_dict()
        my_new_model = BaseModel(**model_json)
        # Checks that the object has the same attributes that the model
        dict_attr = {'name': 'Holberton', 'my_number': 89, 'id': model.id,
                     'created_at': model.created_at,
                     'updated_at': model.updated_at}
        for key, value in dict_attr.items():
            self.assertTrue(hasattr(my_new_model, key))
            self.assertEqual(getattr(my_new_model, key), value)
        # Checks if __class__ attribute was not added
        self.assertTrue(hasattr(my_new_model, key))
        cls_name = getattr(my_new_model, key)
        self.assertNotEqual(cls_name, model_json["__class__"])

if __name__ == '__main__':
    unittest.main()
