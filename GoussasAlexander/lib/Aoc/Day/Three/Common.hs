module Aoc.Day.Three.Common where

import           Data.Char
import           Data.List (intersect)
import           Data.Text (Text)
import qualified Data.Text as T

-- Each rucksack has two compartments
-- Items of a given type are meant to go in one of them

type Item = Char
type Compartment = [Item]
type Rucksack = (Compartment, Compartment)

parseInput :: Text -> [Rucksack]
parseInput = map getCompartments . lines . T.unpack

getCompartments :: [Item] -> Rucksack
getCompartments items =
  let n = length items `div` 2
   in splitAt n items

getMisplacedItem :: Rucksack -> Item
getMisplacedItem = head . uncurry intersect

getItemPriority :: Item -> Int
getItemPriority item
  | isAsciiLower item = (ord item - 97) + 1
  | isAsciiUpper item = (ord item - 65) + 27
  | otherwise = error "Invalid item"
