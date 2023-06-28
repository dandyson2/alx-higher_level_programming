#!/usr/bin/python3
"""My square module"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Create a Square

        Args:
            size: length of a side of Square
            position: where the square is (coordinates)
        """
        self.size = size
        self.position = position

    def __str__(self):
        """Return a string representation of the square"""
        return self.pos_print()

    @property
    def size(self):
        """The property of size as the length of a side of Square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square

        Args:
            value: the value to set as the size

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """The property of the coordinates of this Square

        Raises:
            TypeError: if value is not a tuple
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of this Square

        Args:
            value: a tuple of two positive integers representing the position

        Raises:
            TypeError: if value is not a tuple
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Get the area of the square

        Returns:
            The square of the size
            """
        return self.__size ** 2

    def pos_print(self):
        """Return the square representation with respect to the position

        Returns:
            The square representation as a string
        """
        pos = ""
        if self.size == 0:
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
        """Print the square with respect to the position"""
        print(self.pos_print(), end='')
