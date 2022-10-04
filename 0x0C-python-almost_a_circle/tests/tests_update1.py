#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.square import Square

class Update_Tests(unittest.TestCase):

    def test_doc_present(self):
        self.assertIsNotNone(Rectangle.update.__doc__)

    def test_no_argument(self):
        rct = Rectangle(200, 300, 25, 65, 90)
        rct.update()
        self.assertEqual(rct.width, 200)
        self.assertEqual(rct.height, 300)
        self.assertEqual(rct.x, 25)
        self.assertEqual(rct.y, 65)
        self.assertEqual(rct.id, 90)

    def test_args_set(self):
        rct = Rectangle(200, 300)
        rct.update(12, 34, id=34, width=5000)
        self.assertEqual(rct.width, 34)
        self.assertEqual(rct.height, 300)
        self.assertEqual(rct.x, 0)
        self.assertEqual(rct.y, 0)
        self.assertEqual(rct.id, 12)

    def test_kwargs_set(self):
        rct = Rectangle(200, 300)
        rct.update(id=34, width=5000)
        self.assertEqual(rct.width, 5000)
        self.assertEqual(rct.height, 300)
        self.assertEqual(rct.x, 0)
        self.assertEqual(rct.y, 0)
        self.assertEqual(rct.id, 34)

    def test_doc_present_Square(self):
        self.assertIsNotNone(Square.update.__doc__)

    def test_no_argument_Square(self):
        rct = Square(300, 25, 65, 90)
        rct.update()
        self.assertEqual(rct.size, 300)
        self.assertEqual(rct.height, 300)
        self.assertEqual(rct.x, 25)
        self.assertEqual(rct.y, 65)
        self.assertEqual(rct.id, 90)

    def test_args_set_Square(self):
        rct = Square(200)
        rct.update(12, 34, id=34, size=5000)
        self.assertEqual(rct.size, 34)
        self.assertEqual(rct.height, 34)
        self.assertEqual(rct.x, 0)
        self.assertEqual(rct.y, 0)
        self.assertEqual(rct.id, 12)

    def test_kwargs_set_Square(self):
        rct = Square(200)
        rct.update(id=34, size=5000)
        self.assertEqual(rct.size, 5000)
        self.assertEqual(rct.height, 5000)
        self.assertEqual(rct.x, 0)
        self.assertEqual(rct.y, 0)
        self.assertEqual(rct.id, 34)
