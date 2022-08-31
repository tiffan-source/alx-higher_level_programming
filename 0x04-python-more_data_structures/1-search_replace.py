#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if isinstance(my_list, list):
        result = map(lambda a: a if a != search else replace, my_list)
        return list(result)
