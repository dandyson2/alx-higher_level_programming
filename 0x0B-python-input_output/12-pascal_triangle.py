#!/usr/bin/python3
"""This module defines a Pascal's Triangle function"""


def pascal_triangle(n):
    """Represents Pascal's Triangle of size n"""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) < n:
        tri = triangles[-1]
        tmp = [1]
        i = 0
        while i < len(tri) - 1:
            tmp.append(tri[i] + tri[i + 1])
            i += 1
        tmp.append(1)
        triangles.append(tmp)
    return triangles
