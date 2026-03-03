"""
Plot h vs Abs. Error from the finite difference approximation of sin'(x).

Both axes use logarithmic scales. A vertical reference line marks sqrt(eps),
the theoretical optimal step size for the forward difference formula.

Saves the plot as error_plot.png.
"""

from ast import Return
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from finite_difference import compute_step_size, approximate_derivative, known_derivative, absolute_error
from machine_epsilon import cleve_moler_epsilon, sqrt_epsilon


def collect_data(x: float = 1.0, max_n: int = 30):
    #Return (h_values, errors) lists from the finite difference computation.    
    exact = known_derivative(x)
    h_values = []
    errors = []

    for n in range(1, max_n + 1):
        h = compute_step_size(n)
        approx = approximate_derivative(x, h)
        err = absolute_error(approx, exact)
        h_values.append(h)
        errors.append(err)

    return h_values, errors


def plot_error(h_values, errors, sqrt_eps, output_file="error_plot.png"):
    #Generate and save the log-log plot of h vs absolute error.
    fig, ax = plt.subplots(figsize=(9, 6))

    ax.plot(h_values, errors, marker='o', markersize=5,
            linewidth=1.5, color='steelblue', label="Abs. Error")

    # Vertical reference line at sqrt(eps)
    ax.axvline(x=sqrt_eps, color='tomato', linestyle='--', linewidth=1.5,
               label=f"$\\sqrt{{\\epsilon_{{mach}}}}$ ≈ {sqrt_eps:.2e}")

    ax.set_xscale("log")
    ax.set_yscale("log")

    ax.set_xlabel("h  (step size)", fontsize=12)
    ax.set_ylabel("Absolute Error  |f'(x) - approx|", fontsize=12)
    ax.set_title("Finite Difference Approximation of sin'(1)\nAbsolute Error vs Step Size h", fontsize=13)

    ax.legend(fontsize=11)
    ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.7)

    plt.tight_layout()
    plt.savefig(output_file, dpi=150)
    print(f"Plot saved to: {output_file}")


def find_minimum_error(h_values, errors):
    #Return the (h, error) pair where error is smallest.
    min_idx = errors.index(min(errors))
    return h_values[min_idx], errors[min_idx]


def main():
    eps = cleve_moler_epsilon()
    sqrt_eps = sqrt_epsilon(eps)

    h_values, errors = collect_data()
    h_min, err_min = find_minimum_error(h_values, errors)

    print(f"Machine Epsilon (eps):      {eps:.6e}")
    print(f"sqrt(eps):                  {sqrt_eps:.6e}")
    print(f"Minimum absolute error:     {err_min:.6e}  at h = {h_min:.6e}")
    print()

    plot_error(h_values, errors, sqrt_eps)


if __name__ == "__main__":
    main()