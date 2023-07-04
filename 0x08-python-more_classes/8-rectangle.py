#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """Represents a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing this rectangle class

        Args:
            width (int): Represents the width of the rectangle.
            height (int): Represents the height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than zero.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        return 0 if self.__width == 0 or self.__height == 0 else 2 *
    (self.__width + self.__height)

    def __str__(self):
        """Presents a diagram of the rectangle defined for an object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        row = 0
        while row < self.__height:
            col = 0
            while col < self.__width:
                try:
                    rectangle += str(self.print_symbol)
                except Exception:
                    rectangle += type(self).print_symbol
                col += 1
            if row < self.__height - 1:
                rectangle += "\n"
            row += 1
        return rectangle

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message for every object that is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles and returns the bigger one or rect_2

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Returns:
            Rectangle: The bigger rectangle or rect_2 if they are equal.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of Rectan
        """
        while rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
