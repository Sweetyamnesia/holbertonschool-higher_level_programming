#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value == int:
            return True
        else:
            return False
    except Exception as e:
        print("{:d}".format(value))
