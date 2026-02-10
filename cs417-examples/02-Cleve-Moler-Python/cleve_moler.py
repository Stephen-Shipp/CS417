import math
from decimal import Decimal

D_ONE = Decimal(1.0)


def estimate_precision_float() -> float:
    a = 4.0 / 3.0
    b = a - 1.0
    c = b + b + b

    return math.fabs(c - 1.0)


def estimate_precision_decimal() -> Decimal:
    a = Decimal(4.0) / Decimal(3.0)
    b = a - Decimal(1.0)
    c = b + b + b

    return abs(D_ONE - c)
