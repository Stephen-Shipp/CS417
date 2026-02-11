# Decimal to Binary Converter

Converts decimal numbers (base 10) to binary (base 2) using the multiplication
algorithm discussed in Chapter 1.

## Requirements

  * Python 3.6+

> This code makes use of the `f"..."` or [f-string
> syntax](https://www.python.org/dev/peps/pep-0498/). This syntax was
> introduced in Python 3.6.


## Sample Execution & Output

The program accepts one or more decimal numbers as command line arguments:

```
python3 convert.py 0.5 0.25 0.75
```

This will generate the following output:

```
| Base 10 | Base 2 |
| :------ | :----- |
| 0.5     | 0.1    |
| 0.25    | 0.01   |
| 0.75    | 0.11   |
```

---

Numbers that do not have a finite binary representation will be truncated
at `MAX_DIGITS` (default: 8) with `...` appended to indicate truncation:

```
python3 convert.py 0.1 0.2 0.3
```

will generate:

```
| Base 10 | Base 2        |
| :------ | :------------ |
| 0.1     | 0.00011001... |
| 0.2     | 0.00110011... |
| 0.3     | 0.01001100... |
```


## Running Tests

Unit tests are provided using pytest. To run the test suite:

```
python3 -m pytest test_convert.py -v
```

Alternatively, a convenience script is provided:

```
./run_tests.sh
```

> Note: pytest must be installed to run tests. Install with:
> `pip3 install pytest`