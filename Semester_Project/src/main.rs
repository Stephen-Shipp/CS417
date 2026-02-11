mod input;
mod preprocess;

fn main() {
    let args: Vec<String> = std::env::args().collect();

    //Handle command line arguments
    if args.len() != 2 {
        eprintln!("Usage: {} <temperature_file>", args[0]);
        std::process::exit(1);
    }

    let filename = &args[1];

    //Read the temperature data from the specified file
    let readings = match input::read_temperature_file(filename) {
        Ok(r) => r,
        Err(e) => {
            eprintln!("Error reading temperature file: {}", e);
            std::process::exit(1);
        }
    };

    let core_data_vec = preprocess::preprocess(&readings);

    //Print the preprocessed data for each core
    for (core_idx, core_data) in core_data_vec.iter().enumerate() {
        println!("Core {}:", core_idx);
        for (time, temp) in core_data.times.iter().zip(core_data.temps.iter()) {
            println!("  Time: {:.2} s, Temp: {:.2} °C", time, temp);
        }  

    }

}
