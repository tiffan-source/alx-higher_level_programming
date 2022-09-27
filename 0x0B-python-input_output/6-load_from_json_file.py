#!/usr/bin/python3
"""module define function to create object
from file using json description"""
import json


def load_from_json_file(filename):
    """ load_from_json_file - create an object from json file
    filename: file to read """
    with open(filename, "r", encoding="UTF-8") as f:
        obj = f.readline()
        return json.loads(obj)
