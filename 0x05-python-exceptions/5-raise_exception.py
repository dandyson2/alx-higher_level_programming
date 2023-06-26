#!/usr/bin/python3
def raise_exception():
    try:
        raise 1 + "TypeError"
    except TypeError as e:
        raise e


