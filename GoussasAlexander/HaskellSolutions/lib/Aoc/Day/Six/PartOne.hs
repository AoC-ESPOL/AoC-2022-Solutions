module Aoc.Day.Six.PartOne where

import           Aoc.Class
import           Aoc.Day.Six.Common

import           Data.Proxy
import qualified Data.Text          as T

data PartOne

instance Aoc (Proxy PartOne) where
  type Result (Proxy PartOne) = Int

  solution _ input =
    pure $ getFirstNonUniqueWindowOfSize 4 (T.unpack input)
