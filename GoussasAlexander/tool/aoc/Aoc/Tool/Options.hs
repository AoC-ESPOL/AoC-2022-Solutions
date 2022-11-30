module Aoc.Tool.Options where

import Options.Applicative

data Command
  = Generate GenerateOptions
  | FetchInput FetchInputOptions
  deriving (Show)

newtype FetchInputOptions = FetchInputOptions {getDay :: Int} deriving (Show)

newtype GenerateOptions = GenerateOptions {optDayNumber :: Int} deriving (Show)

fetchInputCommand :: ParserInfo Command
fetchInputCommand =
  FetchInput
    <$> info
      (FetchInputOptions <$> dayNumber "The puzzle day to get.")
      (progDesc "Fetch the puzzle input for a day.")

generateCommand :: ParserInfo Command
generateCommand =
  Generate
    <$> info
      (GenerateOptions <$> dayNumber "The day to generate a solution component for.")
      (progDesc "Generate an AoC solution component.")

dayNumber :: String -> Parser Int
dayNumber helpMsg =
  option
    auto
    ( long "day"
        <> short 'd'
        <> help helpMsg
        <> metavar "INT"
    )

parseOptions :: IO Command
parseOptions =
  execParser $
    info
      (opts <**> helper)
      ( fullDesc
          <> progDesc "CLI utility make it easier to use Haskell for AoC."
      )
  where
    opts =
      hsubparser
        ( command "generate" generateCommand
            <> command "fetchInput" fetchInputCommand
        )
