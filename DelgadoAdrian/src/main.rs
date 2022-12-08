#![allow(clippy::must_use_candidate, clippy::missing_panics_doc)]

use std::{fs, time::Instant};

use arboard::Clipboard;
use color_eyre::{
    eyre::{ensure, WrapErr},
    Result,
};
use time::{macros::datetime, OffsetDateTime};

mod flags;
use flags::Problem;

fn main() -> Result<()> {
    // Nice and colorful errors
    color_eyre::install()?;
    // Get session cookie from env file
    dotenvy::dotenv()?;

    let Problem { day, part } = Problem::from_env()?;

    ensure!((1..=25).contains(&day), "Day must be between 1 and 25");
    ensure!((1..=2).contains(&part), "Part must 1 or 2");

    let input = get_problem(day)?;

    let result = solve(day, part, &input);

    println!("{result}");

    Clipboard::new()?.set_text(&result)?;

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

fn timing_fn<T, F>(f: F) -> T
where
    F: Fn() -> T,
{
    let now = Instant::now();
    let ret = f();
    println!("Finished in {} μs", now.elapsed().as_micros());
    ret
}

macro_rules! match_solvers {
    (($curr_day:ident, $curr_part:ident, $input:ident) , [$(($day:literal,$module:ident)),+ $(,)?]) => {
        match ($curr_day, $curr_part) {
        $(
            ($day, 1) => timing_fn(|| $module::part1($input)).to_string(),
            ($day, 2) => timing_fn(|| $module::part2($input)).to_string(),
        )+
            _ => unreachable!(),
        }
    };
}

fn solve(day: u8, part: u8, input: &str) -> String {
    match_solvers!(
        (day, part, input),
        [
            (1, day_01),
            (2, day_02),
            (3, day_03),
            (4, day_04),
            (5, day_05),
            (6, day_06),
            (7, day_07),
            (8, day_08),
            (9, day_09),
            (10, day_10),
            (11, day_11),
            (12, day_12),
            (13, day_13),
            (14, day_14),
            (15, day_15),
            (16, day_16),
            (17, day_17),
            (18, day_18),
            (19, day_19),
            (20, day_20),
            (21, day_21),
            (22, day_22),
            (23, day_23),
            (24, day_24),
            (25, day_25),
        ]
    )
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
