#!/usr/bin/python3
"""
Unittest for FileStorage Class
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel 
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

        """ pilas"""

    def test_docs(self):
        """Tests if everything is documented
        """

        #  Class check
        self.assertIsNotNone(FileStorage.__doc__)

        # Methods check
        self.assertIsNotNone(FileStorage.__init__.__doc__)
        self.assertIsNotNone(FileStorage.__str__.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)

    def test_exec_permissions(self):
        """Method that test for check the execution permissions
        """
        read = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(write)
        exect = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertFalse(exect)

    def test_is_an_instance(self):
        """Method that check if FileStorageInstance is an instance
        of FileStorage()
        """
        FileStorageInstance = FileStorage()
        self.assertIsInstance(FileStorageInstance, FileStorage)

    def test_different_id(self):
        """Method that check if each instance that is created has
        a unique id
        """
        instance1 = FileStorage()
        instance2 = FileStorage()
        self.assertNotEqual(instance1, instance2)

if __name__ == '__main__':
    unittest.main()
