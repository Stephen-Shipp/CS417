"""
Collection of instrumented nonlinear solvers for CS 417/517 lecture examples.
"""

from fractions import Fraction
from typing import Callable

EPSILON = 10e-6
MAX_ITERATIONS = 100
ONE_HALF = Fraction.from_float(0.5)


def __get_printable_fraction(fraction: Fraction, digit_limit: int = 8) -> str:
    """
    Generate a printable fraction in the form:
    \\frac{numerator}{denominator} (.6f)

    If either the numerator or denominator contains more than
    the allowed number of digits omit the fractional part

    :param fraction: fraction to format
    :param digit_limit: maximum number of digits allowed in numerator or
        denominator
    """

    fmt_str = "$\\frac{{{f.numerator}}}{{{f.denominator}}}={:.6f}$"

    if len(str(fraction.numerator)) > digit_limit or fraction.denominator == 1:

        return "${:.6f}$".format(float(fraction))

    return fmt_str.format(float(fraction), f=fraction)


def print_solution(solution: Fraction, fx_solution) -> None:
    """
    Print the solution (x) and f(x) under a subsection heading.

    :param solution: approximate solution
    :param fx_solution: f(solution)
    """

    print()
    print("## Solution")
    print("$x=" + __get_printable_fraction(solution)[1:])
    print()
    print("$f(x)=" + __get_printable_fraction(fx_solution)[1:])
    print()


def bisection(f: Callable[[Fraction], Fraction],
              a: Fraction,
              b: Fraction) -> Fraction:
    """
    Compute a solution to f using the bisection method

    a0 = a
    b0 = b

    for n = 1, 2, ... do
    xn = 0.5 (a_{n-1} + b_{n-1});
        if f(xn) < 0 then
            an = xn, bn = bn-1
        end if;

        if f(xn) > 0 then
            an = an-1, bn = xn
        end if;

        if bn - an < eps then
            break;
        end if;

    end for
    """

    fmt_str_header = "|{:^4}|{:^16}|{:^16}|{:^16}|{:^20}|"
    fmt_str_row = "|{:4d}|{:>16}|{:>16}|{:>16}|{:>20}|"

    table_headers = ("n", "$a_n$", "$b_n$", "$x_n$", "$f(x_n)$")

    a_n = Fraction(a)
    b_n = Fraction(b)

    print(fmt_str_header.format(*table_headers))
    print("|---:|"
          + ("-" * 15 + ":|") * 3
          + ("-" * 19 + ":|"))
    print(fmt_str_row.format(0,
                             __get_printable_fraction(a_n),
                             __get_printable_fraction(b_n),
                             "", ""))

    for n in range(1, MAX_ITERATIONS):
        x_n = ONE_HALF * (a_n + b_n)

        if f(b_n) < 0:
            raise ValueError("$f(b_{}) < 0$ - Invariant violated!".format(n-1))

        if f(x_n) < 0:
            a_n = x_n
            # b_n = b_n-1 # unchanged

        if f(x_n) >= 0:
            # a_n = a_n-1 # unchanged
            b_n = x_n

        print(fmt_str_row.format(n,
                                 __get_printable_fraction(a_n),
                                 __get_printable_fraction(b_n),
                                 __get_printable_fraction(x_n),
                                 __get_printable_fraction(f(x_n))))

        # Stop Condition
        if abs(b_n - a_n) < EPSILON:
            break

    return x_n


def regula_falsi(f: Callable[[Fraction], Fraction],
                 a: Fraction,
                 b: Fraction) -> Fraction:
    """
    Compute a solution to f using the false position method

    a0 = a
    b0 = b;

    for n = 1, 2, ... do
        xn = an - ((an - bn)/(f(an) - f(bn)))f(an);

        if f(xn) · f(an) > 0 then
            an+1 = xn, bn+1 = bn
        else
            an+1 = an, bn+1 = xn
        end if
    end for
    """

    fmt_str_header = "|{:^4}|{:^16}|{:^16}|{:^16}|{:^20}|"
    fmt_str_row = "|{:4d}|{:>16}|{:>16}|{:>16}|{:>20}|"

    table_headers = ("n", "$a_n$", "$b_n$", "$x_n$", "$f(x_n)$")

    a_n = Fraction(a)
    b_n = Fraction(b)

    print(fmt_str_header.format(*table_headers))
    print("|---:|"
          + ("-" * 15 + ":|") * 3
          + ("-" * 19 + ":|"))
    print(fmt_str_row.format(0, __get_printable_fraction(a_n),
                             __get_printable_fraction(b_n), "", ""))

    for n in range(1, MAX_ITERATIONS):
        try:
            x_n = a_n - ((a_n - b_n) / (f(a_n) - f(b_n))) * f(a_n)

        except ZeroDivisionError:
            err_fmt_str = "$x_n=\\frac{{{a_n}-{b_n}}}{{{}-{}}}*{}$"
            err_str = err_fmt_str.format(f(a_n), f(b_n), f(a_n),
                                         a_n=a_n,
                                         b_n=b_n)

            raise ZeroDivisionError(err_str + " Division by Zero")

        if f(x_n) * f(a_n) > 0:
            a_n = x_n
            # b_n - No change
        else:
            # a_n - No Change
            b_n = x_n

        print(fmt_str_row.format(n,
                                 __get_printable_fraction(a_n),
                                 __get_printable_fraction(b_n),
                                 __get_printable_fraction(x_n),
                                 __get_printable_fraction(f(x_n))))

        if abs(b_n - a_n) < EPSILON:
            break

    return x_n


def secant(f: Callable[[Fraction], Fraction],
           x_n_minus_1: Fraction,
           x_n: Fraction) -> Fraction:
    """
    Compute a solution to f using the secant method

    x_{n-1} = a0 = a
    x_n = b0 = b;

    for n = 1, 2, ... do
        xn = xn - ((xn - x_n-1)/(f(xn) - f(x_n-1)))f(xn);

        if f(xn) · f(an) > 0 then
            an+1 = xn, bn+1 = bn
        else
            an+1 = an, bn+1 = xn
        end if
    end for
    """

    fmt_str_header = "|{:^4}|{:^16}|{:^16}|{:^16}|{:^20}|"
    fmt_str_row = "|{:4d}|{:>16}|{:>16}|{:>16}|{:>20}|"

    table_headers = ("n", "$x_{n-1}$", "$x_n$", "$x_{n+1}$", "$f(x_{n+1})$")

    x_n_minus_1 = Fraction(x_n_minus_1)
    x_n = Fraction(x_n)

    print(fmt_str_header.format(*table_headers))
    print("|---:|"
          + ("-" * 15 + ":|") * 3
          + ("-" * 19 + ":|"))
    print(fmt_str_row.format(1,
                             __get_printable_fraction(x_n_minus_1),
                             __get_printable_fraction(x_n), "", ""))

    for n in range(2, MAX_ITERATIONS):
        try:
            next_x_n = x_n - ((x_n - x_n_minus_1)
                              / (f(x_n) - f(x_n_minus_1))) * f(x_n)

        except ZeroDivisionError:
            err_fmt_str = "$x_n=\\frac{{{x_n}-{x_nm1}}}{{{}-{}}}*{}$"
            err_str = err_fmt_str.format(f(x_n),
                                         f(x_n_minus_1),
                                         f(x_n),
                                         x_n=x_n,
                                         x_nm1=x_n_minus_1)
            raise ZeroDivisionError(err_str + " Division by Zero")

        print(fmt_str_row.format(n,
                                 __get_printable_fraction(x_n),
                                 __get_printable_fraction(x_n_minus_1),
                                 __get_printable_fraction(next_x_n),
                                 __get_printable_fraction(f(next_x_n))))

        x_n_minus_1 = x_n
        x_n = next_x_n

        if abs(x_n - x_n_minus_1) < EPSILON:
            break

    return x_n


def newton(f: Callable[[Fraction], Fraction],
           df: Callable[[Fraction, Fraction], Fraction],
           x_n: Fraction) -> Fraction:
    """
    Compute a solution to f using Newton's method.

    Compute x_{n+1} = x_n - (f(x_n) / df(x_n)) until
    |x_{n+1} - x_n| <= eps
    """

    fmt_str_header = "|{:^4}|{:^16}|{:^16}|{:^16}|{:^20}|"
    fmt_str_row = "|{:4d}|{:>16}|{:>16}|{:>16}|{:>20}|"

    table_headers = ("n", "$x_{n-1}$",
                     "$f(x_{n-1})$", "$f'(x_{n-1})$", "$x_{n+1}$")

    print(fmt_str_header.format(*table_headers))
    print("|---:|"
          + ("-" * 15 + ":|") * 3
          + ("-" * 19 + ":|"))

    x_n = Fraction(x_n)

    for n in range(1, MAX_ITERATIONS):
        next_x_n = x_n - (f(x_n) / df(x_n))

        print(fmt_str_row.format(n,
                                 __get_printable_fraction(x_n),
                                 __get_printable_fraction(f(x_n)),
                                 __get_printable_fraction(df(x_n)),
                                 __get_printable_fraction(next_x_n)))

        if abs(x_n - next_x_n) < EPSILON:
            break

        x_n = next_x_n

    return x_n
