{-# LANGUAGE DataKinds #-}

module Aoc.Tool.Input (fetchInputForDay) where

import           Aoc.Tool.Print (ppErr)
import           Configuration.Dotenv
import qualified Data.ByteString as BS
import qualified Data.ByteString.UTF8 as BS8
import qualified Data.Text as T
import           Network.HTTP.Req
import           System.FilePath

type Day = Int

type Cookie = String

fetchInputForDay :: Day -> IO ()
fetchInputForDay day =
  getSessionCookie
    >>= maybe
      (ppErr "Failed to load AOC_SESSION cookie from .env file")
      (downloadInputForDay day >> writePuzzleInputToFile day)

writePuzzleInputToFile :: Day -> String -> IO ()
writePuzzleInputToFile day puzzleInput = do
  let fileName = "puzzle-inputs" </> "day" <> show day <.> "txt"
  writeFile fileName puzzleInput

inputUrlForDay :: Day -> Url 'Https
inputUrlForDay dayNumber = https "adventofcode.com/2022/day" /: T.pack (show dayNumber) /: "input"

downloadInputForDay :: Day -> Cookie -> IO (Maybe String)
downloadInputForDay day sessionCookie = runReq defaultHttpConfig $ do
  r <- req GET (inputUrlForDay day) NoReqBody bsResponse (header "Cookie" $ "session=" <> BS8.fromString sessionCookie)
  let response = responseBody r
  pure $
    if BS.null response
      then Nothing
      else Just . BS8.toString $ response

-- | 'getSessionCookie' attempts to retrieve the AOC session cookie from the .env file.
getSessionCookie :: IO (Maybe String)
getSessionCookie = lookup "AOC_SESSION" <$> loadFile defaultConfig
