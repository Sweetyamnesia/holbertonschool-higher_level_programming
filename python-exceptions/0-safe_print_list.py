#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            element = my_list[i]
            print("{}".format(element), end="")
            count += 1
    except Exception:
        pass

    print()
    return count
