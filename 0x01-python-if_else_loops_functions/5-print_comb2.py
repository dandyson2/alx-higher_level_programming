#!/usr/bin/python3
number = 0
while number < 100:
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
    number += 1
