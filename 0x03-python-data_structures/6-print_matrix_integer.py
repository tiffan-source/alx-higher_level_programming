#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) != 0:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                end = " " if j < len(matrix[i]) - 1 else ""
                print("{:d}".format(matrix[i][j]), end=end)
            print("", end="\n")
