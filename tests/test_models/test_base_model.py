#!/usr/bin/python3

"""Unittest for BaseModel Class"""

import unittest
from models.base_model import BaseModel

class Test_base(unittest.TestCase):
    """Class Test for BaseMmodel"""

    def test_uuid(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)

    def test_datetime(self):
        bm1 = BaseModel()
        self.assertTrue(hasattr(bm1, "created_at"))
        self.assertTrue(hasattr(bm1, "updated_at"))
        self.assertNotEqual(bm1.created_at, bm1.updated_at)
    
    def test_add_attributes(self):
        bm1 = BaseModel()
        bm1.name = "Sebas"
        bm1.number = 90
        self.assertTrue(hasattr(bm1, "name"))
        self.assertEqual(bm1.name, "Sebas")
        self.assertIsInstance(bm1.name, str)
        self.assertTrue(hasattr(bm1, "number"))
        self.assertEqual(bm1.number, 90)
        self.assertIsInstance(bm1.number, int)


    
    """def test_module_docstring(self):
        self.assertNotEqual(print(__import__("base_model").__doc__), "")

    def test_class_docstring(self):
        self.assertNotEqual(print(__import__("base_model").BaseModel.__doc__), "")

    def test_func_docstrings(self):
        self.assertNotEqual(print(__import__("base_model").__init__.__doc__), "")
        self.assertNotEqual(print(__import__("base_model").__str__.__doc__), "")
        self.assertNotEqual(print(__import__("base_model").save.__doc__), "")
        self.assertNotEqual(print(__import__("base_model").to_dict.__doc__), "")"""

if __name__ == '__main__':
    unittest.main()
