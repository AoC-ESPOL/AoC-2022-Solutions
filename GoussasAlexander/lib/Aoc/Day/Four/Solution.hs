module Aoc.Day.Four.Solution where

import           Aoc.Class
import           Aoc.Day.Four.PartOne
import           Aoc.Day.Four.PartTwo
import           Aoc.Util

import           Data.Proxy

data DayFour

instance Aoc (Proxy DayFour) where
  type Result (Proxy DayFour) = (Int, Int)

  solution _ input =
    tupled
      (solution (Proxy @PartOne) input)
      (solution (Proxy @PartTwo) input)
