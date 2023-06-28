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

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The square of the size.
        """

        return self.__size ** 2
