#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if isinstance(a_dictionary, dict):
        key = []
        for i in a_dictionary:
            if a_dictionary[i] == value:
                key.append(i)
        for i in key:
            del a_dictionary[i]
        return a_dictionary
