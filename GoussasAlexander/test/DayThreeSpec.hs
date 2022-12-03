module DayThreeSpec where

import           Aoc.Class
import           Aoc.Day.Three.PartOne
import           Aoc.Input             (inputForDay)
import           Aoc.Types

import           Aoc.Day.Three.PartTwo (day3Part2)
import qualified Data.Text             as T
import           Test.Hspec


main :: IO ()
main = hspec spec

spec :: Spec
spec = partOneSpec

partOneSpec :: Spec
partOneSpec =
  describe "Part one" $ do
    describe "With the example input" $
      it "Returns 157" $
        let input = T.unlines
                      [ "vJrwpWtwJgWrhcsFMMfFFhFp"
                      , "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"
                      , "PmmdzqPrVvPwwTWBwg"
                      , "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn"
                      , "ttgJtRGJQctTZtZT"
                      , "CrZsJsPPZsGzwwsLwLmpwMDw"
                      ]
         in solution day3Part1 input `shouldReturn` 157

    describe "With the real input" $
      it "Returns 7845" $ do
        input <- inputForDay $ mkDay 3
        solution day3Part1 input `shouldReturn` 7845


partTwoSpec :: Spec
partTwoSpec = describe "Part two" $ do
  describe "With the example input" $
    it "Returns 70" $
      let input = T.unlines
                  [ "vJrwpWtwJgWrhcsFMMfFFhFp"
                  , "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"
                  , "PmmdzqPrVvPwwTWBwg"
                  , "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn"
                  , "ttgJtRGJQctTZtZT"
                  , "CrZsJsPPZsGzwwsLwLmpwMDw"
                  ]
       in solution day3Part2 input `shouldReturn` 70

  describe "With the real input" $
    it "Returns 2790" $ do
      input <- inputForDay $ mkDay 3
      solution day3Part2 input `shouldReturn` 2790

