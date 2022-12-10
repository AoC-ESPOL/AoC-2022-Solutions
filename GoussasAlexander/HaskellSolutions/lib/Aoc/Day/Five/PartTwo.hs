module Aoc.Day.Five.PartTwo where

import           Aoc.Class
import           Aoc.Day.Five.Common
import           Aoc.Util

import           Data.List           (foldl')
import           Data.Proxy
import           Data.Vector         (Vector, (!), (//))

data PartTwo

instance Aoc (Proxy PartTwo) where
  type Result (Proxy PartTwo) = [Char]

  solution _ input = do
    let (crates, moves) = runParser parser input
        stacks = mkStacks crates
        stacks' = foldl' processMove stacks moves
     in pure $ getTopsOfStacks stacks'


processMove :: Vector [Char] -> Move -> Vector [Char]
processMove vs (Move quantity from to) =
  let (elems, newFrom) = splitAt quantity (vs ! from)
      newTo = elems ++ vs ! to
   in vs // [(from, newFrom), (to, newTo)]
