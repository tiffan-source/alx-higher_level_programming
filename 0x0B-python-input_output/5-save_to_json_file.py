#!/usr/bin/python3
""" module define function to save json
representation of an object in a file"""
import json


def save_to_json_file(my_obj, filename):
    """ save_to_json_file - save representation
    of file in json representation

    my_obj: object to represent
    filename: file to modify"""
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(json.dumps(my_obj))
