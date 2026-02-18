"""
Compute machine epsilon using the Cleve Moler Algorithm:

    a ← 4.0 / 3.0
    b ← a - 1
    c ← b + b + b
    eps = |1 - c|

Then compute sqrt(eps) as the expected optimal step size h.
"""

import math


def cleve_moler_epsilon() -> float:
    """Return machine epsilon using the Cleve Moler algorithm."""
    a = 4.0 / 3.0
    b = a - 1.0
    c = b + b + b
    return abs(1.0 - c)


def sqrt_epsilon(eps: float) -> float:
    """Return the square root of machine epsilon."""
    return math.sqrt(eps)


def main():
    eps = cleve_moler_epsilon()
    sqrt_eps = sqrt_epsilon(eps)

    print(f"Machine Epsilon (eps):  {eps:.6e}")
    print(f"sqrt(eps):              {sqrt_eps:.6e}")


if __name__ == "__main__":
    main()