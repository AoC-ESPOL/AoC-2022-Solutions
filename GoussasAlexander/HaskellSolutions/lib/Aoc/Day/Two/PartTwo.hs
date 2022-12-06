module Aoc.Day.Two.PartTwo where

import           Aoc.Class
import           Aoc.Day.Two.Common

import           Data.Proxy
import           Data.Text          (Text)

data Day2Part2

data RoundResult = Win | Lose | Draw deriving Show

parseRoundResult :: Text -> RoundResult
parseRoundResult "X" = Lose
parseRoundResult "Y" = Draw
parseRoundResult "Z" = Win
parseRoundResult c   = error $ "No parse for char " <> show c

calculateHandForResult :: Hand -> RoundResult -> Hand
calculateHandForResult Paper Win     = Scissors
calculateHandForResult Paper Lose    = Rock
calculateHandForResult Paper Draw    = Paper
calculateHandForResult Scissors Win  = Rock
calculateHandForResult Scissors Lose = Paper
calculateHandForResult Scissors Draw = Scissors
calculateHandForResult Rock Win      = Paper
calculateHandForResult Rock Lose     = Scissors
calculateHandForResult Rock Draw     = Rock

day2Part2 :: Proxy Day2Part2
day2Part2 = Proxy

instance Aoc (Proxy Day2Part2) where
  type Result (Proxy Day2Part2) = Int

  solution _ input =
    let rounds = parseInputWith parseRoundResult input
        rounds' = map (\(a, b) -> (a, calculateHandForResult a b)) rounds
     in pure $ sum $ map calculateScoreForRound rounds'
