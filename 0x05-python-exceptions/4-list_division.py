#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            element_1 = my_list_1[i]
            element_2 = my_list_2[i]
            division = 0
            if isinstance(element_1, (int, float)) and isinstance(element_2, (int, float)):
                if element_2 != 0:
                    division = element_1 / element_2
                else:
                    print("division by 0")
            else:
                print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            result.append(division)
    return result
