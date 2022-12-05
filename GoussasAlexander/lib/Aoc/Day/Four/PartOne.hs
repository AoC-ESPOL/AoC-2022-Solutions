module Aoc.Day.Four.PartOne where

import           Aoc.Class
import           Aoc.Day.Four.Common

import           Data.List           (isInfixOf)
import           Data.Proxy

data PartOne

instance Aoc (Proxy PartOne) where
  type Result (Proxy PartOne) = Int

  solution _  =  pure . length . filter (uncurry doAssignmentsOverlap) . parseInput


doAssignmentsOverlap :: Assignments -> Assignments -> Bool
doAssignmentsOverlap xs ys = xs `isInfixOf` ys || ys `isInfixOf` xs
