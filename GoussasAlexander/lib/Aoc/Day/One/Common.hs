module Aoc.Day.One.Common where

import           Aoc.Util

import           Data.Attoparsec.Text
import           Data.Text            (Text)

groupP :: Parser [Int]
groupP = many1 (decimal <* endOfLine)

groupsP :: Parser [[Int]]
groupsP = groupP `sepBy` char '\n'

parseInput :: Text -> IO [[Int]]
parseInput = pure . runParser groupsP
