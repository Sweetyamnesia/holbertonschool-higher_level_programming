#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    for i in range(x):
        try:
            count = 0
            element = my_list[i]
            print("{:d}".format(element), end="")
            count += 1
        except (ValueError, TypeError):
            continue

    print()
    return count
