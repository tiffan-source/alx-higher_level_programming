#!/usr/bin/python3
"""Module define fonction to determine if isinstance"""


def is_same_class(obj, a_class):
    """
    is_same_class - return True if the object is exaclty
    an instance of the specified class and false otherwise
    """
    if type(obj) in [a_class]:
        return True
    return False
