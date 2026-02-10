import sys


def compute_avg_naive(to_avg: list[float]) -> float:
    """
    Compute a naive average.
    """

    return sum(to_avg) / len(to_avg)


def compute_running_avg(to_avg: list[float]) -> float:
    """
    Compute a stable mean (running average)
    """

    x_bar = to_avg[0]

    for i, x_i in enumerate(to_avg[1:], start=1):
        x_bar += (x_i - x_bar) / (i + 1)

    return x_bar


def main():
    half_length = 50000
    if len(sys.argv) > 1:
        half_length = int(sys.argv[1]) // 2

    numbers = [1_000_000_000.1, 1.1] * half_length

    naive_avg = compute_avg_naive(numbers)
    sorted_avg_asc = compute_avg_naive(list(sorted(numbers)))
    sorted_avg_dsc = compute_avg_naive(list(sorted(numbers, reverse=True)))

    print(f"Naive Avg.              : {naive_avg:>.20f}")
    print(f"Sorted Avg. (ascending) : {sorted_avg_asc:>.20f}")
    print(f"Sorted Avg. (descending): {sorted_avg_dsc:>.20f}")

    stable = compute_running_avg(numbers)
    sorted_stable_asc = compute_running_avg(list(sorted(numbers)))
    sorted_stable_dsc = compute_running_avg(list(sorted(numbers, reverse=True)))

    print(f"Stable Avg.             : {stable:>.20f}")
    print(f"Stable Avg. (ascending) : {sorted_stable_asc:>.20f}")
    print(f"Stable Avg. (descending): {sorted_stable_dsc:>.20f}")


if __name__ == "__main__":
    main()
