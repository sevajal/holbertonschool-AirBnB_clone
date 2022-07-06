#!/usr/bin/python3

"""Unittest for State Class"""

import unittest
from models.state import State

class Test_base(unittest.TestCase):
    """Class Test for State"""

    def test_uuid(self):
        s1 = State()
        s2 = State()
        self.assertIsInstance(s1, State)
        self.assertTrue(hasattr(s1, "id"))
        self.assertNotEqual(s1.id, s2.id)
        self.assertIsInstance(s1.id, str)

if __name__ == '__main__':
    unittest.main()