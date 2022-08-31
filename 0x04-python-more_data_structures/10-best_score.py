#!/usr/bin/python3

def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        lst_s = list(a_dictionary)
        if len(lst_s) == 0:
            return (None)
        else:
            a = a_dictionary[lst_s[0]]
            for i in lst_s:
                if a < a_dictionary[i]:
                    a = a_dictionary[i]
            return (a)
