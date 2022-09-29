#!/usr/bin/python3
"""Module fonction to get all attribute of an object"""


def lookup(obj):
    """lookup - return all attribute and finction of an obj
    obj: object to lookup
    Return: list of data"""
    return dir(obj)
