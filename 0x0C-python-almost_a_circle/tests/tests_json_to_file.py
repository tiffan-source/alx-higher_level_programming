#!/usr/bin/python3
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Json_File_Test(unittest.TestCase):

    def setUp(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def tearDown(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_doc_json_file_function(self):
        self.assertIsNotNone(Base.save_to_file.__doc__)

    def test_file_rectangle_create(self):
        r1 = Rectangle(200, 300)
        r2 = Rectangle(100, 500, 45, 65, 90)
        lst = [r1, r2]
        Base.save_to_file(lst)
        self.assertTrue(os.path.exists("Rectangle.json"))
        self.assertFalse(os.path.exists("Square.json"))

    def test_file_square_create(self):
        r1 = Square(200, 300)
        r2 = Square(500, 45, 65, 90)
        lst = [r1, r2]
        Base.save_to_file(lst)
        self.assertFalse(os.path.exists("Rectangle.json"))
        self.assertTrue(os.path.exists("Square.json"))

    def test_file_both_create(self):
        lst = None
        Base.save_to_file(lst)
        self.assertTrue(os.path.exists("Rectangle.json"))
        self.assertTrue(os.path.exists("Square.json"))
