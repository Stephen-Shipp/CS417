# Requirements

  * Python 3.11 or newer
  * `matplotlib` (for plot generation)

## Testing Requirements

  * `pytest` 7.x or newer
  * `pytest-cov` (optional, for coverage reports)


# Execution

**Compute machine epsilon:**

```
python3 machine_epsilon.py
```

**Generate the error plot:**

```
python3 plot_error.py
```

The plot is saved as `error_plot.png` in the current directory.


# Sample Execution & Output

Running `python3 plot_error.py` produces:

```
Machine Epsilon (eps):      2.220446e-16
sqrt(eps):                  1.490116e-08
Minimum absolute error:     5.455107e-10  at h = 7.450581e-09

Plot saved to: error_plot.png
```


# Findings

## Machine Epsilon

Using the Cleve Moler Algorithm:

```
a ← 4.0 / 3.0
b ← a - 1
c ← b + b + b
eps = |1 - c|
```

The computed value is:

```
eps     = 2.220446e-16  (= 2^-52, IEEE 754 double precision)
sqrt(eps) = 1.490116e-08
```

## Minimum Error Observed

From the log-log plot of h vs absolute error, the minimum absolute error is:

```
Minimum error ≈ 5.455e-10  at h ≈ 7.451e-09
```

## Comparison with sqrt(eps)

The minimum error occurs at `h ≈ 7.45e-09`, which is just below `sqrt(eps) ≈ 1.49e-08`.
This is consistent with theory: the forward difference formula balances two competing
sources of error as h decreases —

  * **Truncation error** decreases as h shrinks (fewer terms dropped from Taylor series)
  * **Rounding error** increases as h shrinks (catastrophic cancellation in `sin(1+h) - sin(1)`)

The crossover point falls near `sqrt(eps)`.
This is the theoretical optimal step size for the forward finite difference formula, and
the graph confirms this prediction closely.

The minimum observed error (`~5.5e-10`) is slightly smaller than `sqrt(eps)` itself
(`~1.49e-08`), which is also expected: the minimum error magnitude is on the order of
`sqrt(eps)`, not exactly equal to it, because the actual crossover depends on the
magnitude of `f(x)` and `f''(x)` at the evaluation point.


# Running Tests

```
./run_tests.sh
```

For additional options:

```
./run_tests.sh coverage    # Run with coverage report
./run_tests.sh quiet       # Minimal output
./run_tests.sh failed      # Rerun only previously failed tests
./run_tests.sh specific    # Run a specific test class
./run_tests.sh help        # Show all options
```

Or directly with pytest:

```
python3 -m pytest test_machine_epsilon.py -v
```