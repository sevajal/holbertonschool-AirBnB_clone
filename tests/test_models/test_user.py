#!/usr/bin/python3

"""Unittest for User Class"""

import unittest
from models.user import User

class Test_base(unittest.TestCase):
    """Class Test for User"""

    def test_uuid(self):
        user1 = User()
        user2 = User()
        self.assertIsInstance(user1, User)
        self.assertTrue(hasattr(user1, "id"))
        self.assertNotEqual(user1.id, user2.id)
        self.assertIsInstance(user1.id, str)

if __name__ == '__main__':
    unittest.main()