module Aoc.Day.One.Solution where

import           Aoc.Class

import           Aoc.Day.One.PartOne (day1Part1)
import           Aoc.Day.One.PartTwo (day1Part2)
import           Aoc.Util            (tupled)
import           Data.Proxy


data DayOne

dayOne :: Proxy DayOne
dayOne = Proxy

instance Aoc (Proxy DayOne) where
  type Result (Proxy DayOne) = (Int, Int)

  solution _ input = tupled (solution day1Part1 input) (solution day1Part2 input)
