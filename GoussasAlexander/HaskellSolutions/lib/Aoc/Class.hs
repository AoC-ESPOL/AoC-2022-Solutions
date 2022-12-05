module Aoc.Class where

import           Data.Text

class Aoc a where
  -- | The result type for the day's puzzle.
  type Result a

  -- | 'solution' returns the solution for the day's puzzle.
  solution :: a -> Text -> IO (Result a)
