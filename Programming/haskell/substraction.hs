-- EXPLICIT/ LITERAL EXPRESSIONS - SUBTRACTION
subtractIntegers :: Integer -> Integer -> Integer
subtractIntegers x y = x - y

-- PROGRAM
main :: IO ()
main =  do

-- THIS "putStr command will do whatever you tell the teleprompter to write immediately.
putStr "Reduce x by y using a - sign ="
print(subtractIntegers 1738 12)

-- https://www.tutorialspoint.com/compile_haskell_online.php