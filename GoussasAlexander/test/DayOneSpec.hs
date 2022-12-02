module DayOneSpec where

import           Aoc.Class
import           Aoc.Day.One.PartOne
import           Aoc.Day.One.PartTwo

import           Aoc.Input           (inputForDay)
import           Aoc.Types           (mkDay)
import           Test.Hspec

main :: IO ()
main = hspec spec

spec :: Spec
spec = describe "Day One" $ partOneSpec >> partTwoSpec

partOneSpec :: Spec
partOneSpec = describe "Part one" $ do
  describe "With the puzzle input" $
    it "Results in 69795" $ do
      input <- inputForDay $ mkDay 1
      solution day1Part1 input `shouldReturn` 69795

partTwoSpec :: Spec
partTwoSpec = describe "Part two" $ do
  describe "With the puzzle input" $
    it "Results in 208437" $ do
      input <- inputForDay $ mkDay 1
      solution day1Part2 input `shouldReturn` 208437
