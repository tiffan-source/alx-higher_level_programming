#!/usr/bin/python3
"""Module define class that inherit list class"""


class MyList(list):
    """ class MyList extend list and implement print_sorted """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        if len(self) == 0:
            print("[]")
        else:
            lst = self[:]
            for i in range(len(self)):
                for j in range(len(self)):
                    if lst[i] < lst[j]:
                        save = lst[i]
                        lst[i] = lst[j]
                        lst[j] = save
            print(lst)
