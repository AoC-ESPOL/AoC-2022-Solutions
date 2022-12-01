module Aoc.Day.One.PartOne where

import           Aoc.Class
import           Aoc.Day.One.Common

import           Data.Proxy

data Day1Part1

day1Part1 :: Proxy Day1Part1
day1Part1 = Proxy

instance Aoc (Proxy Day1Part1) where
  type Result (Proxy Day1Part1) = Int

  solution _ input = maximum . map sum <$> parseInput input
