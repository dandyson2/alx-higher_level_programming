#!/usr/bin/python3
"""Magic Python class"""


import math


class MagicClass:
    """
    A class representing magic.

    Attributes:
        radius (float): The radius of the magic.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass object.

        Args:
            radius (float): The radius of the magic. Default is 0.

        Raises:
            TypeError: If radius is not a number.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the magic.

        Returns:
            float: The area of the magic.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the magic.

        Returns:
            float: The circumference of the magic.
        """
        return 2 * math.pi * self.__radius
