#!/usr/bin/python3
def uppercase(s):
    new_str = "".join(chr(ord(i) - 32) if 97 <= ord(i) <= 122 else i for i in s)
    print("{}".format(new_str))
uppercase("")
