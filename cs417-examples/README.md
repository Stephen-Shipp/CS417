# Overview

This repository is a collection of code examples for CS 417/517.


# Working with the Example Code

The contents of this repo can be downloaded as a zip file (using the download
button). In general, cloning the repo using

```
git clone https://github.com/cstkennedy/cs417-examples.git
```

is the better option. Cloning the repo will allow you to download updates from
lecture using

```
git pull
```

## SSH Keys

To clone the repo, you will need to set up SSH Keys on
[GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)


# Languages

Depending on the discussion, source code may be written in

  - Python 3.11+
  - C++ (11, 17, or 20)
  - Rust

Each example will include a `README.md` that describes the required
compiler/interpreter, compilation instructions, and example commands.


# Dockerfile

Run `docker build --tag 417-examples:0.1 .` to build the Docker image.

Run `docker run -it 417-examples:0.1` to run the Docker image.
