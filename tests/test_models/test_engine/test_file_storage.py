#!/usr/bin/python3
"""
Unittest for FileStorage Class
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json

class Test_FileStorage(unittest.TestCase):
    """Class Test for FileStorage"""
    base = BaseModel()

    @classmethod
    def setUpClass(cls):
        """Test the setup"""
        FileStorage.__objects = {}

    def test_attributes(self):
        """Test the attributes"""
        file = FileStorage.__objects
        self.assertEqual(file, {})
        self.assertIsInstance(file, dict)

    def testClassInstance(self):
        """ Check instance """
        self.assertIsInstance(storage, FileStorage)

    def testStoreBaseModel(self):
        """ Test save and reload functions """
        self.base.new_name = "new_instance"
        self.base.save()
        basemodel_dict = self.base.to_dict()
        all_objs = storage.all()

        key = basemodel_dict['__class__'] + "." + basemodel_dict['id']
        self.assertEqual(key in all_objs, True)

if __name__ == '__main__':
    unittest.main()
