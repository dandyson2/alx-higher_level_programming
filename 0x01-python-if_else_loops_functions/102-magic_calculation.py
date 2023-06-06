#!/usr/bin/python3
def magic_calculation(a, b, c):
    """Perform a custom magic calculation."""
    if a < b:
        result = c
    elif c > b:
        result = a + b
    else:
        result = a * b - c

    return (result);
