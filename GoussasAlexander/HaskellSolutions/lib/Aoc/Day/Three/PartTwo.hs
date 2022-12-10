module Aoc.Day.Three.PartTwo where

import           Aoc.Class
import           Aoc.Day.Three.Common

import           Data.Foldable        (toList)
import           Data.Proxy
import qualified Data.Sequence        as Seq


data Day3Part2

day3Part2 :: Proxy Day3Part2
day3Part2 = Proxy

chunksOf :: Int -> [Rucksack] -> [[Rucksack]]
chunksOf n rucksacks =
  toList (toList <$> Seq.chunksOf n (Seq.fromList rucksacks))

joinRucksack :: Rucksack -> [Item]
joinRucksack (xs, ys) = xs ++ ys

findBadge :: [Rucksack] -> Item
findBadge rs = head $ filter p (joinRucksack $ head rs)
  where
    p item = all (\r -> item `elem` joinRucksack r) rs

instance Aoc (Proxy Day3Part2) where
  type Result (Proxy Day3Part2) = Int

  solution _ input = do
    let rucksacks = parseInput input
        groups = chunksOf 3 rucksacks
    pure $ sum $ map (getItemPriority . findBadge) groups

