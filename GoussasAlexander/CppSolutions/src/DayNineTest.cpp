#include <cassert>
#include <iostream>

#include "DayNine.hpp"

using namespace aoc;

const char* sampleInput = "R 4\n"
                          "U 4\n"
                          "L 3\n"
                          "D 1\n"
                          "R 4\n"
                          "D 1\n"
                          "L 5\n"
                          "R 2";

auto
testPartOneWithSampleInput() -> void
{
  DayNine day{};
  auto result = day.partOne(sampleInput);
  assert(result == "13");
}

auto
testPartTwoWithSampleInput()
{
  DayNine day{};
  auto result = day.partTwo(sampleInput);
  assert(result == "1");
}

auto
testPartTwoWithSlightlyLargerExample()
{
  DayNine day{};
  auto input = "R 5\n"
               "U 8\n"
               "L 8\n"
               "D 3\n"
               "R 17\n"
               "D 10\n"
               "L 25\n"
               "U 20";
  auto result = day.partTwo(input);
  assert(result == "36");
}

auto
main() -> int
{
  testPartOneWithSampleInput();
  testPartTwoWithSampleInput();
  testPartTwoWithSlightlyLargerExample();
  return 0;
}
