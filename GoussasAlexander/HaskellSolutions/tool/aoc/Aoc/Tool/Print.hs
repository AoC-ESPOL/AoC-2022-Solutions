module Aoc.Tool.Print where

import           System.IO (hPutStrLn, stderr)

-- | 'pp' pretty prints a message to the console.
pp :: String -> IO ()
pp = putStrLn


-- | 'ppErr' pretty prints an error message to the console.
ppErr :: String -> IO ()
ppErr = hPutStrLn stderr
