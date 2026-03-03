//! Output Module
//!
//! Handles formatting and writing interpolation results to files.
//! Output format matches the required specification:
//!   "       0 <= x <=       30 ; y =      61.0000 +       0.6333 x ; interpolation"

use crate::interpolation::InterpolationSegment;
use std::fs::File;
use std::io::{self, Write, BufWriter};
use std::path::Path;

/// Formats a single interpolation segment as a string.
///
/// # Arguments
/// * `segment` - the interpolation segment to format
///
/// # Returns
/// A formatted string matching the required output specification
fn format_segment(segment: &InterpolationSegment) -> String {
    format!(
        "{:>8.0} <= x <= {:>8.0} ; y = {:>12.4} + {:>12.4} x ; interpolation",
        segment.x_start,
        segment.x_end,
        segment.intercept,
        segment.slope
    )
}

/// Formats all segments for a single core.
///
/// # Arguments
/// * `segments` - vector of interpolation segments
///
/// # Returns
/// A vector of formatted strings, one per segment
fn format_all_segments(segments: &[InterpolationSegment]) -> Vec<String> {
    segments.iter().map(format_segment).collect()
}

/// Generates the output filename for a given core.
///
/// # Arguments
/// * `input_filename` - the original input filename
/// * `core_index` - the core number (0-indexed)
///
/// # Returns
/// The output filename in format: "{input_base}-core-{NN}.txt"
pub fn generate_output_filename(input_filename: &str, core_index: usize) -> String {
    // Remove .txt extension if present
    let base = input_filename
        .strip_suffix(".txt")
        .unwrap_or(input_filename);

    format!("{}-core-{:02}.txt", base, core_index)
}

/// Writes interpolation results to a file.
///
/// # Arguments
/// * `filename` - path to the output file
/// * `segments` - vector of interpolation segments to write
///
/// # Returns
/// Ok(()) on success, or an io::Error on failure
pub fn write_to_file(filename: &str, segments: &[InterpolationSegment]) -> io::Result<()> {
    let path = Path::new(filename);
    let file = File::create(path)?;
    let mut writer = BufWriter::new(file);

    let formatted_lines = format_all_segments(segments);

    for line in formatted_lines {
        writeln!(writer, "{}", line)?;
    }

    // Add trailing newline as shown in sample output
    writeln!(writer)?;

    writer.flush()?;
    Ok(())
}

/// Writes interpolation results for all cores.
///
/// # Arguments
/// * `input_filename` - the original input filename (used to generate output names)
/// * `all_segments` - vector of segment vectors, one per core
///
/// # Returns
/// Ok(()) on success, or an io::Error on failure
pub fn write_all_cores(
    input_filename: &str,
    all_segments: &[Vec<InterpolationSegment>],
) -> io::Result<()> {
    for (core_idx, segments) in all_segments.iter().enumerate() {
        let output_filename = generate_output_filename(input_filename, core_idx);
        write_to_file(&output_filename, segments)?;
        println!("Wrote: {}", output_filename);
    }
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_generate_output_filename() {
        assert_eq!(
            generate_output_filename("sample-input.txt", 0),
            "sample-input-core-00.txt"
        );
        assert_eq!(
            generate_output_filename("sample-input.txt", 3),
            "sample-input-core-03.txt"
        );
        assert_eq!(
            generate_output_filename("data", 1),
            "data-core-01.txt"
        );
    }

    #[test]
    fn test_format_segment() {
        let segment = InterpolationSegment {
            x_start: 0.0,
            x_end: 30.0,
            intercept: 61.0,
            slope: 0.6333,
        };
        let formatted = format_segment(&segment);
        assert!(formatted.contains("0 <= x <="));
        assert!(formatted.contains("30"));
        assert!(formatted.contains("interpolation"));
    }
}