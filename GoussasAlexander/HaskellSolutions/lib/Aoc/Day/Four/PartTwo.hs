module Aoc.Day.Four.PartTwo where

import           Aoc.Class
import           Aoc.Day.Four.Common

import           Data.List           (intersect)
import           Data.Proxy

data PartTwo

instance Aoc (Proxy PartTwo) where
  type Result (Proxy PartTwo) = Int

  solution _ = pure . length . filter (uncurry doAssignmentsOverlap) . parseInput

doAssignmentsOverlap :: Assignments -> Assignments -> Bool
doAssignmentsOverlap xs ys =
  let overlap = xs `intersect` ys
   in not . null $ overlap
