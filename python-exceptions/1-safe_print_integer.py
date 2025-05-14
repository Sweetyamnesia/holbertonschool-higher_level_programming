#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value == int:
            return True
        else:
            print("{:d}".format(value))
    except Exception:
        return False
