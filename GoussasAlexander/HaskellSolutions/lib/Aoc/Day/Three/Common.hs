module Aoc.Day.Three.Common where

import           Aoc.Util

import           Data.Attoparsec.Text
import           Data.Char
import           Data.Functor
import           Data.Text            (Text)
import qualified Data.Text            as T

-- Each rucksack has two compartments
-- Items of a given type are meant to go in one of them

type Item = Char
type Compartment = [Item]
type Rucksack = (Compartment, Compartment)

parseInput :: Text -> [Rucksack]
parseInput = runParser $ many1 rucksackP

rucksackP :: Parser Rucksack
rucksackP = lineP <&> \line ->
  splitAt (T.length line `div` 2) $ T.unpack line

getItemPriority :: Item -> Int
getItemPriority item
  | isAsciiLower item = (ord item - 97) + 1
  | isAsciiUpper item = (ord item - 65) + 27
  | otherwise = error "Invalid item"
