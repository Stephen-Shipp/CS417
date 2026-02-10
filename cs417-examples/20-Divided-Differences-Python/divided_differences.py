#! /usr/bin/env python3

import copy
import logging
import sys
from typing import Generator, TextIO


def read_input_points(open_file: TextIO) -> Generator[tuple[float, float], None, None]:
    """
    TBW

    Args:
        open_file

    Yields:
        TBW
    """

    for line in open_file:
        x, y = [float(val) for val in line.strip().split()][:2]
        yield (x, y)


def algorithm_31(x_values: list[float], fx_values: list[float]) -> list[list[float]]:
    """
    TBW

    Args:
        x_values:
        fx_values:

    Returns:
        TBW
    """

    for _ in range(0, 1):
        for _ in range(0, 1):
            pass


def algorithm_32(x_values: list[float], fx_values: list[float]) -> list[float]:
    """
    TBW

    Args:
        x_values:
        fx_values:

    Returns:
        TBW
    """
    num_points = len(x_values)

    # Option 1
    #  d_i = []
    #  for i in range(0, n):
    #      d_i.append(fx_values[i])

    # Option 2
    #  d_i_values = [f_of_x_i for f_of_x_i in fx_values]

    # Option 3
    d_i_buffer = copy.deepcopy(fx_values)

    n = num_points - 1

    logging.debug("-" * 80)
    logging.debug(d_i_buffer)
    d_i_out = [fx_values[0]]

    for k in range(1, n + 1):
        for i in range(0, n - k + 1):
            logging.debug(f"i = {i:} | k = {k:} | {i+k} -> ")
            logging.debug(
                f"({d_i_buffer[i + 1]} - {d_i_buffer[i]}) / ({x_values[i + k]} - {x_values[i]})"
            )
            d_i_buffer[i] = (d_i_buffer[i + 1] - d_i_buffer[i]) / (
                x_values[i + k] - x_values[i]
            )
            logging.debug(f"{d_i_buffer[i]=}")

            logging.debug(d_i_buffer)

        d_i_out.append(d_i_buffer[0])

    return d_i_out


def main():
    """
    This main function serves as the driver for the demo. Such functions
    are not required in Python. However, we want to prevent unnecessary module
    level (i.e., global) variables.
    """

    logging.basicConfig(level=logging.DEBUG)

    filename = sys.argv[1]

    all_xs = []  # All x values
    all_fs = []  # All y/ f(x) values

    with open(filename, "r") as points_file:
        for point in read_input_points(points_file):
            logging.debug(point)
            all_xs.append(point[0])
            all_fs.append(point[1])

    logging.debug("-" * 80)
    logging.debug(all_xs)
    logging.debug(all_fs)

    algorithm_31(all_xs, all_fs)

    d_i_values = algorithm_32(all_xs, all_fs)

    logging.debug("-" * 80)
    logging.debug(d_i_values)


if __name__ == "__main__":
    main()
