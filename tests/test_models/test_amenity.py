#!/usr/bin/python3

"""Unittest for Amenity Class"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class Test_base(unittest.TestCase):
    """Class Test for Amenity"""

    def test_uuid(self):
        am1 = Amenity()
        am2 = Amenity()
        self.assertIsInstance(am1, Amenity)
        self.assertTrue(hasattr(am1, "id"))
        self.assertNotEqual(am1.id, am2.id)
        self.assertIsInstance(am1.id, str)

    def test_is_subclass(self):
        am1 = Amenity()
        self.assertIsInstance(am1, BaseModel)
    
    def test_datetime(self):
        am1 = Amenity()
        self.assertTrue(hasattr(am1, "created_at"))
        self.assertTrue(hasattr(am1, "updated_at"))
        self.assertNotEqual(am1.created_at, am1.updated_at)

    def test_attributes(self):
        am1 = Amenity()
        self.assertTrue(hasattr(am1, "name"))
        self.assertEqual(am1.name, "")
        self.assertIsInstance(am1.name, str)

    """def test_module_docstring(self):
        self.assertNotEqual(print(__import__("amenity").__doc__), "")

    def test_class_docstring(self):
        self.assertNotEqual(print(__import__("amenity").Amenity.__doc__), "")"""

if __name__ == '__main__':
    unittest.main()