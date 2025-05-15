#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for my_list_1, my_list_2 in zip(my_list_1, my_list_2):
            result.append(my_list_1 / my_list_2)
    except ZeroDivisionError:
        return None
    finally:
        print("{:d}".format(list_length))
        return result
