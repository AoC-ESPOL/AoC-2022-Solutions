module DayTwoSpec where

import           Aoc.Class
import           Aoc.Day.Two.PartOne

import           Test.Hspec

main :: IO ()
main = hspec spec

spec :: Spec
spec = partOneSpec

partOneSpec :: Spec
partOneSpec = describe "Part one" $ do
  describe "With the example input" $
    it "works" $ do
      solution day2Part1 "A Y\nB X\nC Z" `shouldReturn` 15

partTwoSpec :: Spec
partTwoSpec = describe "Part two" $ do
  describe "With the example input" $
    it "works" $ do
      solution day2Part1 "A Y\nB X\nC Z" `shouldReturn` 12
