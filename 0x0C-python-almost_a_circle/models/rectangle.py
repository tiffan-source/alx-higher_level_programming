#!/usr/bin/python3
"""
Module define class Rectangle
and some methode and attribute
to describe it
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle
    use to modelize a Rectangle
    herit property from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init - initialize all attribute of rectangle
        call init of parent class to init id
        """
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):
        if type(width) not in [int]:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        if type(height) not in [int]:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        if type(x) not in [int]:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        if type(y) not in [int]:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        area - get the area of rectangle
        """
        return self.width * self.height

    def display(self):
        """
        display - print a rectangle
        """
        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print("", end="\n")

    def __str__(self):
        """
        str - return string in format
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        a = f"[Rectangle] ({self.id}) {self.x}/{self.y}"
        b = f" - {self.width}/{self.height}"
        return a + b
