#!/usr/bin/python3
"""A module that defines a square based on the previous """


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """
        Initializes an instance of the Square class.

        Args:
            size (int): Represents the size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The square of the size.
        """

        return self.__size ** 2
