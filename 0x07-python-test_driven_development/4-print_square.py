#!/usr/bin/python3

"""
module define function to print square
and handle TypeError
"""

def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise TypeError("size must be >= 0")
    else:
        str = "#" * size
        for i in range(size):
            print(f"{str}")
