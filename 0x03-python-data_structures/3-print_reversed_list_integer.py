#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    l_lst = len(my_list)
    for i in range(l_lst):
        print("{:d}".format(my_list[l_lst - i - 1]))
