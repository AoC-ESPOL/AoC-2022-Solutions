module Aoc.Day.Two.Solution where

import           Aoc.Class
import           Aoc.Day.Two.PartOne
import           Aoc.Day.Two.PartTwo

import           Aoc.Util            (tupled)
import           Data.Proxy

data DayTwo

dayTwo :: Proxy DayTwo
dayTwo = Proxy

instance Aoc (Proxy DayTwo) where
  type Result (Proxy DayTwo) = (Int, Int)

  solution _ input =
     tupled (solution day2Part1 input)
            (solution day2Part2 input)
