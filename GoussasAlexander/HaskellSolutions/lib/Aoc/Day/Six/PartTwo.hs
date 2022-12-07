module Aoc.Day.Six.PartTwo where

import           Aoc.Class
import           Aoc.Day.Six.Common

import           Data.Proxy
import qualified Data.Text          as T

data PartTwo

instance Aoc (Proxy PartTwo) where
  type Result (Proxy PartTwo) = Int

  solution _ input = do
    pure $ getFirstNonUniqueWindowOfSize 14 (T.unpack input)
