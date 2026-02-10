# Overview

This is a Rust Example of the Cleve-Molder precision estimate algorithm.


# Requirements

  - Rust
  - Cargo
  - `hyperfine`

The `hyperfine` utility can be installed using cargo

```
cargo install hyperfine
```

# Compilation

The code can be compiled in debug mode using

```
cargo build
```

or in release (optimized) mode using

```
cargo build --release
```
 

# Sample Execution & Output

The standard `cargo run [--release]` command can by used to run the example.

To run the program directly (i.e., without the overhead of Cargo) use

```
target/debug/fp-error-estimate
```

for debug mode or

```
target/relase/fp-error-estimate
```

for release (optimized) mode.


## Abbreviated Sample Output

```
    1 -> 1.0
    2 -> 5.0e-1
    3 -> 2.5e-1
    4 -> 1.25e-1
    5 -> 6.25e-2
    6 -> 3.12e-2
    7 -> 1.562e-2
    8 -> 7.812e-3
    9 -> 3.906e-3
   10 -> 1.9531e-3
   11 -> 9.7656e-4
   12 -> 4.8828e-4
   13 -> 2.4414e-4
   14 -> 1.22070e-4
   15 -> 6.10352e-5
   16 -> 3.05176e-5
   17 -> 1.525879e-5
   18 -> 7.629395e-6
   19 -> 3.814697e-6
   20 -> 1.9073486e-6
```


