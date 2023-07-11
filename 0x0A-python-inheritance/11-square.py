#!/usr/bin/python3
"""This module defines a Rectangle"""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width, height):
        """Initialize a new rectangle"""
        self._width = width
        self._height = height

    def area(self):
        """Calculate the area of the rectangle"""
        return self._width * self._height

    def __str__(self):
        """Return a string representation of the rectangle"""
        return "Rectang(width={}, height={})".format(self._width, self._height)


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """Initialize a new square"""
        super().__init__(size, size)
        self._size = size

    def __str__(self):
        """Return a string representation of the square"""
        return "Square(side={})".format(self._size)
