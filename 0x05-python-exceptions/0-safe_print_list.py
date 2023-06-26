#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    total = 0
    i = 0
    while i < x:
        try:
            print(f"{my_list[i]}", end="")
            total += 1
        except IndexError:
            break
        i += 1
    print()
    return total
