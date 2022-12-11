#pragma once

#include <filesystem>
#include <string>

using namespace std::literals::string_literals;

namespace aoc
{

class Aoc
{
public:
  /**
   * Part one solution.
   */
  virtual std::string partOne(std::string input) = 0;

  virtual std::string partOne() final;

  /**
   * Part two solution.
   */
  virtual std::string partTwo(std::string input) = 0;

  virtual std::string partTwo() final;

  /**
   * The input file name for the day.
   */
  virtual std::filesystem::path inputFileName() = 0;

  virtual void run() noexcept;

protected:
  virtual auto getInput() -> std::string;
};

}
