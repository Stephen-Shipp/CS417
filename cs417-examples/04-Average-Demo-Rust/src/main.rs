/// Compute a naive average.
fn compute_avg_naive(to_avg: &[f64]) -> f64 {
    to_avg.iter().sum::<f64>() / (to_avg.len() as f64)
}

/// Compute a stable mean (running average)
fn compute_running_avg(to_avg: &[f64]) -> f64 {
    let mut x_bar = to_avg[0];

    for (i, x_i) in to_avg.iter().enumerate().skip(1) {
        x_bar += (x_i - x_bar) / (i + 1) as f64
    }
    x_bar
}

fn main() {
    let argv: Vec<String> = std::env::args().collect();

    let half_length = if argv.len() > 1 {
        argv[1].parse().unwrap()
    } else {
        50_000_usize
    };

    let mut numbers = [1_000_000_000.1_f64, 1.1_f64].repeat(half_length);

    let naive_avg = compute_avg_naive(&numbers);
    let stable = compute_running_avg(&numbers);

    numbers.sort_by(|lhs, rhs| lhs.partial_cmp(rhs).unwrap());
    let sorted_avg_asc = compute_avg_naive(&numbers);
    let sorted_stable_asc = compute_running_avg(&numbers);

    numbers.reverse();
    let sorted_avg_dsc = compute_avg_naive(&numbers);
    let sorted_stable_dsc = compute_running_avg(&numbers);

    println!("Naive Avg.              : {naive_avg:>.20}");
    println!("Sorted Avg. (ascending) : {sorted_avg_asc:>.20}");
    println!("Sorted Avg. (descending): {sorted_avg_dsc:>.21}");

    println!("Stable Avg.             : {stable:>.20}");
    println!("Stable Avg. (ascending) : {sorted_stable_asc:>.20}");
    println!("Stable Avg. (descending): {sorted_stable_dsc:>.20}");
}
