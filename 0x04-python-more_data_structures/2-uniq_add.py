#!/usr/bin/python3

def check_exist(lst, data):
    for i in lst:
        if i == data:
            return True
    return False


def uniq_add(my_list=[]):
    data = 0
    lst = []
    for i in my_list:
        if not (check_exist(lst, i)):
            lst.append(i)
            data += i
    return data
