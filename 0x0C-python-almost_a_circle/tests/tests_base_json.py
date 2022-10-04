#!/usr/bin/python3
import unittest
from models.base import Base

class JSON_Base_Test(unittest.TestCase):

    def test_doc_json_function(self):
        self.assertIsNotNone(Base.to_json_string.__doc__)

    def test_return_type(self):
        data = [{"id":90}]
        self.assertTrue(type(Base.to_json_string(data)) in [str])

    def test_value_if_none_or_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_value_if_data(self):
        self.assertEqual(Base.to_json_string([{"id":80}]), "[{\"id\": 80}]")
