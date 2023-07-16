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

    def update(self, *args, **kwargs):
        """
            assigns key/value argument to attributes
            kwargs is skipped if args is not empty
            Args:
                *args -  variable number of no-keyword args
                **kwargs - variable number of keyworded args
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def __str__(self):
        """
            The string function
        """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def to_dictionary(self):
        """
            The dictionary representation of a square, (return)
        """
        return {'id': getattr(self, "id"),
                'size': getattr(self, "width"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
