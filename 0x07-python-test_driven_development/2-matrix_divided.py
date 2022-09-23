#!/usr/bin/python3

"""module define function to
divided a list by integer
function matrix_divided(matrix, div)
"""

def matrix_divided(matrix, div):

    """matrix_divided
    matrix: list of list of integer
    div: number that divide list
    """
    result = []
    err = ""
    l_lst = 0

    if not isinstance(matrix ,list):
        err = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(err)

    if div == 0:
        err = "division by zero"
        raise TypeError(err)

    if type(div) not in [int, float]:
        err = "div must be a number"
        raise TypeError(err)

    for idx, lst in enumerate(matrix):
        if not isinstance(lst ,list):
            err = "matrix must be a matrix (list of lists) of integers/floats"
            raise TypeError(err)

        if idx == 0:
            l_lst = len(lst)

        if len(lst) != l_lst:
            err = "Each row of the matrix must have the same size"
            raise TypeError(err)

        if len(lst) == 0:
            err = "matrix must be a matrix (list of lists) of integers/floats"
            raise TypeError(err)

        new_lst = []
        for i in lst:
            if type(i) not in [int, float]:
                err= "matrix must be a matrix (list of lists) of integers/floats"
                raise TypeError(err)
            new_lst.append(round(i / div, 2))

        result.append(list(new_lst[:]))

    if len(result) == 0:
        err = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(err)

    return result
