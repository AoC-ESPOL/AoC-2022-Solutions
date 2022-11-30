# Advent of Code Solutions

## Structure

### Solutions

Solutions are divided into modules in the following manner:

- Each day has its separate module folder
- Each part of the day has its own module in the day's folder
- There is a `Common.hs` module inside the day's folder to factor out
  common functionality in parts I and II.

### Tests

Each solution should have its corresponding test, which usually uses the examples
from the corresponding problem. The naming convention for the day module is
`Day<day>Spec.hs`. For example, for day 1 the corresponding test module would be
called `DayOneSpec`.

### Puzzle inputs

The puzzle inputs are located in the `puzzle-inputs` directory. These must be named
following the convention: `day<day number>.txt`.

The provided CLI tool can be used to fetch the input for every day. For example, to fetch
the input for day 1:

```bash
aoc fetchInput --day 1
```

This will download your input and put it in `puzzle-inputs/day1.txt`.

NOTE: For this to work you need to put your session cookie in an `.env` file using the
key `AOC_SESSION`.

## Generate boilerplate

This template comes with a CLI tool to help you generate all this boilerplate code. To install
it run

```bash
cabal install
```

Then you can use the tool to generate to solution component and test modules:

```bash
aoc generate --day 1
```

Example output:

```
Creating component file: lib/Aoc/Day/One/PartOne.hs
Creating component file: lib/Aoc/Day/One/PartTwo.hs
Creating component file: lib/Aoc/Day/One/Common.hs
Creating test module: test/DayOneSpec.hs

Finished creating component.

Copy this in your cabal file to add the new component to the build:

In lib:

   Aoc.Day.One.PartOne,
   Aoc.Day.One.PartTwo,
   Aoc.Day.One.Common,

In the test suite:

   DayOneSpec,


```

## Running

In the `app` directory there is an executable to run the solutions. You'll need to edit it
in order to add the solution for each day. See the instructions in the source code.

Then you can run it with

```bash
cabal run aoc-runner <day-number>
```

For example, to run the solution for day 1:

```bash
cabal run aoc-runner 1
```

## License

MIT
