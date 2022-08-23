#!/usr/bin/python3

def uppercase(str):
    l_str = len(str)
    for i in range(l_str):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            print(chr(ord(str[i]) - 32), end=('' if i != l_str - 1 else '\n'))
        else:
            print(str[i], end=('' if i != l_str - 1 else '\n'))
