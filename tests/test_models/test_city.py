#!/usr/bin/python3

"""Unittest for City Class"""

import unittest
from models.city import City
from models.base_model import BaseModel

class Test_base(unittest.TestCase):
    """Class Test for City"""

    def test_uuid(self):
        c1 = City()
        c2 = City()
        self.assertIsInstance(c1, City)
        self.assertTrue(hasattr(c1, "id"))
        self.assertNotEqual(c1.id, c2.id)
        self.assertIsInstance(c1.id, str)

    def test_is_subclass(self):
        c1 = City()
        self.assertIsInstance(c1, BaseModel)

    def test_datetime(self):
        c1 = City()
        self.assertTrue(hasattr(c1, "created_at"))
        self.assertTrue(hasattr(c1, "updated_at"))
        self.assertNotEqual(c1.created_at, c1.updated_at)

    def test_attributes(self):
        c1 = City()
        self.assertTrue(hasattr(c1, "name"))
        self.assertEqual(c1.name, "")
        self.assertIsInstance(c1.name, str)
        self.assertTrue(hasattr(c1, "state_id"))
        self.assertEqual(c1.state_id, "")
        self.assertIsInstance(c1.state_id, str)

    """def test_module_docstring(self):
        self.assertNotEqual(print(__import__("city").__doc__), "")

    def test_class_docstring(self):
        self.assertNotEqual(print(__import__("city").City.__doc__), "")"""


if __name__ == '__main__':
    unittest.main()