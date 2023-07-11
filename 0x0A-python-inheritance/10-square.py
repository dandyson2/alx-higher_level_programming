#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
from typing import Union


class BaseGeometry:
    """Base class for geometry"""

    def area(self) -> float:
        """Calculates the area"""
        raise NotImplementedError("area() is not implemented")

    def integer_validator(self, name: str, value: Union[int, float]) -> None:
        """Validates if value is a positive integer"""
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Class representing a square using Rectangle"""

    def __init__(self, size: int) -> None:
        """Initialize a new square"""
        super().__init__(size, size)
        self.__size = size
