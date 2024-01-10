#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    neuveux = []
    for col in matrix:
        oneMore = list(map(lambda x: x**2, col))
        neuveux.append(oneMore)
    return neuveux
