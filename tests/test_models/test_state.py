#!/usr/bin/python3

"""Unittest for State Class"""


import unittest
from models.state import State
from models.base_model import BaseModel


class Test_base(unittest.TestCase):
    """Class Test for State"""

    def test_uuid(self):
        """Test the uuid"""
        s1 = State()
        s2 = State()
        self.assertIsInstance(s1, State)
        self.assertTrue(hasattr(s1, "id"))
        self.assertNotEqual(s1.id, s2.id)
        self.assertIsInstance(s1.id, str)

    def test_is_subclass(self):
        """Test if is a subclass"""
        s1 = State()
        self.assertIsInstance(s1, BaseModel)

    def test_datetime(self):
        """Test the datetime attributes"""
        s1 = State()
        self.assertTrue(hasattr(s1, "created_at"))
        self.assertTrue(hasattr(s1, "updated_at"))
        self.assertNotEqual(s1.created_at, s1.updated_at)

    def test_attributes(self):
        """Test the attributes"""
        s1 = State()
        self.assertTrue(hasattr(s1, "name"))
        self.assertEqual(s1.name, "")
        self.assertIsInstance(s1.name, str)

    def test_add_attributes(self):
        """Test new attributes"""
        s1 = State()
        s1.email = "Sebas@holberton.com"
        s1.number = 90
        self.assertTrue(hasattr(s1, "email"))
        self.assertEqual(s1.email, "Sebas@holberton.com")
        self.assertIsInstance(s1.email, str)
        self.assertTrue(hasattr(s1, "number"))
        self.assertEqual(s1.number, 90)
        self.assertIsInstance(s1.number, int)


if __name__ == '__main__':
    unittest.main()
