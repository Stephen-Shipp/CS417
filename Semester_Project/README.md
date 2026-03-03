# CS 417 Semester Project - Part 3

## Description

Processes CPU core temperature data from input files and performs piecewise
linear interpolation for each core. Given n data points, the program computes
n-1 line segments connecting each pair of adjacent points.

For each pair of adjacent points (x_k, y_k) and (x_{k+1}, y_{k+1}):
- Slope: m = (y_{k+1} - y_k) / (x_{k+1} - x_k)  
- Intercept: b = y_k - m * x_k

Each segment is valid for the interval [x_k, x_{k+1}].


## Requirements

  * Rust (rustc) 1.80.0 or newer
  * Cargo 1.80.0 or newer
  * Dependencies (managed via Cargo.toml):
    * `regex` 1.x
    * `thiserror` 2.x


## Project Structure

```
semester_project/
├── Cargo.toml
├── README.md
├── sample-input.txt
└── src/
    ├── main.rs           # Driver / entry point
    ├── input.rs          # Provided input library
    ├── preprocess.rs     # Data preprocessing (row to column transform)
    ├── interpolation.rs  # Piecewise linear interpolation
    └── output.rs         # File output formatting
```


## Compilation

The code can be compiled using Cargo with the standard `cargo build` command.

```
cargo build
```

For an optimized release build:

```
cargo build --release
```


## Sample Execution & Output

If run without command line arguments, using

```
cargo run
```

the following usage message will be displayed.

```
Usage: semester_project <temperature_file>
```

If run using

```
cargo run -- sample-input.txt
```

the program will generate four output files (one per CPU core):

```
Wrote: sample-input-core-00.txt
Wrote: sample-input-core-01.txt
Wrote: sample-input-core-02.txt
Wrote: sample-input-core-03.txt
```


### sample-input-core-00.txt

```
       0 <= x <=       30 ; y =      61.0000 +       0.6333 x ; interpolation
      30 <= x <=       60 ; y =      98.0000 +      -0.6000 x ; interpolation
      60 <= x <=       90 ; y =      20.0000 +       0.7000 x ; interpolation
      90 <= x <=      120 ; y =     128.0000 +      -0.5000 x ; interpolation

```


### sample-input-core-01.txt

```
       0 <= x <=       30 ; y =      63.0000 +       0.6000 x ; interpolation
      30 <= x <=       60 ; y =      99.0000 +      -0.6000 x ; interpolation
      60 <= x <=       90 ; y =      25.0000 +       0.6333 x ; interpolation
      90 <= x <=      120 ; y =     121.0000 +      -0.4333 x ; interpolation

```


### sample-input-core-02.txt

```
       0 <= x <=       30 ; y =      50.0000 +       0.6000 x ; interpolation
      30 <= x <=       60 ; y =      84.0000 +      -0.5333 x ; interpolation
      60 <= x <=       90 ; y =      16.0000 +       0.6000 x ; interpolation
      90 <= x <=      120 ; y =     106.0000 +      -0.4000 x ; interpolation

```


### sample-input-core-03.txt

```
       0 <= x <=       30 ; y =      58.0000 +       0.6333 x ; interpolation
      30 <= x <=       60 ; y =      94.0000 +      -0.5667 x ; interpolation
      60 <= x <=       90 ; y =      22.0000 +       0.6333 x ; interpolation
      90 <= x <=      120 ; y =     121.0000 +      -0.4667 x ; interpolation

```


## Running Tests

Unit tests are included in the interpolation and output modules.

```
cargo test
```