module Aoc.Input (inputForDay) where

import           Aoc.Types

import           Data.Text
import qualified Data.Text.IO    as TIO
import           System.FilePath

puzzleDir :: FilePath
puzzleDir = "puzzle-inputs"

-- | 'inputFileForDay' get the file corresponding to the day's puzzle input.
inputFileForDay :: AocDay -> FilePath
inputFileForDay day = puzzleDir </> "day" <> (show . toInt $ day) <.> "txt"

-- | 'inputForDay' returns the input for a given day.
inputForDay :: AocDay -> IO Text
inputForDay = TIO.readFile . inputFileForDay
