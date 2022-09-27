#!/usr/bin/python3

"""Module define function to read
a file in UTF-8 format"""


def read_file(filename=""):
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
