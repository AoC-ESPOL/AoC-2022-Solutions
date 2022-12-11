#pragma once

#include <string>

#include "Aoc.hpp"

namespace aoc
{

class DayNine: public Aoc {
public:
  std::string partOne(std::string input) override;

  std::string partTwo(std::string input) override;

  std::filesystem::path inputFileName() override {
    return "day09.txt";
  }
};

}
