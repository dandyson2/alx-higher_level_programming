#!/usr/bin/python3

"""A class that defines a rectangle"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing the rectangle class

        Args:
            width (int): Represents the width of the rectangle
            height (int): Represents the height of the rectangle

        Raises:
            TypeError: If width or height is not an integer
            ValueError: If width or height is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute

        Args:
            value (int): The value to set as width

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than zero
        """
        self.__validate_dimension(value, "width")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attribute

        Args:
            value (int): The value to set as height

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than zero
        """
        self.__validate_dimension(value, "height")
        self.__height = value

    def __validate_dimension(self, value, dimension):
        """Validates the value of width or height

        Args:
            value (int): The value to validate
            dimension (str): The dimension ("width" or "height")

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError(f"{dimension} must be an integer")
        while value < 0:
            raise ValueError(f"{dimension} must be >= 0")

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
