#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if isinstance(my_list, list):
        c_lst = my_list[:]
        if idx < 0 or idx >= len(my_list):
            return (c_lst)
        c_lst[i] = my_list[idx]
        return (c_lst)
