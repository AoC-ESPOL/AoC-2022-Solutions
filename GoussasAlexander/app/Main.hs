module Main where

import Control.Monad (forM_)
import Data.Text (Text)
import Input
import System.Environment (getArgs)

-- NOTE: Add here the solutions for each day.
solveDay :: Int -> Text -> IO (Int, Int)
solveDay _day _input = error "Invalid day"

solve :: Day -> IO ()
solve day = inputForDay day >>= solveDay (toInt day) >>= printSolutions day

printSolutions :: (Show a, Show b) => Day -> (a, b) -> IO ()
printSolutions day (p1, p2) = do
  putStrLn $ "Solutions for day " <> show (toInt day)
  putStrLn $ "Part I:  " <> show p1
  putStrLn $ "Part II: " <> show p2

main :: IO ()
main = do
  args <- getArgs
  if null args
    then putStrLn "Missing required argument 'day:int'"
    else forM_ (parseDay $ head args) solve
