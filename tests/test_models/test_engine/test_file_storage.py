#!/usr/bin/python3

"""Unittest for FileStorage Class"""

import unittest
from models.engine import file_storage
from models.engine.file_storage import FileStorage

class Test_base(unittest.TestCase):
    """Class Test for FileStorage"""

    @classmethod
    def setUpClass(cls):
        FileStorage.__objects = {}
    
    def test_attributes(self):
        file = FileStorage.__objects
        self.assertEqual(file, {})
        self.assertIsInstance(file, dict)

if __name__ == '__main__':
    unittest.main()