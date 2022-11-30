{-# LANGUAGE LambdaCase #-}

module Main where

import Aoc.Tool.Gen (generateComponentForDay)
import Aoc.Tool.Input (fetchInputForDay)
import Aoc.Tool.Options

main :: IO ()
main =
  parseOptions >>= \case
    Generate genOpts -> generateComponentForDay (optDayNumber genOpts)
    FetchInput fetchOpts -> fetchInputForDay (getDay fetchOpts)
