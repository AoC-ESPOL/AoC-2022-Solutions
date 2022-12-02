module Aoc.Util where

tupled :: (Applicative a) =>  a b -> a c -> a (b, c)
tupled b c = (,) <$> b <*> c
