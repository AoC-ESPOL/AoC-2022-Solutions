module Aoc.Day.One.Common where

import           Data.Text (Text)
import qualified Data.Text as T

parseInput :: Text -> IO [[Int]]
parseInput input = do
  let groups = map (T.splitOn "\n") $ T.splitOn "\n\n" input
  return $ map (map (read . T.unpack) . filter (not . T.null)) groups
