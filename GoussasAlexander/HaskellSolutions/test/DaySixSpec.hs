module DaySixSpec where

import           Aoc.Class
import           Aoc.Day.Six.PartOne
import           Aoc.Day.Six.PartTwo
import           Aoc.Input
import           Aoc.Types

import           Data.Proxy
import           Test.Hspec

main :: IO ()
main = hspec spec

spec :: Spec
spec = partOneSpec >> partTwoSpec

partOneSpec :: Spec
partOneSpec = describe "Part One" $ do
  describe "With the example inputs" $ do
    it "Returns 5 when given bvwbjplbgvbhsrlpgdmjqwftvncz" $
      solution (Proxy @PartOne) "bvwbjplbgvbhsrlpgdmjqwftvncz" `shouldReturn` 5

    it "Returns 6 when given nppdvjthqldpwncqszvftbrmjlhg" $
      solution (Proxy @PartOne) "nppdvjthqldpwncqszvftbrmjlhg" `shouldReturn` 6

  describe "With the puzzle input" $
    it "Returns 1343" $ do
      input <- inputForDay (mkDay 6)
      solution (Proxy @PartOne) input `shouldReturn` 1343

partTwoSpec :: Spec
partTwoSpec = describe "Part two" $
  describe "With the puzzle input" $
    it "Returns 2193" $ do
      input <- inputForDay (mkDay 6)
      solution (Proxy @PartTwo) input `shouldReturn` 2193
