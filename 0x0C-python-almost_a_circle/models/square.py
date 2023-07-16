#!/usr/bin/python3
"""
    Module that defines a class Square implementation class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Implementation of square rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            Square initialization (overrides Rectangle init)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            Returns the size of square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            Size setter value
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value
