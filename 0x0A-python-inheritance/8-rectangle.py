#!/usr/bin/python3
"""Inherit from BaseGeometry"""
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
    """Class to define a rectangle using BaseGeometry"""

    def __init__(self, width: int, height: int) -> None:
        """Initialize a new Rectangle"""
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
