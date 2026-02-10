fn sqrt_demo() {
    for power in 0..20 {
        let result = (1_f64 + 10_f64.powf(-power as f64)).sqrt();
        println!(" sqrt(1 + 10^-{power:<2}) = {result:>50.50}");
    }
}

fn main() {
    sqrt_demo();
}
