#!/usr/bin/python3

def uppercase(str):
    l_str = len(str)
    tmp = str

    for i in range(l_str):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            tmp = tmp[:i] + chr(ord(str[i]) - 32) + tmp[i + 1:]

    print("{}".format(tmp))
