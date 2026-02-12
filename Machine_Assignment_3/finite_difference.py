import math
"""
Compute an approximate value for the derivative of f(x) = sin(x)
using the finite difference formula:

    f'(x) ≈ (f(x + h) - f(x)) / h

with x = 1 and h = 2^-1, 2^-2, ..., 2^-30.
"""

def main():
    x = 1.0
    known_derivative = math.cos(x)

    # Header
    print(f"|  h   |       x       | Approx. f'(x) |  Known f'(x)  |  Abs. Error   |")
    print(f"|:----:|--------------:|--------------:|--------------:|--------------:|")

    for n in range(1, 31):
        h = 2.0 ** (-n)

        approx_derivative = (math.sin(x + h) - math.sin(x)) / h
        abs_error = abs(known_derivative - approx_derivative)

        print(
            f"|2^-{n:02d} "
            f"| {x:>13.8f} "
            f"| {approx_derivative:>13.8f} "
            f"| {known_derivative:>13.8f} "
            f"| {abs_error:>13.8f} |"
        )


if __name__ == "__main__":
    main()