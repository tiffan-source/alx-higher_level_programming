#!/usr/bin/python3
"""module use to do multiplication betwee
two matrix"""


def matrix_mul(m_a, m_b):
    """matrix_mul do the product of two matrix
    m_a first matrix
    m_b second matrix
    """
    rslt = []
    somme = 0

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for i in m_a:
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")

    for i in m_b:
        if not isinstance(i, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0:
        raise TypeError("m_a can't be empty")

    for i in m_a:
        if len(i) == 0:
            raise TypeError("m_a can't be empty")

    if len(m_b) == 0:
        raise TypeError("m_b can't be empty")

    for i in m_b:
        if len(i) == 0:
            raise TypeError("m_b can't be empty")

    for i in m_a:
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")

    for i in m_b:
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    a = len(m_a[0])
    b = len(m_b[0])

    for i in m_a:
        if len(i) != a:
            raise TypeError("each row of m_a must be of the same size")

    for i in m_b:
        if len(i) != b:
            raise TypeError("each row of m_b must be of the same size")

    if a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    for i in range(len(m_a)):
        rslt.append([])
        for j in range(len(m_b)):
            somme = 0
            for k in range(a):
                somme += m_a[i][k] * m_b[k][j]
            rslt[i].append(somme)

    return rslt
