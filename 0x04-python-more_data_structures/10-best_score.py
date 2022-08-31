#!/usr/bin/python3

def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        lst_s = list(a_dictionary)
        if len(lst_s) == 0:
            return (None)
        else:
            a = lst_s[0]
            for i in lst_s:
                if a_dictionary[a] < a_dictionary[i]:
                    a = i
            return (a)
