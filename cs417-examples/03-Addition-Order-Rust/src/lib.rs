pub const EPS: f32 = 1e-12;

pub trait FloatingPointDiffer {
    fn differ_more_than(self, tolerance: f32) -> bool;
}

impl FloatingPointDiffer for (f32, f32) {
    fn differ_more_than(self, tolerance: f32) -> bool {
        (self.0 - self.1).abs() > tolerance
    }
}

pub enum DiffersFrom {
    Neither,
    First,
    Second,
    Both,
}

pub fn first_differs_from(first: f32, second: f32, third: f32, tolerance: f32) -> DiffersFrom {
    match (
        (first, second).differ_more_than(tolerance),
        (first, third).differ_more_than(tolerance),
    ) {
        (false, false) => DiffersFrom::Neither,
        (true, false) => DiffersFrom::First,
        (false, true) => DiffersFrom::Second,
        (true, true) => DiffersFrom::Both,
    }
}
