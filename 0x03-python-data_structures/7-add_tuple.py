#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    l_rst = [0, 0]
    if len(tuple_a) > 0:
        l_rst[0] += tuple_a[0]
    if len(tuple_a) > 1:
        l_rst[1] += tuple_a[1]
    if len(tuple_b) > 0:
        l_rst[0] += tuple_b[0]
    if len(tuple_b) > 1:
        l_rst[1] += tuple_b[1]
    return l_rst[0], l_rst[1]
