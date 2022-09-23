#!/usr/bin/python3

"""
Module use to
print a name with
function say_my_name
"""

def say_my_name(first_name, last_name=""):
    """
    print a name
    first_name: first name to print
    last_name: last name to print
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name}", end="")
        if not last_name == "":
            print(f" {last_name}")
