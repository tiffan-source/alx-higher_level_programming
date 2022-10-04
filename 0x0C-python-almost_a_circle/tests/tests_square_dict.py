#!/usr/bin/python3
import unittest
from models.square import Square


class Square_Dic_Test(unittest.TestCase):

    def test_doc_to_dictionary_square(self):
        self.assertIsNotNone(Square.to_dictionary.__doc__)

    def test_give_dictionary_Square(self):
        rct = Square(200, 45, 90, 100)
        self.assertTrue(type(rct.to_dictionary()) in [dict])
        self.assertEqual((rct.to_dictionary())["id"], 100)
        self.assertEqual((rct.to_dictionary())["size"], 200)
        self.assertEqual((rct.to_dictionary())["x"], 45)
        self.assertEqual((rct.to_dictionary())["y"], 90)
