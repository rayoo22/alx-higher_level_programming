#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for row in matrix:
        for col in range(len(row)):
            return [row[col] * row[col] for i in matrix]
