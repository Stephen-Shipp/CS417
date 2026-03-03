//! Piecewise Linear Interpolation Module
//!
//! Computes linear interpolation segments for pairs of adjacent data points.
//! Each segment is defined by y = b + m*x where:
//!   - m (slope) = (y_{k+1} - y_k) / (x_{k+1} - x_k)
//!   - b (intercept) = y_k - m * x_k

use crate::preprocess::CoreData;

/// Represents a single linear interpolation segment.
/// Valid for the interval [x_start, x_end].
#[derive(Debug, Clone)]
pub struct InterpolationSegment {
    /// Start of the interval (x_k)
    pub x_start: f64,
    /// End of the interval (x_{k+1})
    pub x_end: f64,
    /// Y-intercept (b in y = b + mx)
    pub intercept: f64,
    /// Slope (m in y = b + mx)
    pub slope: f64,
}

/// Computes the slope between two points.
///
/// # Arguments
/// * `x0` - x-coordinate of first point
/// * `y0` - y-coordinate of first point
/// * `x1` - x-coordinate of second point
/// * `y1` - y-coordinate of second point
///
/// # Returns
/// The slope m = (y1 - y0) / (x1 - x0)
fn compute_slope(x0: f64, y0: f64, x1: f64, y1: f64) -> f64 {
    (y1 - y0) / (x1 - x0)
}

/// Computes the y-intercept given a point and slope.
///
/// # Arguments
/// * `x` - x-coordinate of a point on the line
/// * `y` - y-coordinate of a point on the line
/// * `slope` - the slope of the line
///
/// # Returns
/// The y-intercept b = y - m*x
fn compute_intercept(x: f64, y: f64, slope: f64) -> f64 {
    y - slope * x
}

/// Creates an interpolation segment from two adjacent points.
///
/// # Arguments
/// * `x0` - x-coordinate of first point (interval start)
/// * `y0` - y-coordinate of first point
/// * `x1` - x-coordinate of second point (interval end)
/// * `y1` - y-coordinate of second point
///
/// # Returns
/// An InterpolationSegment valid for [x0, x1]
fn create_segment(x0: f64, y0: f64, x1: f64, y1: f64) -> InterpolationSegment {
    let slope = compute_slope(x0, y0, x1, y1);
    let intercept = compute_intercept(x0, y0, slope);

    InterpolationSegment {
        x_start: x0,
        x_end: x1,
        intercept,
        slope,
    }
}

/// Performs piecewise linear interpolation on core temperature data.
///
/// Given n data points, produces n-1 line segments connecting
/// each pair of adjacent points.
///
/// # Arguments
/// * `core_data` - temperature readings for a single CPU core
///
/// # Returns
/// A vector of InterpolationSegments, one for each pair of adjacent points
pub fn interpolate(core_data: &CoreData) -> Vec<InterpolationSegment> {
    let n = core_data.times.len();

    if n < 2 {
        return Vec::new();
    }

    let mut segments: Vec<InterpolationSegment> = Vec::with_capacity(n - 1);

    for k in 0..(n - 1) {
        let x0 = core_data.times[k];
        let y0 = core_data.temps[k];
        let x1 = core_data.times[k + 1];
        let y1 = core_data.temps[k + 1];

        let segment = create_segment(x0, y0, x1, y1);
        segments.push(segment);
    }

    segments
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_compute_slope() {
        // Points (0, 61) and (30, 80): slope = (80-61)/(30-0) = 19/30 ≈ 0.6333
        let slope = compute_slope(0.0, 61.0, 30.0, 80.0);
        assert!((slope - 0.6333).abs() < 0.001);
    }

    #[test]
    fn test_compute_intercept() {
        // With slope 0.6333 and point (0, 61): intercept = 61 - 0.6333*0 = 61
        let intercept = compute_intercept(0.0, 61.0, 0.6333);
        assert!((intercept - 61.0).abs() < 0.001);
    }

    #[test]
    fn test_create_segment() {
        let seg = create_segment(0.0, 61.0, 30.0, 80.0);
        assert!((seg.x_start - 0.0).abs() < 0.001);
        assert!((seg.x_end - 30.0).abs() < 0.001);
        assert!((seg.intercept - 61.0).abs() < 0.001);
        assert!((seg.slope - 0.6333).abs() < 0.001);
    }

    #[test]
    fn test_interpolate_empty() {
        let core_data = CoreData {
            times: Vec::new(),
            temps: Vec::new(),
        };
        let segments = interpolate(&core_data);
        assert!(segments.is_empty());
    }

    #[test]
    fn test_interpolate_single_point() {
        let core_data = CoreData {
            times: vec![0.0],
            temps: vec![61.0],
        };
        let segments = interpolate(&core_data);
        assert!(segments.is_empty());
    }

    #[test]
    fn test_interpolate_two_points() {
        let core_data = CoreData {
            times: vec![0.0, 30.0],
            temps: vec![61.0, 80.0],
        };
        let segments = interpolate(&core_data);
        assert_eq!(segments.len(), 1);
        assert!((segments[0].slope - 0.6333).abs() < 0.001);
    }
}