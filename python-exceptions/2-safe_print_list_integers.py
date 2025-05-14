#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for element in my_list:
            print("{:d}".format(element))
            return True
    except Exception:
        return False
