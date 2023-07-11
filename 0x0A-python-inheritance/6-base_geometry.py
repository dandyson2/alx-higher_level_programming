#!/usr/bin/python3
"""
Defines a base geometry class, BaseGeometry.
"""


class BaseGeometry:
    def area(self):
        raise Exception("area()  is not implemented in the derived class.")


bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(type(e).__name__, e))
