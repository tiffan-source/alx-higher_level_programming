#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    sum = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            sum += 1
        print("")
        return sum
    except IndexError:
        print("", end="\n")
        return sum
