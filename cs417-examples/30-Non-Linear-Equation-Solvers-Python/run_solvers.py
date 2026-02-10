#! /usr/bin/env python3

import sys
from fractions import Fraction
from typing import Tuple

from solvers import bisection, newton, print_solution, regula_falsi, secant


def __build_f_df():
    """
    Wrapper function that returns two math style functions:

      - f - a function in the form Real -> Real
      - df - the derivative of f in the form Real -> Real
    """

    # Function (f) and its derivative (dx)
    def f(x):
        # return (x ** 2) - 1
        # return Fraction(math.cos(x))
        # return Fraction(math.log(x)) # can not have negative operand (Real)
        # return x**5 - (7 * x)**2
        return x**2 - 3 * x - 4

    def df(x):
        # return 2 * x
        # return Fraction(-1 * math.sin(x))
        # return Fraction(numerator=1, denominator=x)
        # return 5 * (x ** 4) - (14 * x)
        return 2 * x - 3

    return (f, df)


def __handle_cli_args() -> Tuple[Fraction, Fraction]:
    """
    A wrapper for CLI parsing and usage message logic
    """

    try:
        limit_a = Fraction(sys.argv[1])
        limit_b = Fraction(sys.argv[2])

    except IndexError:
        print("Usage: {0} a b".format(*sys.argv))
        sys.exit(1)

    except ValueError as e:
        print("Arguments 0 and 1 (a and b) must be valid numbers")
        print("  " + str(e))
        sys.exit(2)

    return (limit_a, limit_b)


def main():
    limit_a, limit_b = __handle_cli_args()

    # a = Fraction(-1 * math.pi / 4)
    # b = Fraction(2 * math.pi / 3)

    math_f, math_df = __build_f_df()

    # ---------------------------------------------------------------------------
    # Bisection Method
    # ---------------------------------------------------------------------------
    print("# Bisection")
    print("## Steps")

    try:
        solution_bisection = bisection(math_f, limit_a, limit_b)
        fx_bisection = math_f(solution_bisection)

        print_solution(solution_bisection, fx_bisection)

    except ValueError as err:
        print()
        print("## Method Failed")
        print(str(err))

    # ---------------------------------------------------------------------------
    # Regula Falsi (False Position)
    # ---------------------------------------------------------------------------
    print()
    print("# Regula Falsi (False Position)")
    print("## Steps")

    try:
        solution_regula_falsi = regula_falsi(math_f, limit_a, limit_b)
        fx_regula_falsi = math_f(solution_regula_falsi)

        print_solution(solution_regula_falsi, fx_regula_falsi)

    except ZeroDivisionError as err:
        print()
        print("## Method Failed")
        print(str(err))

    # ---------------------------------------------------------------------------
    # Secant Method
    # ---------------------------------------------------------------------------
    print()
    print("# Secant")
    print("## Steps")

    try:
        solution_secant = secant(math_f, limit_a, limit_b)
        fx_secant = math_f(solution_secant)

        print_solution(solution_secant, fx_secant)

    except ZeroDivisionError as err:
        print()
        print("## Method Failed")
        print(str(err))

    # ---------------------------------------------------------------------------
    # Newton's Method
    # ---------------------------------------------------------------------------
    print()
    print("# Newton")
    print("## Steps")

    try:
        solution_newton = newton(math_f, math_df, limit_a)
        fx_newton = math_f(solution_newton)

        print_solution(solution_newton, fx_newton)

    except ZeroDivisionError as err:
        print()
        print("## Method Failed")
        print(str(err))


if __name__ == "__main__":
    main()
