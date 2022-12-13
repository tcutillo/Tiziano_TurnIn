main = do   
   let var = 24 
   
   -- HERE IS SIMILAR TO MODULO
   
   if var `rem` 2 == 0 
      then putStrLn "Number is Even" 
   else putStrLn "Number is Odd"