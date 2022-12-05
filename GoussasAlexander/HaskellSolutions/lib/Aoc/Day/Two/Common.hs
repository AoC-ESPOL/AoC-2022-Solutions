module Aoc.Day.Two.Common
(
    parseInput
  , parseInputWith
  , calculateScoreForRound
  , Hand (..)
)
where

import           Data.Text (Text)
import qualified Data.Text as T

data Hand = Rock | Paper | Scissors deriving Show

scoreForHand :: Hand -> Int
scoreForHand Rock     = 1
scoreForHand Paper    = 2
scoreForHand Scissors = 3

scoreForRoundResult :: Hand -> Hand -> Int
scoreForRoundResult Rock Paper     = 6
scoreForRoundResult Rock Scissors  = 0
scoreForRoundResult Paper Rock     = 0
scoreForRoundResult Paper Scissors = 6
scoreForRoundResult Scissors Paper = 0
scoreForRoundResult Scissors Rock  = 6
scoreForRoundResult _ _            = 3

calculateScoreForRound :: (Hand, Hand) -> Int
calculateScoreForRound (foe, self) =
  scoreForRoundResult foe self + scoreForHand self

parseHand :: Text -> Hand
parseHand "A" = Rock
parseHand "Y" = Paper
parseHand "B" = Paper
parseHand "X" = Rock
parseHand "C" = Scissors
parseHand "Z" = Scissors
parseHand c   = error $ "No parse from char " <> show c

parseInputWith :: (Text -> a) -> Text -> [(Hand, a)]
parseInputWith parseFn = map parseRound . T.lines
  where
    parseRound line =
      let (foe:self:_) = T.words line
       in (parseHand foe, parseFn self)

parseInput :: Text -> [(Hand, Hand)]
parseInput = parseInputWith parseHand
