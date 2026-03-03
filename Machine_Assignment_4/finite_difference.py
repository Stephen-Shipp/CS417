"""
Compute an approximate value for the derivative of f(x) = sin(x)
using the finite difference formula:

    f'(x) ≈ (f(x + h) - f(x)) / h

with x = 1 and h = 2^-1, 2^-2, ..., 2^-30.
"""

import math


def compute_step_size(n: int) -> float:
    """Return h = 2^-n."""
    return 2.0 ** (-n)


def approximate_derivative(x: float, h: float) -> float:
    """Compute forward finite difference approximation of sin'(x)."""
    return (math.sin(x + h) - math.sin(x)) / h


def known_derivative(x: float) -> float:
    """Return the exact derivative of sin(x), which is cos(x)."""
    return math.cos(x)


def absolute_error(approx: float, exact: float) -> float:
    """Return the absolute error between the approximation and exact value."""
    return abs(exact - approx)


def format_row(n: int, x: float, approx: float, exact: float, error: float) -> str:
    """Format a single table row."""
    return (
        f"|2^-{n:02d} "
        f"| {x:>13.8f} "
        f"| {approx:>13.8f} "
        f"| {exact:>13.8f} "
        f"| {error:>13.8f} |"
    )


def print_table_header() -> None:
    """Print the Markdown table header."""
    print("|  h   |       x       | Approx. f'(x) |  Known f'(x)  |  Abs. Error   |")
    print("|:----:|--------------:|--------------:|--------------:|--------------:|")


def run_finite_difference(x: float = 1.0, max_n: int = 30) -> None:
    """Run the finite difference computation and print results."""
    exact = known_derivative(x)

    print_table_header()

    for n in range(1, max_n + 1):
        h = compute_step_size(n)
        approx = approximate_derivative(x, h)
        error = absolute_error(approx, exact)
        print(format_row(n, x, approx, exact, error))


def main():
    run_finite_difference()


if __name__ == "__main__":
    main()