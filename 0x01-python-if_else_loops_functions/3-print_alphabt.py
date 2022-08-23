#!/usr/bin/python3

for i in range(97, 97 + 26):
    if chr(i) != 'e' and chr(i) != 'q':
        print("{}".format(chr(i)), end="")
