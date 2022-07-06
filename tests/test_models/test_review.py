#!/usr/bin/python3

"""Unittest for Review Class"""


import unittest
from models.review import Review
from models.base_model import BaseModel


class Test_base(unittest.TestCase):
    """Class Test for Review"""

    def test_uuid(self):
        """Test the uuid"""
        r1 = Review()
        r2 = Review()
        self.assertIsInstance(r1, Review)
        self.assertTrue(hasattr(r1, "id"))
        self.assertNotEqual(r1.id, r2.id)
        self.assertIsInstance(r1.id, str)

    def test_is_subclass(self):
        """Test is is a subclass"""
        r1 = Review()
        self.assertIsInstance(r1, BaseModel)

    def test_datetime(self):
        """Test the datetime attributes"""
        r1 = Review()
        self.assertTrue(hasattr(r1, "created_at"))
        self.assertTrue(hasattr(r1, "updated_at"))
        self.assertNotEqual(r1.created_at, r1.updated_at)

    def test_attributes(self):
        """Test the attributes"""
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

    def test_add_attributes(self):
        """Test new attributes"""
        r1 = Review()
        r1.email = "Sebas@holberton.com"
        r1.number = 90
        self.assertTrue(hasattr(r1, "email"))
        self.assertEqual(r1.email, "Sebas@holberton.com")
        self.assertIsInstance(r1.email, str)
        self.assertTrue(hasattr(r1, "number"))
        self.assertEqual(r1.number, 90)
        self.assertIsInstance(r1.number, int)


if __name__ == '__main__':
    unittest.main()
