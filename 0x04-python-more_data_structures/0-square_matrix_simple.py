#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix = [[[column][row] ** 2 for column in range(4)] for row in range(4)]
    print(
