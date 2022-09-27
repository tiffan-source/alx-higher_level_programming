#!/usr/bin/python3
import json
"""module define function to print the
representation in json of an object"""


def to_json_string(my_obj):
    """ to_json_string - returns the JSON
    representation of an object
    my_obj: object to parse to JSON"""
    return json.dumps(my_obj)
