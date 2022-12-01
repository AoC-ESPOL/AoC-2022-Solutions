module Aoc.Day.One.PartTwo where

import           Aoc.Class
import           Aoc.Day.One.Common

import           Data.List
import           Data.Proxy

data Day1Part2

day1Part2 :: Proxy Day1Part2
day1Part2 = Proxy

instance Aoc (Proxy Day1Part2) where
  type Result (Proxy Day1Part2) = Int

  solution _ input = sum
                  . take 3
                  . sortBy (flip compare)
                  . map sum
                   <$> parseInput input
