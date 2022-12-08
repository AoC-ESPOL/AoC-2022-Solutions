module Aoc.Day.Six.Solution where

import           Aoc.Class
import           Aoc.Day.Six.PartOne
import           Aoc.Day.Six.PartTwo
import           Aoc.Util

import           Data.Proxy

data DaySix

instance Aoc (Proxy DaySix) where
  type Result (Proxy DaySix) = (Int, Int)

  solution _ input =
    tupled
      (solution (Proxy @PartOne) input)
      (solution (Proxy @PartTwo) input)
