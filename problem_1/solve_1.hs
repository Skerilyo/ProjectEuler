sum_mod :: Int -> Int -> Int
sum_mod a b = case b of
    0 -> a
    _ -> if ((b `mod` 3) == 0 || (b `mod` 5) == 0) then
            sum_mod (a + b) (b - 1)
         else
            sum_mod a (b - 1)


main :: IO()
main = print $ sum_mod 0 999