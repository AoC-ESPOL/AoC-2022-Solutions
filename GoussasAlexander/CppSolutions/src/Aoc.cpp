#include <filesystem>
#include <fstream>
#include <iostream>
#include <iterator>

namespace fs = std::filesystem;

#include "Aoc.hpp"

namespace aoc
{

auto
Aoc::getInput() -> std::string
{
  auto fileName{ inputFileName() };

  if (!fs::exists(fileName))
    {
      std::cerr << "Input file name not found: " << fileName << "\n";
      exit(EXIT_FAILURE);
    }

  std::ifstream ifs{ fileName, std::ios::in };
  return std::string{ std::istreambuf_iterator<char>{ ifs }, {} };
}

std::string
Aoc::partOne()
{
  return partOne(getInput());
}

std::string
Aoc::partTwo()
{
  return partTwo(getInput());
}

void
Aoc::run() noexcept
{
  std::cout << "Part one: " << partOne() << "\n";
  std::cout << "Part two: " << partTwo() << "\n";
}

}
