#!/usr/bin/python3

def sqrt(a):
    return a ** 2


def get_sqr(tab=[]):
    result = map(sqrt, tab)
    return list(result)


def square_matrix_simple(matrix=[]):
    result = map(get_sqr, matrix)
    return list(result)
