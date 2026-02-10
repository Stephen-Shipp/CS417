use regex::Regex;
use std::cell::LazyCell;
use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

use thiserror::Error;

#[derive(Debug)]
pub struct TemperatureLine {
    pub time_step: u64,
    pub readings: Vec<f64>,
}

#[derive(Debug, Error)]
pub enum ParseError {
    #[error(transparent)]
    IOError(#[from] std::io::Error),
}

//------------------------------------------------------------------------------
const TIME_STEP_SIZE: u64 = 30;

const LINE_DELIM_RE: LazyCell<Regex> =
    LazyCell::new(|| Regex::new(r"[^0-9]*\s+|[^0-9]*$").unwrap());

pub fn read_temperature_file(filename: &str) -> Result<Vec<TemperatureLine>, ParseError> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    read_temperatures(reader)
}

pub fn read_temperatures<R>(reader: R) -> Result<Vec<TemperatureLine>, ParseError>
where
    R: BufRead,
{
    let mut readings: Vec<TemperatureLine> = Vec::new();

    for (idx, wrapped_line) in reader.lines().enumerate() {
        let line = wrapped_line?;
        let time = (idx as u64) * TIME_STEP_SIZE;

        let core_temps: Vec<f64> = LINE_DELIM_RE
            .split(line.trim())
            .into_iter()
            .filter_map(|s| s.parse().ok())
            .collect();

        let new_reading = TemperatureLine {
            time_step: time,
            readings: core_temps,
        };

        readings.push(new_reading);
    }

    Ok(readings)
}
