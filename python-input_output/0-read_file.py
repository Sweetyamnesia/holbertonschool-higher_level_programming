#!/usr/bin/python3

def read_file(filename=""):
    # function which reads a text file
    with open("my_file_0.txt", "r")as file:
        content = file.read()
    print(content)
