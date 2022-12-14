#!/usr/bin/python3
"""Module define fonction to determine if object
is a instance of class that inherit from other"""


def inherits_from(obj, a_cls):
    """
    inherits_from - return True if the object is
    sub instance of the specified class and false otherwise
    """
    try:
        if type(obj) not in [a_cls] and issubclass(obj.__class__, a_cls):
            return True
        return False
    except TypeError:
        return False
