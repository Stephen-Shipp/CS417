use clap::Parser;
use colored::Colorize;
use rand::prelude::*;

use addition_order::*;

pub fn perform_addition_1(x: f32, y: f32, z: f32) -> f32 {
    let x_plus_y = x + y;

    x_plus_y + z
}

pub fn perform_addition_2(x: f32, y: f32, z: f32) -> f32 {
    let y_plus_z = y + z;

    x + y_plus_z
}

pub fn perform_addition_3(x: f32, y: f32, z: f32) -> f32 {
    let x_plus_z = x + z;

    x_plus_z + y
}

/// Simple demonstration of floating point error on addition order
#[derive(Parser, Debug)]
#[command(version, about, long_about = None)]
struct Args {
    /// Number of floating point triples to generate
    #[arg(short, long)]
    number: usize,

    /// Tolerance above which floating point values are considered different
    #[arg(short, long, default_value_t = EPS)]
    tolerance: f32,
}

fn main() {
    let args = Args::parse();

    let mut rng = rand::rng();

    println!(
        "|{:^16}|{:^16}|{:^16}|{:^16}|{:^16}|{:^16}|{:^20}|",
        "x", "y", "z", "(x + y) + z", "x + (y + z)", "(x + z) + y", "Difference Found"
    );

    for _ in 0..args.number {
        let (x, y, z) = (
            rng.random::<f32>(),
            rng.random::<f32>(),
            rng.random::<f32>(),
        );

        let result_1 = perform_addition_1(x, y, z);
        let result_2 = perform_addition_2(x, y, z);
        let result_3 = perform_addition_3(x, y, z);

        let results_differ = (result_1, result_2).differ_more_than(args.tolerance)
            || (result_1, result_3).differ_more_than(args.tolerance)
            || (result_2, result_3).differ_more_than(args.tolerance);

        print!("|{x:16.14}|{y:16.14}|{z:16.14}");
        println!(
            "|{}|{}|{}|{:^20}|",
            match first_differs_from(result_1, result_2, result_3, args.tolerance) {
                DiffersFrom::Both => format!("{:16.14}", result_1).bright_cyan().bold(),
                _ => format!("{:16.12}", result_1).dimmed(),
            },
            match first_differs_from(result_2, result_1, result_3, args.tolerance) {
                DiffersFrom::Both => format!("{:16.14}", result_2).bright_cyan().bold(),
                _ => format!("{:16.12}", result_2).dimmed(),
            },
            match first_differs_from(result_3, result_1, result_2, args.tolerance) {
                DiffersFrom::Both => format!("{:16.14}", result_3).bright_cyan().bold(),
                _ => format!("{:16.12}", result_3).dimmed(),
            },
            if results_differ { "Yes" } else { "" }
        );
    }
}
