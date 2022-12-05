module Aoc.Day.Four.Common where

import           Aoc.Util

import           Control.Applicative
import           Data.Attoparsec.Text
import           Data.Text            (Text)

type Assignments = [Int]

elfAssignmentsP :: Parser Assignments
elfAssignmentsP = range <$> decimal <* char '-' <*> decimal

pairP :: Parser (Assignments, Assignments)
pairP = (,) <$> elfAssignmentsP <* char ',' <*> elfAssignmentsP

parseInput :: Text -> [(Assignments, Assignments)]
parseInput = runParser $ pairP `sepBy` (endOfLine <|> endOfInput)
