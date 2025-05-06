#!/usr/bin/python3
for alphabet in range(ord('a'), ord('z') + 1):
    if chr(alphabet) not in ('q', 'e'):
        print(f"{chr(alphabet)}", end="")
