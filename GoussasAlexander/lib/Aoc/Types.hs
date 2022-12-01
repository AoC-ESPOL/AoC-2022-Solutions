module Aoc.Types
(
    AocDay
  , mkDay
  , parseDay
  , toInt
)
where


-- | A day of AoC.
newtype AocDay = AocDay {toInt :: Int} deriving (Show, Eq)

mkDay :: Int -> AocDay
mkDay day
  | day < 1 || day > 25 = error "Invalid AoC day"
  | otherwise = AocDay day

-- | 'parseDay' tries to parse the provided string into a 'Day'.
parseDay :: String -> Maybe AocDay
parseDay s =
  let day = read s
   in if day < 1 || day > 25
        then Nothing
        else pure $ AocDay day


