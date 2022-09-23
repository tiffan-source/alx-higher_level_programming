#!/usr/bin/python3

"""
module use to define a function that
print a string with indentation
"""

def text_indentation(text):
    """
    print a text with some indentation
    text: string to print with some indentation
    """

    no_space = False
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i in [".", "?", ":"]:
            no_space = True
            print(f"{i}", end="\n\n")
        else:
            if not ( i == " " and no_space == True ):
                print(f"{i}", end="")
                no_space = False
