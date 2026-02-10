use rand::prelude::*;
use rayon::prelude::*;
use std::env;
use clap::Parser;

struct Point(f64, f64);

/// Generate a sequence of random x values and plug them into f(x).
///
/// Args:
///     f: mathematical function
///     lower_limit: 'a' the lower bound
///     upper_bound: 'b' the upper bound
///     n: number of points to generate
///
/// Yields:
///     A sequence of points in the form (x, f(x))
fn generate_random_points(
    f: fn(f64) -> f64,
    lower_limit: f64,
    upper_limit: f64,
    n: u64,
) -> Vec<Point> {
    let d = rand::distributions::Uniform::new_inclusive(lower_limit, upper_limit);
    let mut rng = thread_rng();

    (0..n)
        .map(|_| {
            let x = rng.sample(d);
            Point(x, f(x))
        })
        .collect()
}

#[derive(Parser)]
pub struct Args {
    #[allow(unused)]
    unused: String,

    /// lower limit
    limit_a: f64,

    /// upper limit
    limit_b: f64,

    /// maximum magnitude
    max_magnitude: u32,
}

/// This main demonstrates the impact of the number of points on Monte Carlo
/// integration
fn main() {
    let args = Args::parse();
    let (limit_a, limit_b, max_magnitude) = (args.limit_a, args.limit_b, args.max_magnitude);

    let math_f = |x: f64| x.powf(2_f64);

    println!("| {:^16} | {:^20} |", "# Points", "Est. f(x)");

    let max_num_points: u64 = 2_u64.pow(max_magnitude);
    let point_sequence = generate_random_points(math_f, limit_a, limit_b, max_num_points);

    for magnitude in 0..=max_magnitude {
        let num_points = 2_u64.pow(magnitude);

        let sum_of_f_of_x_values: f64 = point_sequence
            .par_iter()
            .map(|point| point.1)
            .take(num_points as usize)
            .sum();

        let integral_result = (limit_b - limit_a) / (num_points as f64) * sum_of_f_of_x_values;

        println!("| {:>16} | {:^20.8} |", num_points, integral_result);
    }
}
