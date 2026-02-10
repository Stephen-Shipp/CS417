from __future__ import annotations

from typing import TextIO, Generator

import sys

import numpy as np


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


def main():

    with open(sys.argv[1], "r") as the_file:
        points = read_points_from_file(the_file)

    # Print Points for Demo Purposes
    print(points)

    for x, y in points:
        print(f"{x:>3f}, {y:>3f}")

    print()


    # Derive X
    matrix_X = np.array([[1, x] for x, _y in points])
    print(matrix_X)
    print()

    # Derive X^T
    matrix_XT = matrix_X.transpose()
    print(matrix_XT)
    print()

    # Derive Y
    #  matrix_Y = []
    #  for _, y in points:
        #  matrix_Y.append(y)

    matrix_Y = np.array([[y] for _, y in points])
    print(matrix_Y)
    print()

    matrix_XTX = np.matmul(matrix_XT, matrix_X)
    print(matrix_XTX)

    print()
    matrix_XTY = np.matmul(matrix_XT, matrix_Y)
    print(matrix_XTY)

    matrix_augmented = np.hstack((matrix_XTX, matrix_XTY))
    print(matrix_augmented)
    print()
    print(matrix_augmented[:,-1])


if __name__ == "__main__":
    main()
