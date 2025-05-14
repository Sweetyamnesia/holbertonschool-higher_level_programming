#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        return list(map(lambda x: x > x, my_list))
    except x < my_list:
        print("x inférieur à my_list")
