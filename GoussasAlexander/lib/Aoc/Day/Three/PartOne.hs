module Aoc.Day.Three.PartOne where

import           Aoc.Class
import           Aoc.Day.Three.Common

import           Data.List
import           Data.Proxy


data Day3Part1

day3Part1 :: Proxy Day3Part1
day3Part1 = Proxy

instance Aoc (Proxy Day3Part1) where
  type Result (Proxy Day3Part1) = Int

  solution _ input = do
    let rucksacks = parseInput input
    pure $ sum $ map (getItemPriority . getMisplacedItem) rucksacks


getMisplacedItem :: Rucksack -> Item
getMisplacedItem = head . uncurry intersect


