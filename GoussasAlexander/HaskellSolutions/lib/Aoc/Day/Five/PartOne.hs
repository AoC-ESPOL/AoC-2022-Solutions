module Aoc.Day.Five.PartOne where

import           Aoc.Class
import           Aoc.Day.Five.Common
import           Aoc.Util


import           Data.List           (foldl')
import           Data.Proxy
import           Data.Vector         (Vector, (!), (//))

data PartOne

instance Aoc (Proxy PartOne) where
  type Result (Proxy PartOne) = [Char]

  solution _ input = do
    let (crates, moves) = runParser parser input
        stacks = mkStacks crates
        stacks' = foldl' processMove stacks moves
     in pure $ getTopsOfStacks stacks'

updateStacks :: Vector [Char] -> Move -> Vector [Char]
updateStacks vs (Move _ from to) =
    vs // [(from, tail $ vs ! from), (to, head (vs ! from) :  vs ! to)]

processMove :: Vector [Char] -> Move -> Vector [Char]
processMove vs move@(Move quantity _ _) =
  foldl' (\vs' _ -> updateStacks vs' move) vs [1..quantity]
