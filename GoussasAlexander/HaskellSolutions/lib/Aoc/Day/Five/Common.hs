module Aoc.Day.Five.Common where

import           Aoc.Util

import           Control.Applicative
import           Data.Attoparsec.Text
import           Data.Vector          (Vector)
import qualified Data.Vector          as V

data Crate = Crate Char | Empty deriving (Show, Eq)

isEmptyCrate :: Crate -> Bool
isEmptyCrate Empty = True
isEmptyCrate _     = False

toChar :: Crate -> Char
toChar (Crate c) = c
toChar Empty     = error "Can get char from empty crate!"

data Move = Move
  { mQuantity :: Int
  , mFrom     :: Int
  , mTo       :: Int
  } deriving (Show, Eq)


moveP :: Parser Move
moveP = normalizeMove <$> (Move
  <$> (string "move " *> decimal <* char ' ')
  <*> (string "from " *> decimal <* char ' ')
  <*> (string "to " *> decimal))
  where
    normalizeMove (Move q f t) = Move q (f-1) (t-1)

movesP :: Parser [Move]
movesP =  moveP `sepBy` endOfLine

cratesP :: Parser [Crate]
cratesP = (crateP <|> emptyCrateP) `sepBy` char ' ' <* endOfLine

crateP :: Parser Crate
crateP = Crate <$> (char '[' *> anyChar <* char ']')

emptyCrateP :: Parser Crate
emptyCrateP = Empty <$ count 3 (char ' ')

parser :: Parser ([[Crate]], [Move])
parser = (,) <$> allCratesP <*> movesP
  where
    allCratesP = many1 cratesP <* (lineP *> endOfLine)

mkStacks :: [[Crate]] -> Vector [Char]
mkStacks crates = V.generate (length $ head crates) gen
  where
    gen :: Int -> [Char]
    gen n = map toChar $ filter (not . isEmptyCrate) $ map (!!n) crates

getTopsOfStacks :: Vector [Char] -> [Char]
getTopsOfStacks = V.toList . V.map head
