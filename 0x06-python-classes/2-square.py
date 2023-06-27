#!/usr/bin/python3
def __init__(self, size=0):
    for val in (size,):
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        if val < 0:
            raise ValueError("size must be >= 0")

    self.__size = size
