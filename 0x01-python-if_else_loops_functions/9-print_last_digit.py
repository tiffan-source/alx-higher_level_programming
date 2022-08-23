#!/usr/bin/python3

def print_last_digit(number):
    if number >= 0:
        lst = number % 10
    else:
        lst = (number * -1) % 10

    print(lst, end="")
    return lst
