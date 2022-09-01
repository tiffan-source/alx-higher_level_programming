#!/usr/bin/python3

def roman_to_int(roman_string):
    lst = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    result = 0
    prev = 2000
    if isinstance(roman_string, str):
        for i in roman_string:
            result += lst[i]
            if (lst[i] > prev):
                result -= prev * 2
            prev = lst[i]
        return result
    else:
        return 0
