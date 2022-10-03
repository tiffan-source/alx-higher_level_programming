#!/usr/bin/python3
from models.rectangle import Rectangle
import unittest


class Property_Test(unittest.TestCase):

    def test_raise_width_exception(self):
        with self.assertRaises(TypeError):
            data = Rectangle("Hello", 200)

    def test_raise_height_exception(self):
        with self.assertRaises(TypeError):
            data = Rectangle(200, "test")
        with self.assertRaises(TypeError):
            data = Rectangle(200, (43, ))

    def test_raise_valueError_height(self):
        with self.assertRaises(ValueError):
            data = Rectangle(-200, 233)
        with self.assertRaises(ValueError):
            data = Rectangle(200, 0)

    def test_raise_valueError_width(self):
        with self.assertRaises(ValueError):
            data = Rectangle(200, -233)
        with self.assertRaises(ValueError):
            data = Rectangle(200, 0)

    def test_raise_x_exception(self):
        with self.assertRaises(TypeError):
            data = Rectangle(200, 200, x="")

    def test_raise_y_exception(self):
        with self.assertRaises(TypeError):
            data = Rectangle(200, 54, x=43, y="")

    def test_raise_valueError_x(self):
        with self.assertRaises(ValueError):
            data = Rectangle(200, 233, x=-45)

    def test_raise_valueError_y(self):
        with self.assertRaises(ValueError):
            data = Rectangle(200, 233, y=-30)
