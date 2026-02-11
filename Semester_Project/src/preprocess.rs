use crate::input::TemperatureLine;

/// Holds time and temperature data for a single CPU core.
pub struct CoreData {
    pub times: Vec<f64>,
    pub temps: Vec<f64>,
}

/// Takes raw temperature readings and splits them into per-core data.
///
/// # Arguments
/// * `readings` - parsed temperature lines from the input library
///
/// # Returns
/// A Vec of CoreData, one entry per CPU core
pub fn preprocess(readings: &[TemperatureLine]) -> Vec<CoreData> {
    //Get the number of cores from the first reading (assuming all readings have the same number of cores)
    let num_cores = if readings.is_empty() { 0 } else { readings[0].readings.len() };

    //Initailize a Vec of CoreData with empty vectors for each core
    let mut core_data_vec: Vec<CoreData> = Vec::with_capacity(num_cores);
    for _ in 0..num_cores {
        core_data_vec.push(CoreData {
            times: Vec::new(),
            temps: Vec::new(),
        });
    }

    // TODO: loop through readings and populate each CoreData with the corresponding time and temperature data
    for reading in readings {
        for (core_idx, temp) in reading.readings.iter().enumerate() {
            core_data_vec[core_idx].times.push(reading.time_step as f64);
            core_data_vec[core_idx].temps.push(*temp);
        }
    }

    core_data_vec
}
