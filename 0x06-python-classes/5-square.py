#!/usr/bin/python3
"""A module that defines a square based on the previous"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initializing this square class

        Args:
            size: represents the size of the square defined

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Retrieves size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of square

        Args:
            value: the value to set as the size

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than zero
        """

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate the area of the square

        Returns:
            The square of the size
        """

        return self.__size ** 2

    def my_print(self):
        """Print the square using '#'"""

        if self.__size == 0:
            print()
        else:
            i = 0
            while i < self.__size:
                print("#" * self.__size)
                i += 1
