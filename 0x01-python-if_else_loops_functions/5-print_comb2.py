#!/usr/bin/python3

for i in range(0, 100):
    prefix_0 = '0' if i < 10 else ''
    print("{}{}".format(prefix_0, i), end=('\n' if i == 99 else ", "))
