#!/usr/bin/python3
"""Square module"""


class Square:
    """
    A class that represents a square.

    Attributes:
        size (int): The length of a side of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square object.

        Args:
            size (int): The length of a side of the square. Default is 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        The size property representing the length of a side of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size property of the square.

        Args:
            value (int): The length of a side of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
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
            int: The area of the square.
        """
        return self.__size ** 2

    def __le__(self, other):
        """
        Less than or equal to comparison operator.

        Args:
            other (Square): The other Square object to compare with.

        Returns:
            bool: True if the area is less, False otherwise.
        """
        return self.area() <= other.area()

    def __lt__(self, other):
        """
        Less than comparison operator.

        Args:
            other (Square): The other Square object to compare with.

        Returns:
            bool: True if the area is less, False otherwise.
        """
        return self.area() < other.area()

    def __ge__(self, other):
        """
        Greater than or equal to comparison operator.

        Args:
            other (Square): The other Square object to compare with.

        Returns:
            bool: True if the area is greater, False otherwise.
        """
        return self.area() >= other.area()

    def __ne__(self, other):
        """
        Not equal to comparison operator.

        Args:
            other (Square): The other Square object to compare with.

        Returns:
            bool: True if area is greater, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Greater than comparison operator.

        Args:
            other (Square): The other Square object to compare with.

        Returns:
            bool: True if the area is greater,False otherwise.
        """
        return self.area() > other.area()

    def __eq__(self, other):
        """
        Equal to comparison operator.

        Args:
            other (Square): The other Square object to compare with.

        Returns:
            bool: True if the area  is equal, False otherwise.
        """
        return self.area() == other.area()
