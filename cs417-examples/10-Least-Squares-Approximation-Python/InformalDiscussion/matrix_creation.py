from __future__ import annotations
#  from typing import list
from typing import TextIO, Generator

import sys

def do_something(to_avg: list[float]) -> float:
    """
    Do something

    Args:

        a:
        b:

    Returns
        returns something
    """

    pass


def read_points_from_file(point_file: TextIO) -> list[tuple[float, float]]:
    """
    Read in a set of points from a file. The first entry on each row will be
    treated as x and the second entry will be treated as f(x).

    Args:
        point_file: file to read

    Returns:
        list of points in the form [(x_0, y_0), (x_1, y_1), ...]
    """

    # This can be improved quite a bit with a list comprehension
    points = []
    for line in point_file:
        nums = line.split()

        points.append((float(nums[0]), float(nums[1])))

    return points


def transpose_of(matrix: list[list[float]]) -> list[list[float]]:
    """
    T.B.W

    Args:
        matrix: input matrix

    Returns:
        transpose of the input matrix
    """

    input_rows = len(matrix)
    input_cols = len(matrix[0])

    output_rows = input_cols
    output_cols = input_rows

    transpose = [[0 for _ in range(0, output_cols)] for _ in range(0, output_rows)]

    for i in range(0, input_rows):
        for j in range(0, input_cols):
            transpose[j][i] = matrix[i][j]

    return transpose

def multiply(lhs, rhs):
    """
    T.B.W
    """
    lhs_cols = len(lhs[0])
    result_rows = len(lhs)
    result_cols = len(rhs[0])

    result = [[0 for _ in range(0, result_cols)] for _ in range(0, result_rows)]

    for i in range(0, result_rows):
        for j in range(0, result_cols):
            for k in range(0, lhs_cols):
                result[i][j] += lhs[i][k] * rhs[k][j]

    return result

def main():

    with open(sys.argv[1], "r") as the_file:
        points = read_points_from_file(the_file)

    # Print Points for Demo Purposes
    print(points)

    for x, y in points:
        print(f"{x:>3f}, {y:>3f}")

    print()


    # Derive X
    matrix_X = [[1, x] for x, y in points]
    print(matrix_X)
    print()

    # Derive X^T
    matrix_XT = transpose_of(matrix_X)
    print(matrix_XT)
    print()

    # Derive Y
    #  matrix_Y = []
    #  for _, y in points:
        #  matrix_Y.append(y)

    matrix_Y = [[y] for _, y in points]
    print(matrix_Y)
    print()

    matrix_XTX = multiply(matrix_XT, matrix_X)
    print(matrix_XTX)

    matrix_XTY = multiply(matrix_XT, matrix_Y)
    print(matrix_XTY)



















if __name__ == "__main__":
    main()
