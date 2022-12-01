# AoC 2022

Solutions for Advent of Code 2022 in Rust

## Usage

From Cargo

```sh
cargo run --release -- <DAY> <PART>
```

As a standalone binary

```sh
aoc_2022 <DAY> <PART>
```

The application expects an `AOC_SESSION` env variable which has an Advent of Code session cookie
and a `USER_AGENT` env variable with your github handle. (see: <https://www.reddit.com/r/adventofcode/comments/z9dhtd/please_include_your_contact_info_in_the_useragent/>)

The env variables can be also provided via an `.env` file.
