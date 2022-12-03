module Aoc.Day.Two.PartOne where

import           Aoc.Class
import           Aoc.Day.Two.Common

import           Data.Proxy

data Day2Part1

day2Part1 :: Proxy Day2Part1
day2Part1 = Proxy

instance Aoc (Proxy Day2Part1) where
  type Result (Proxy Day2Part1) = Int

  solution _ input = do
    let rounds = parseInput input
    pure $ sum $ map calculateScoreForRound rounds
