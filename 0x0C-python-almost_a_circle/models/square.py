#!/usr/bin/python3
"""
module define square class that inherit from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square
    implement method and attribute to represent a square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        __init__ - intialize a square using __init__ from rectangle
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        __str__ - return square in form
        [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id:d}) {self.x:d}/{self.y:d} - {self.width:d}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        update - update informtaion about rectangle
        args: list of parameter to set
        """
        lgt = len(args)

        if (lgt == 0):
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
        if lgt >= 1:
            self.id = args[0]
        if lgt >= 2:
            self.size = args[1]
        if lgt >= 3:
            self.x = args[2]
        if lgt >= 4:
            self.y = args[3]

    def to_dictionary(self):
        """
        to_dictionary - return all property of square in dictionary form
        """

        dct = {}
        dct["id"] = self.id
        dct["size"] = self.size
        dct["x"] = self.x
        dct["y"] = self.y

        return dct
