module Aoc.Util where

import           Data.Attoparsec.Text
import           Data.Text            (Text)
import qualified Data.Text            as T

tupled :: (Applicative a) =>  a b -> a c -> a (b, c)
tupled b c = (,) <$> b <*> c

range :: Int -> Int -> [Int]
range start end =  [start..end]

runParser :: Parser a -> Text -> a
runParser parser =
    either error id
  . eitherResult
  . flip feed T.empty
  . parse parser
