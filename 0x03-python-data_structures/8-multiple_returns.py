#!/usr/bin/python3

def multiple_returns(sentence):
    f_c = ''
    if len(sentence) == 0:
        f_c = None
    else:
        f_c = sentence[0]
    return (len(sentence), f_c)
