fn approach_zero<F>(f: F)
where
    F: Fn(f64) -> f64,
{
    for i in 0..2000 {
        let x = 2_f64.powf(-i as f64);
        let f_of_x = f(x);

        println!("2^-{} / {:>24.20e} | {:>24.20e}", i, x, f_of_x);
    }
}

fn g(x: f64) -> f64 {
    x.powf(3_f64) + 7_f64
}

fn main() {
    // approach_zero(|x: f64| x.powf(2_f64) + 3_f64 * x)
    approach_zero(g);
}
