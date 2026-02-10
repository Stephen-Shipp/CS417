use rug::Float;

fn cleve_moler(desired_precision: u32) -> Float {
    let a = Float::with_val(desired_precision, 4.0) / Float::with_val(desired_precision, 3.0);

    let b = a - Float::with_val(desired_precision, 1.0);
    let c = Float::with_val(desired_precision, &b + &b) + &b;

    let one = Float::with_val(desired_precision, 1.0);

    (c - one).abs()
}

fn main() {
    for precision in 1..=1000 {
        println!("{:>5} -> {}", precision, cleve_moler(precision));
    }
}
