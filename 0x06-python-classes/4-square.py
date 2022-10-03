#!/usr/bin/python3

"""
File descrie a square class
"""


class Square:
    """Class Square to represente a square and implement some method

    Attributes:
    __size (int): Size of the square
    """
    __size = 3

    def __init__(self, size=0):
        """Init function use to set atttribute size to the square

        Args:
        size (int): size of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2

    def size(self):
        return self.__size

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
