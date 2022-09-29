#!/usr/bin/python3
"""Module define fonction to determine if isinstance or subinstance"""


def is_kind_of_class(obj, a_cls):
    """
    is_kind_of_class - return True if the object is exaclty
    an instance o sub instance of the specified class and false otherwise
    """
    if type(obj) in [a_cls] isinstance(obj, a_cls) or issubclass(obj, a_cls):
        return True
    return False
