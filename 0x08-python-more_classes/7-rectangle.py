#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """Represents a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
        while not isinstance(value, int):
            raise TypeError("width must be an integer")
        while value < 0:
            raise ValueError("width must be >= 0")
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
        while not isinstance(value, int):
            raise TypeError("height must be an integer")
        while value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        while self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """Presents a diagram of the rectangle defined for an object"""
        while self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                try:
                    rectangle += str(self.print_symbol)
                except Exception:
                    rectangle += type(self).print_symbol
            if column < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when an object is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
