module Aoc.Day.Five.Solution where

import           Aoc.Class
import           Aoc.Day.Five.PartOne
import           Aoc.Day.Five.PartTwo
import           Aoc.Util

import           Data.Proxy

data DayFive

instance Aoc (Proxy DayFive) where
  type Result (Proxy DayFive) = ([Char], [Char])

  solution _ input =
    tupled
      (solution (Proxy @PartOne) input)
      (solution (Proxy @PartTwo) input)
