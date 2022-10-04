#!/usr/bin/python3
"""
Module define Base class
"""
import json


class Base:
    """
    class Base
    __nb_objects: number of object instance
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to_json_dictionary - returns the JSON string
        representation of list_dictionaries
        list_dictionaries: list of dictionnary
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
