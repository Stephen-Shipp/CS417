import sys

MAX_DIGITS = 8


def decimal_to_binary_fraction(x):
    """
    Convert a decimal fraction (0 < x < 1) to binary representation.
    Returns a string like "0.101" or "0.00110011..."
    """
    digits = []
    c = x
    
    for i in range(MAX_DIGITS):
        c = c * 2
        digit = int(c)
        digits.append(str(digit))
        c = c - digit
        
        if c == 0:
            break
    
    result = "0." + "".join(digits)
    
    if c != 0:
        result = result + "..."
    
    return result


def convert(x):
    """
    Handle all cases: 0, 1, and everything in between.
    """
    if x == 0:
        return "0"
    elif x == 1:
        return "1"
    else:
        return decimal_to_binary_fraction(x)


def main():
    inputs = sys.argv[1:]
    
    # Convert all inputs first so we can calculate column widths
    results = []
    for arg in inputs:
        decimal_value = float(arg)
        binary_value = convert(decimal_value)
        results.append((arg, binary_value))
    
    # Calculate column widths (minimum width for headers)
    col1_width = max(len("Base 10"), max(len(r[0]) for r in results))
    col2_width = max(len("Base 2"), max(len(r[1]) for r in results))
    
    # Print header
    print(f"| {'Base 10':<{col1_width}} | {'Base 2':<{col2_width}} |")
    print(f"| {':':-<{col1_width}} | {':':-<{col2_width}} |")
    
    # Print data rows
    for decimal_str, binary_str in results:
        print(f"| {decimal_str:<{col1_width}} | {binary_str:<{col2_width}} |")


if __name__ == "__main__":
    main()