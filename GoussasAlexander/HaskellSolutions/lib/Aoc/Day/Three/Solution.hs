module Aoc.Day.Three.Solution where

import           Aoc.Class
import           Aoc.Day.Three.PartOne
import           Aoc.Day.Three.PartTwo
import           Aoc.Util

import           Data.Proxy

data DayThree

dayThree :: Proxy DayThree
dayThree = Proxy

instance Aoc (Proxy DayThree) where
  type Result (Proxy DayThree) = (Int, Int)

  solution _ input = tupled
      (solution day3Part1 input)
      (solution day3Part2 input)
