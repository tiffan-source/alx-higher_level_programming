#!/usr/bin/python3
"""Module define fonction to determine if isinstance or subinstance"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class - return True if the object is exaclty
    an instance o sub instance of the specified class and false otherwise
    """
    if isinstance(obj, a_class) or issubclass(obj, a_class):
        return True
    return False
