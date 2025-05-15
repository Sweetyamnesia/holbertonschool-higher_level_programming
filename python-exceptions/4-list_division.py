#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            element1 = my_list_1[i]
            element2 = my_list_2[i]

            if element1 != int or float or element2 != int or float:
                print("wrong type")
                result = 0
            elif element2 == 0:
                print("division by 0")
            else:
                element1 / element2
    except IndexError:
        print("out of range")
    finally:
        print("{:d}".format(list_length))
    return result
