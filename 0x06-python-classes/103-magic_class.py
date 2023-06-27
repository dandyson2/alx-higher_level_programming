#!/usr/bin/python3
import math

class MagicClass:
    """
    A class representing a magic circle.

    Attributes:
        __radius (int or float): The radius of the magic circle.
    """

    def __init__(self, radius=0):
        """
        Initialize a MagicClass instance.

        Args:
            radius (int or float): The radius of the magic circle.

        Raises:
            TypeError: If radius is not a number.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the magic circle.

        Returns:
            float: The area of the magic circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate the circumference of the magic circle.

        Returns:
            float: The circumference of the magic circle.
        """
        return 2 * math.pi * self.__radius
