//! Semester Project - CPU Temperature Analysis
//!
//! Reads temperature data and performs piecewise linear interpolation
//! for each CPU core, outputting results to separate files.

mod input;
mod interpolation;
mod output;
mod preprocess;

use std::env;
use std::process;

/// Prints usage information and exits.
fn print_usage_and_exit(program_name: &str) -> ! {
    eprintln!("Usage: {} <temperature_file>", program_name);
    process::exit(1);
}

/// Parses command line arguments and returns the input filename.
fn parse_args() -> String {
    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        print_usage_and_exit(&args[0]);
    }

    args[1].clone()
}

/// Reads and parses the temperature file.
fn read_input_file(filename: &str) -> Vec<input::TemperatureLine> {
    match input::read_temperature_file(filename) {
        Ok(readings) => readings,
        Err(e) => {
            eprintln!("Error reading temperature file: {}", e);
            process::exit(1);
        }
    }
}

/// Performs interpolation on all cores.
fn interpolate_all_cores(
    core_data_vec: &[preprocess::CoreData],
) -> Vec<Vec<interpolation::InterpolationSegment>> {
    core_data_vec
        .iter()
        .map(|core_data| interpolation::interpolate(core_data))
        .collect()
}

fn main() {
    // Parse command line arguments
    let filename = parse_args();

    // Read and parse the input file
    let readings = read_input_file(&filename);

    // Preprocess: transform to per-core data
    let core_data_vec = preprocess::preprocess(&readings);

    // Perform piecewise linear interpolation for each core
    let all_segments = interpolate_all_cores(&core_data_vec);

    // Write results to output files
    if let Err(e) = output::write_all_cores(&filename, &all_segments) {
        eprintln!("Error writing output files: {}", e);
        process::exit(1);
    }
}
