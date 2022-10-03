#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class Str_Test(unittest.TestCase):

    def test_str_doc(self):
        self.assertIsNotNone(Rectangle.__str__.__doc__)

    def test_str_not_x_y(self):
        data = Rectangle(400, 450, id=900)
        self.assertEqual(str(data), "[Rectangle] (900) 0/0 - 400/450")

    def test_str_full_data(self):
        data = Rectangle(400, 450, y=90, x=120, id=800)
        self.assertEqual(str(data), "[Rectangle] (800) 120/90 - 400/450")
