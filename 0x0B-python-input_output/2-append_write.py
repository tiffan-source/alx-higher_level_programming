#!/usr/bin/python3
""" module define function to append
sting inside a file"""


def append_write(filename="", text=""):
    """append_write - append a string to text file
    and returns the number of characters written
    Args
    filename: name of the file to use
    text: text to write
    """
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
