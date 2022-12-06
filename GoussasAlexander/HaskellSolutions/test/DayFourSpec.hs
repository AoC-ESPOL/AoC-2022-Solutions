{-# LANGUAGE TypeApplications #-}
module DayFourSpec where

import           Aoc.Class
import           Aoc.Day.Four.PartOne
import           Aoc.Day.Four.PartTwo

import           Data.Proxy
import qualified Data.Text            as T
import           Test.Hspec


main :: IO ()
main = hspec spec

spec :: Spec
spec = partOneSpec

partOneSpec :: Spec
partOneSpec = describe "Part one" $ do
  describe "With the example input" $ do
    it "Returns 2" $ do
      let input = T.unlines [
                    "2-4,6-8",
                    "2-3,4-5",
                    "5-7,7-9",
                    "2-8,3-7",
                    "6-6,4-6",
                    "2-6,4-8"
                    ]
      solution (Proxy @PartOne) input `shouldReturn` 2

partTwoSpec :: Spec
partTwoSpec = describe "Part two" $ do
  describe "With the example input" $
    it "Returns 4" $ do
      let input = T.unlines [
                    "2-4,6-8",
                    "2-3,4-5",
                    "5-7,7-9",
                    "2-8,3-7",
                    "6-6,4-6",
                    "2-6,4-8"
                    ]
      solution (Proxy @PartTwo) input `shouldReturn` 4
