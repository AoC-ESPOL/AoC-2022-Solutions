#![allow(clippy::must_use_candidate, clippy::missing_panics_doc)]

use std::fs;

use clap::Parser;
use color_eyre::{
    eyre::{ensure, WrapErr},
    Result,
};
use time::{macros::datetime, OffsetDateTime};

/// Solve an Advent of Code problem
#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
struct Args {
    /// Day of the problem
    #[arg(value_parser = clap::value_parser!(u8).range(1..=25))]
    day: u8,

    /// Part of the problem
    #[arg(value_parser = clap::value_parser!(u8).range(1..=2))]
    part: u8,
}

fn main() -> Result<()> {
    // Nice and colorful errors
    color_eyre::install()?;
    // Get session cookie from env file
    dotenvy::dotenv()?;

    let Args { day, part } = Args::parse();

    let input = get_problem(day)?;

    let result = solve(day, part, &input);

    println!("{result}");
    Ok(())
}

fn get_problem(day: u8) -> Result<String> {
    ensure!(
        OffsetDateTime::now_utc() >= datetime!(2022-12-01 0:00 -5).replace_day(day).unwrap(),
        "too soon. please try again when day is available"
    );
    fs::create_dir_all("./files")?;

    let file_path = format!("./files/day{day:02}.txt");

    let (session_cookie, user_agent) = match fs::read_to_string(&file_path) {
        // If file exists, return the file
        Ok(aoc_problem) => return Ok(aoc_problem),
        // If os_error, return the error
        Err(e) if e.kind() != std::io::ErrorKind::NotFound => {
            return Err(e).wrap_err("couldn't access cached file")
        }
        // If file not found, get session cookie and user agent
        Err(_) => (
            std::env::var("AOC_SESSION").wrap_err("AOC_SESSION not found")?,
            std::env::var("USER_AGENT").wrap_err("USER_AGENT not found")?,
        ),
    };

    // TODO: use tracing
    println!("file not in cache");

    let cookie = ureq::Cookie::new("session", session_cookie);

    let response = ureq::get(&format!("https://adventofcode.com/2022/day/{day}/input"))
        .set("Cookie", &cookie.to_string())
        .set("User-Agent", &user_agent)
        .call()
        .wrap_err("maybe too soon")?
        .into_string()?;

    // Cache the file
    fs::write(file_path, &response)?;

    Ok(response)
}

fn solve(day: u8, part: u8, input: &str) -> String {
    match (day, part) {
        (1, 1) => day_01::part1(input),
        (1, 2) => day_01::part2(input),
        (2, 1) => day_02::part1(input),
        (2, 2) => day_02::part2(input),
        (3, 1) => day_03::part1(input),
        (3, 2) => day_03::part2(input),
        (4, 1) => day_04::part1(input),
        (4, 2) => day_04::part2(input),
        (5, 1) => day_05::part1(input),
        (5, 2) => day_05::part2(input),
        (6, 1) => day_06::part1(input),
        (6, 2) => day_06::part2(input),
        (7, 1) => day_07::part1(input),
        (7, 2) => day_07::part2(input),
        (8, 1) => day_08::part1(input),
        (8, 2) => day_08::part2(input),
        (9, 1) => day_09::part1(input),
        (9, 2) => day_09::part2(input),
        (10, 1) => day_10::part1(input),
        (10, 2) => day_10::part2(input),
        (11, 1) => day_11::part1(input),
        (11, 2) => day_11::part2(input),
        (12, 1) => day_12::part1(input),
        (12, 2) => day_12::part2(input),
        (13, 1) => day_13::part1(input),
        (13, 2) => day_13::part2(input),
        (14, 1) => day_14::part1(input),
        (14, 2) => day_14::part2(input),
        (15, 1) => day_15::part1(input),
        (15, 2) => day_15::part2(input),
        (16, 1) => day_16::part1(input),
        (16, 2) => day_16::part2(input),
        (17, 1) => day_17::part1(input),
        (17, 2) => day_17::part2(input),
        (18, 1) => day_18::part1(input),
        (18, 2) => day_18::part2(input),
        (19, 1) => day_19::part1(input),
        (19, 2) => day_19::part2(input),
        (20, 1) => day_20::part1(input),
        (20, 2) => day_20::part2(input),
        (21, 1) => day_21::part1(input),
        (21, 2) => day_21::part2(input),
        (22, 1) => day_22::part1(input),
        (22, 2) => day_22::part2(input),
        (23, 1) => day_23::part1(input),
        (23, 2) => day_23::part2(input),
        (24, 1) => day_24::part1(input),
        (24, 2) => day_24::part2(input),
        (25, 1) => day_25::part1(input),
        (25, 2) => day_25::part2(input),
        _ => unreachable!(),
    }
}

mod day_01;
mod day_02;
mod day_03;
mod day_04;
mod day_05;
mod day_06;
mod day_07;
mod day_08;
mod day_09;
mod day_10;
mod day_11;
mod day_12;
mod day_13;
mod day_14;
mod day_15;
mod day_16;
mod day_17;
mod day_18;
mod day_19;
mod day_20;
mod day_21;
mod day_22;
mod day_23;
mod day_24;
mod day_25;
