#!/usr/bin/python3
"""module define function to returns an
object represented by a JSON string"""
import json


def from_json_string(my_obj):
    """ from_json_string - returns an
    object represented by a JSON string"""
    return json.loads(my_obj)
