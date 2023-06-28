#!/usr/bin/python3
"""A module that defines a square."""


class Square:
    """Define a Square."""

    def __str__(self):
        """Teach Python to print the square my way."""
        return self.pos_print()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with size and position.

        Args:
            size (int): The length of a side of the square.
            position (tuple): The position of the square (coordinates).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property of the length of a side of the square.

        Raises:
            TypeError: If size is not an int.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Property of the position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 ints >= 0.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 ints >= 0.

        Returns:
            tuple: The position of the square.
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def pos_print(self):
        """Return the printed square with position."""
        pos = ""
        if not self.size:
            return "\n"
        w = 0
        while w < self.position[1]:
            pos += "\n"
            w += 1
        w = 0
        while w < self.size:
            i = 0
            while i < self.position[0]:
                pos += " "
                i += 1
            j = 0
            while j < self.size:
                pos += "#"
                j += 1
            pos += "\n"
            w += 1
        return pos

    def my_print(self):
        """Print the square."""
        print(self.pos_print(), end="")
