#!/usr/bin/python3
"""
Module composed by a function that multiplies 2 matrices using NumPy

"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (ndarray): Matrix A.
        m_b (ndarray): Matrix B.

    Returns:
        ndarray: Result of the matrix multiplication.

    Raises:
        ValueError: If the dimensions of the matrices are incompatible.

    """
    if m_a.shape[1] != m_b.shape[0]:
        raise ValueError("Matrix dimensions are incompatible for multipli.")

    return np.matmul(m_a, m_b)
