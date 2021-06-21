sum_fib :: Int -> Int -> Int -> Int -> Int
sum_fib p n r max = case p + n > max of
    True -> r
    False -> case ((p + n) `mod` 2) of
        0 -> sum_fib n (p+n) (r+p+n) max
        1 -> sum_fib n (p+n) r       max


main :: IO()
main = print $ sum_fib 0 1 0 4000000