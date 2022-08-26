#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for i in matrix[i]:
            end = " " if i < len(matrix[i]) - 1 else "\n"
            print("{}".format(matrix[i][j]), end = end)
