#!/usr/bin/python3
"""
A module that defines a square.
"""


class Square:
    """
    A class that represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes an instance of the Square class.

        Args:
            size (int): Represents the size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """
        for value, message in [(size, 'size must be an integer'),
                               (size < 0, 'size must be >= 0')]:
            if not isinstance(value, int):
                raise TypeError(message)
            if value:
                raise ValueError(message)

        self.__size = size
