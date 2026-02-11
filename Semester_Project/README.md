# Requirements

  * Rust (rustc) v1.93.0 or newer
  * Cargo v1.93.0 or newer
  * Dependencies (managed via Cargo.toml):
    * `regex` 1.x
    * `thiserror` 2.x


# Compilation

The code can be compiled using Cargo with the standard `cargo build` command.
```
cargo build
```

For an optimized release build:
```
cargo build --release
```


# Sample Execution & Output

If run without command line arguments, using
```
cargo run
```

the following usage message will be displayed.
```
Usage: Semester_Project <temperature_file>
```

If run using
```
cargo run -- sample-input.txt
```

output similar to
```
Core 0:
  Time: 0.00 s, Temp: 61.00 °C
  Time: 30.00 s, Temp: 80.00 °C
  Time: 60.00 s, Temp: 62.00 °C
  Time: 90.00 s, Temp: 83.00 °C
  Time: 120.00 s, Temp: 68.00 °C
Core 1:
  Time: 0.00 s, Temp: 63.00 °C
  Time: 30.00 s, Temp: 81.00 °C
  Time: 60.00 s, Temp: 63.00 °C
  Time: 90.00 s, Temp: 82.00 °C
  Time: 120.00 s, Temp: 69.00 °C
Core 2:
  Time: 0.00 s, Temp: 50.00 °C
  Time: 30.00 s, Temp: 68.00 °C
  Time: 60.00 s, Temp: 52.00 °C
  Time: 90.00 s, Temp: 70.00 °C
  Time: 120.00 s, Temp: 58.00 °C
Core 3:
  Time: 0.00 s, Temp: 58.00 °C
  Time: 30.00 s, Temp: 77.00 °C
  Time: 60.00 s, Temp: 60.00 °C
  Time: 90.00 s, Temp: 79.00 °C
  Time: 120.00 s, Temp: 65.00 °C
```

will be displayed.