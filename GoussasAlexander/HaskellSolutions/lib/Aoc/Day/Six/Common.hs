module Aoc.Day.Six.Common where

import           Data.List (nub, tails)

isUniq :: (Eq a) => [a] -> Bool
isUniq xs = nub xs == xs

mkWindows :: Int -> [a] -> [[a]]
mkWindows size = map (take size)
               . filter (\xs -> length xs >= size)
               . tails

getFirstNonUniqueWindowOfSize :: (Eq a) => Int -> [a] -> Int
getFirstNonUniqueWindowOfSize wsize input =
    let windows = zipWith (\a b -> (a, isUniq b)) [0..] (mkWindows wsize input)
     in head (map fst $ filter snd windows) + wsize

