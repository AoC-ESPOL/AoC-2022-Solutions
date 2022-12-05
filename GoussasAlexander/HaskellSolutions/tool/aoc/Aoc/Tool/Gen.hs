module Aoc.Tool.Gen (generateComponentForDay, Day) where

import           Control.Monad    (unless)

import           Aoc.Tool.Print   (pp, ppErr)

import           Data.List
import           Data.Maybe       (fromJust)
import           System.Directory
import           System.Exit      (exitFailure, exitSuccess)
import           System.FilePath

type Day = Int

generateComponentForDay :: Day -> IO ()
generateComponentForDay day = do
  isCabalProject <- checkCurrentDirIsCabalProject

  unless isCabalProject $ do
    ppErr "Not in a cabal project"
    exitFailure

  createComponentForDay day

  pp "\nFinished creating component.\n"
  pp "Copy this in your cabal file to add the new component to the build:\n"
  pp "In lib:\n"
  pp $ formatForCabalFile $ componentFileNames (fromJust $ directoryForComponent day)
  pp "In the test suite:\n"
  pp $ "   " <> testModuleNameForDay day <> ","
  pp "\n"

-- | 'createDirectoriesForComponent' creates the necessary directories for the new component.
createComponentForDay :: Day -> IO ()
createComponentForDay day = maybe invalidDay createComponent $ directoryForComponent day
  where
    createComponent dirName =
       mapM_
        createComponentFile
        (componentFileNames dirName)
       >> createTestModuleForDay day
    invalidDay = ppErr ("Invalid number for component day: " <> show day) >> exitFailure

-- Source module generation.

-- | 'componentFileNames' returns an array of the component's file names given the component directory.
componentFileNames :: FilePath -> [FilePath]
componentFileNames dirName = map (dirName </>) ["PartOne.hs", "PartTwo.hs", "Common.hs"]

createComponentFile :: FilePath -> IO ()
createComponentFile filepath = do
  fileExists <- doesFileExist filepath
  if fileExists then do
    pp $ "Component file already exists: " <> filepath
    exitSuccess
  else do
    pp $ "Creating component file: " <> filepath
    createDirectoryIfMissing True $ takeDirectory filepath
    writeFile filepath $ createModuleContents (toModuleName filepath)

createModuleContents :: String -> String
createModuleContents moduleName = mconcat
  [ "module " <> moduleName <> " where", "\n\n"
  , if "Common" `isInfixOf` moduleName then "" else "solution :: IO a\nsolution = undefined"
  ]

directoryForComponent :: Day -> Maybe FilePath
directoryForComponent day = (\name -> "lib" </> "Aoc" </> "Day" </> name) <$> nameForDay day

toModuleName :: FilePath -> String
toModuleName =
    drop (length ("lib." :: String))
  . dropExtension
  . map (\c -> if c == '/' then '.' else c)

-- Cabal generation.

-- | 'formatForCabalFile' formats the list of component paths to a shape suitable to paste in
-- the "other-modules" section of the cabal file.
formatForCabalFile :: [FilePath] -> String
formatForCabalFile []     = ""
formatForCabalFile (x:xs) = "   " <> toModuleName x <> ",\n" <> formatForCabalFile xs

-- Test module generation.

createTestModuleForDay :: Day -> IO ()
createTestModuleForDay day = do
  let moduleName = testModuleNameForDay day
      fileName = testModuleFileNameForDay day
      moduleContents = createTestModuleContents moduleName
      filePath = "test" </> fileName
  pp $ "Creating test module: " <> filePath
  writeFile filePath moduleContents

testModuleNameForDay :: Day -> String
testModuleNameForDay day = "Day" <> fromJust (nameForDay day) <> "Spec"

testModuleFileNameForDay :: Day -> FilePath
testModuleFileNameForDay = flip mappend ".hs" . testModuleNameForDay

createTestModuleContents :: String -> String
createTestModuleContents moduleName = mconcat
 [ "module " <> moduleName <> " where\n\n"
 , "import Test.Hspec\n\n"
 , "main :: IO ()\n"
 , "main = hspec spec\n\n"
 , "spec :: Spec\n"
 , "spec = partOneSpec >> partTwoSpec\n\n"
 , "partOneSpec :: Spec\n"
 , "partOneSpec = undefined\n\n"
 , "partTwoSpec :: Spec\n"
 , "partTwoSpec = undefined\n"
 ]

-- Util.

nameForDay :: Day -> Maybe FilePath
nameForDay 1  = pure "One"
nameForDay 2  = pure "Two"
nameForDay 3  = pure "Three"
nameForDay 4  = pure "Four"
nameForDay 5  = pure "Five"
nameForDay 6  = pure "Six"
nameForDay 7  = pure "Seven"
nameForDay 8  = pure "Eight"
nameForDay 9  = pure "Nine"
nameForDay 10 = pure "Ten"
nameForDay 11 = pure "Eleven"
nameForDay 12 = pure "Twelve"
nameForDay 13 = pure "Thirteen"
nameForDay 14 = pure "Fourteen"
nameForDay 15 = pure "Fifteen"
nameForDay 16 = pure "Sixteen"
nameForDay 17 = pure "Seventeen"
nameForDay 18 = pure "Eighteen"
nameForDay 19 = pure "Nineteen"
nameForDay 20 = pure "Twenty"
nameForDay 21 = pure "TwentyOne"
nameForDay 22 = pure "TwentyTwo"
nameForDay 23 = pure "TwentyThree"
nameForDay 24 = pure "TwentyFour"
nameForDay 25 = pure "TwentyFive"
nameForDay _  = Nothing

-- | 'checkCurrentDirIsCabalProject' checks that the current directory is a Cabal project.
checkCurrentDirIsCabalProject :: IO Bool
checkCurrentDirIsCabalProject = any ((== ".cabal") . takeExtension) <$> listDirectory  "."

