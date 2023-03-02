addIntegers :: Integer -> Integer -> Integer
addIntegers x y = x + y

main :: IO ()
main =  do
putStr "Sum of x + y = "
print(addIntegers 10 25)