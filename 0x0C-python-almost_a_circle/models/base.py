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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file - returns the JSON string
        representation of list_dictionaries
        list_objs: list of object to add in the list
        """
        if list_objs is None:
            with open("Rectangle.json", "w") as f_j:
                f_j.write(cls.to_json_string("[]"))
            with open("Square.json", "w") as f_j:
                f_j.write(cls.to_json_string("[]"))
        elif len(list_objs) != 0 and issubclass(type(list_objs[0]), Base):
            with open(list_objs[0].__class__.__name__ + ".json", "w") as f_j:
                dct_to_set = []
                for i in list_objs:
                    dct_to_set.append(i.to_dictionary())

                f_j.write(cls.to_json_string(dct_to_set))
