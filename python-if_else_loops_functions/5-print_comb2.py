#!/usr/bin/python3
for n in range(0, 100):
    if n < 99:
        print(f"{n:02d}, ".format(n), end="")
    else:
        print(f"{n:02d}".format(n))
