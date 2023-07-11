#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
from typing import Union


class BaseGeometry:
    """Base class for geometry"""

    def area(self) -> float:
        """Calculates the area"""
        raise NotImplementedError("area() is not implemented")

    def integer_validator(self, name: str, value: Union[int, float]) -> None:
        """Validates if value is a positive integer"""
        if not isinstance(value, (int, float)):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class representing a rectangle using BaseGeometry"""

    def __init__(self, width: int, height: int) -> None:
        """Initialize a new rectangle"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self) -> int:
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self) -> str:
        """Returns the print() and str() representation of a Rectangle"""
        string = "[{}] ".format(self.__class__.__name__)
        string += str(self.__width) + "/" + str(self.__height)
        return string
