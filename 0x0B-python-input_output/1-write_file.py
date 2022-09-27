#!/usr/bin/python3
""" module define function to write
sting inside a file"""


def write_file(filename="", text=""):
    """write_file - write a string to text file
    and returns the number of characters written
    Args
    filename: name of the file to use
    text: text to write
    """
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
