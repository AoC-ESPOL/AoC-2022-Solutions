module Input
  ( Day,
    toInt,
    mkDay,
    inputForDay,
    parseDay,
  )
where

import Data.Text
import qualified Data.Text.IO as TIO
import System.FilePath

-- | A day of AoC.
newtype Day = Day {toInt :: Int} deriving (Show)

mkDay :: Int -> Day
mkDay day
  | day < 1 || day > 25 = error "Invalid AoC day"
  | otherwise = Day day

-- | 'parseDay' tries to parse the provided string into a 'Day'.
parseDay :: String -> Maybe Day
parseDay s =
  let day = read s
   in if day < 1 || day > 25
        then Nothing
        else pure $ Day day

puzzleDir :: FilePath
puzzleDir = "puzzle-inputs"

-- | 'inputFileForDay' get the file corresponding to the day's puzzle input.
inputFileForDay :: Day -> FilePath
inputFileForDay day = puzzleDir </> "day" <> (show . toInt $ day) <.> "txt"

-- | 'inputForDay' returns the input for a given day.
inputForDay :: Day -> IO Text
inputForDay = TIO.readFile . inputFileForDay
