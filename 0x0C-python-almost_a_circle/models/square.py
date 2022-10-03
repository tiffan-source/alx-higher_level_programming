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
