use num_traits::Float;
use rand::distributions::{Distribution, Uniform};
use rand::prelude::*;

/**
 * Parse command line arguments in the form of tuple.
 *
 * @param argc number of command line arguments
 * @param argv command line arguments to parse
 *
 * @return tuple in the form (error_code, parsed_arg_1, parsed_arg_2) where
 *         error_code is 0 if everything was parsed without issue
 */
/*
fn parse_args(argv: &[&str]) -> (u64, u64, u64)
{
    // Not enough arguments
    if argv.len() < 2 {
        return (0, 0, 0);
    }

    let the_seed = 0; // TODO: Seed the RNG

    if (argv.len() == 3) {
        let the_precision = argv[2].parse().unwrap();

        return (0, the_seed, the_precision);
    }

    return (0, the_seed, 0);
}
*/

fn do_the_work_smarter(lower: f64, upper: f64) {
    let distribution = Uniform::new(lower, upper);
    let mut rng = rand::thread_rng();

    for _ in 0..10 {
        let random_t1: f64 = distribution.sample(&mut rng);
        let t1_as_t2: f32 = random_t1 as f32;

        println!("{random_t1}");
        println!("{t1_as_t2}");
        println!()
    }
}

fn demonstrate_underflow<const NUM_ITERATIONS: u64>() {
    let mut x: f64 = 4.62;

    for i in 0..NUM_ITERATIONS {
        x /= 1000.0;
        println!("i: {i:3} - x: {x:.16e}");
    }
}

fn demonstrate_overflow<const NUM_ITERATIONS: u64>() {
    let mut x: f64 = 4.62;

    for i in 0..NUM_ITERATIONS {
        x *= 1_000_000.0;
        println!("i: {i:3} - x: {x:.16e}");
    }
}

//------------------------------------------------------------------------------
fn main() {
    /*
    const auto [error_code, the_seed, the_precision] = parseArgs(argc, argv);

    if (error_code == 1) {
        std::cerr << "Usage: " << argv[0] << " seed" << "\n";
        return 1;
    }

    srand(the_seed);

    cout.setf(ios::fixed | ios::showpoint);
    cout.precision(the_precision != -1 ? the_precision : 16);

    //--------------------------------------------------------------------------
    cout << "---------------------------------------------------------------\n";
    cout << " Demonstrate \"float\" to \"double\"\n";
    cout << "---------------------------------------------------------------\n";
    doTheWorkSmarter<float, double>();

    */
    println!("{}", "-".repeat(60));
    println!("{:^60}", "Demonstrate \"f64\" to \"f32\"");
    println!("{}", "-".repeat(60));
    do_the_work_smarter(1_f64, 100_f64);

    println!("{}", "-".repeat(60));
    println!("{:^60}", "Demonstrate Underflow");
    println!("{}", "-".repeat(60));
    demonstrate_underflow::<109>();

    println!();
    println!("{}", "-".repeat(60));
    println!("{:^60}", "Demonstrate Overflow");
    println!("{}", "-".repeat(60));
    demonstrate_overflow::<52>();
}
