module DayFiveSpec where

import           Aoc.Class
import           Aoc.Day.Five.Common
import           Aoc.Day.Five.PartOne
import           Aoc.Day.Five.PartTwo
import           Aoc.Input
import           Aoc.Types
import           Aoc.Util

import           Data.Proxy
import qualified Data.Text            as T
import qualified Data.Vector          as V
import           Test.Hspec

main :: IO ()
main = hspec spec

spec :: Spec
spec = parserSpec >> partOneSpec

parserSpec :: Spec
parserSpec = describe "Day 5 Parser" $ do
  it "Can parse a single crate line with no empty crates" $ do
    let input = "[Z] [M] [P]\n"
    runParser cratesP input `shouldBe` [Crate 'Z', Crate 'M', Crate 'P']

  it "Can parse a single crate line with empty crates" $ do
    let input = "[N] [C]    \n"
    runParser cratesP input `shouldBe` [Crate 'N', Crate 'C', Empty]

  it "Can parse a single move line" $ do
    let input = "move 1 from 2 to 1\n"
    runParser moveP input `shouldBe` Move 1 1 0

  it "Can parse a group of move lines" $ do
    let input = T.unlines [ "move 1 from 2 to 1"
                          , "move 3 from 1 to 3"
                          , "move 2 from 2 to 1"
                          , "move 1 from 1 to 2"
                          ]
    runParser movesP input `shouldBe` [Move 1 1 0, Move 3 0 2, Move 2 1 0, Move 1 0 1]

  it "Can parse the example input" $ do
    let input = T.unlines [ "    [D]    "
                          , "[N] [C]    "
                          , "[Z] [M] [P]"
                          , " 1   2   3 "
                          , ""
                          , "move 1 from 2 to 1"
                          , "move 3 from 1 to 3"
                          , "move 2 from 2 to 1"
                          , "move 1 from 1 to 2"
                          ]
    runParser parser input `shouldBe`
      ( [[Empty, Crate 'D', Empty], [Crate 'N', Crate 'C', Empty], [Crate 'Z', Crate 'M', Crate 'P']]
      , [Move 1 1 0, Move 3 0 2, Move 2 1 0, Move 1 0 1]
      )

partOneSpec :: Spec
partOneSpec = describe "Part One" $ do
  it "Building crate stacks works" $ do
    let crates = [[Empty, Crate 'D', Empty], [Crate 'N', Crate 'C', Empty], [Crate 'Z', Crate 'M', Crate 'P']]
    mkStacks crates `shouldBe` V.fromList [['N', 'Z'], ['D', 'C', 'M'], ['P']]

  it "Update stacks works" $ do
    let stacks = V.fromList [['N', 'Z'], ['D', 'C', 'M'], ['P']]
    updateStacks stacks (Move 1 0 1) `shouldBe`  V.fromList [['Z'], ['N', 'D', 'C', 'M'], ['P']]

  it "Get top of stacks works" $ do
    let stacks = V.fromList [['N', 'Z'], ['D', 'C', 'M'], ['P']]
    getTopsOfStacks stacks `shouldBe` "NDP"

  it "With the puzzle input works" $ do
    input <- inputForDay (mkDay 5)
    solution (Proxy @PartOne) input `shouldReturn` "TQRFCBSJJ"

partTwoSpec :: Spec
partTwoSpec = describe "Part two" $
  it "With the puzzle input works" $ do
    input <- inputForDay (mkDay 5)
    solution (Proxy @PartTwo) input `shouldReturn` "RMHFJNVFP"
