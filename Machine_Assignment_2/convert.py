#!/usr/bin/env python3
import sys

MAX_DIGITS = 8


def integer_to_base(n, base):
    """
    Convert a positive integer to representation in given base.
    Returns a string of digits separated by semicolons.
    """
    if n == 0:
        return "0"
    
    digits = []
    
    while n > 0:
        remainder = n % base
        digits.append(str(remainder))
        n = n // base
    
    # Digits come out in reverse order, so flip them
    digits.reverse()
    
    return ";".join(digits)


def fraction_to_base(x, base):
    """
    Convert a decimal fraction (0 < x < 1) to representation in given base.
    Returns a string of digits separated by semicolons.
    May end with '...' if truncated.
    """
    digits = []
    c = x
    
    for i in range(MAX_DIGITS):
        c = c * base
        digit = int(c)
        digits.append(str(digit))
        c = c - digit
        
        if c == 0:
            break
    
    result = ";".join(digits)
    
    if c != 0:
        result = result + "..."
    
    return result


def decimal_to_base(x, base):
    """
    Convert any decimal number to representation in given base.
    Handles negative numbers and numbers >= 1.
    Returns a string like "1;0;1.1;0;1" or "-0.1;1"
    """
    # Handle negative numbers
    if x < 0:
        return "-" + decimal_to_base(-x, base)
    
    # Split into integer and fractional parts
    int_part = int(x)
    frac_part = x - int_part
    
    # Convert each part
    int_str = integer_to_base(int_part, base)
    
    # If there's no fractional part, just return the integer
    if frac_part == 0:
        return int_str
    
    frac_str = fraction_to_base(frac_part, base)
    
    return int_str + "." + frac_str


def convert(x, base):
    """
    Main conversion function.
    """
    return decimal_to_base(x, base)


def main():
    # First argument is the base, rest are numbers to convert
    base = int(sys.argv[1])
    inputs = sys.argv[2:]
    
    # Convert all inputs first so we can calculate column widths
    results = []
    for arg in inputs:
        decimal_value = float(arg)
        converted_value = convert(decimal_value, base)
        results.append((arg, converted_value))
    
    # Calculate column widths (minimum width for headers)
    base_header = f"Base {base}"
    col1_width = max(len("Base 10"), max(len(r[0]) for r in results))
    col2_width = max(len(base_header), max(len(r[1]) for r in results))
    
    # Print header
    print(f"| {'Base 10':<{col1_width}} | {base_header:<{col2_width}} |")
    print(f"| {':':-<{col1_width}} | {':':-<{col2_width}} |")
    
    # Print data rows
    for decimal_str, converted_str in results:
        print(f"| {decimal_str:<{col1_width}} | {converted_str:<{col2_width}} |")


if __name__ == "__main__":
    main()