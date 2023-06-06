#!/usr/bin/python3
def uppercase(s):
    new_str = ''.join(['{:c}'.format(ord(i) - 32) if ord(i) in range(97, 123) else i for i in s])
    print("{}".format(new_str))

uppercase("")
