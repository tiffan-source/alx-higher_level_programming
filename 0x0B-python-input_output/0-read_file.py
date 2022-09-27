#!/usr/bin/python3

"""Module define function to read
a file in UTF-8 format"""


def read_file(filename=""):
    """ read_file - reads a text file and
    prints it to stdout
    filename: name of the file to read
    """
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
