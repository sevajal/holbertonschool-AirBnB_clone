#!/usr/bin/python3

"""Unittest for Review Class"""

import unittest
from models.review import Review
from models.base_model import BaseModel

class Test_base(unittest.TestCase):
    """Class Test for Review"""

    def test_uuid(self):
        r1 = Review()
        r2 = Review()
        self.assertIsInstance(r1, Review)
        self.assertTrue(hasattr(r1, "id"))
        self.assertNotEqual(r1.id, r2.id)
        self.assertIsInstance(r1.id, str)

    def test_is_subclass(self):
        r1 = Review()
        self.assertIsInstance(r1, BaseModel)

    def test_datetime(self):
        r1 = Review()
        self.assertTrue(hasattr(r1, "created_at"))
        self.assertTrue(hasattr(r1, "updated_at"))
        self.assertNotEqual(r1.created_at, r1.updated_at)

    def test_attributes(self):
        r1 = Review()
        self.assertTrue(hasattr(r1, "place_id"))
        self.assertEqual(r1.place_id, "")
        self.assertIsInstance(r1.place_id, str)
        self.assertTrue(hasattr(r1, "user_id"))
        self.assertEqual(r1.user_id, "")
        self.assertIsInstance(r1.user_id, str)
        self.assertTrue(hasattr(r1, "text"))
        self.assertEqual(r1.text, "")
        self.assertIsInstance(r1.text, str)
    
    """def test_module_docstring(self):
        self.assertNotEqual(print(__import__("review").__doc__), "")

    def test_class_docstring(self):
        self.assertNotEqual(print(__import__("review").Review.__doc__), "")"""

if __name__ == '__main__':
    unittest.main()