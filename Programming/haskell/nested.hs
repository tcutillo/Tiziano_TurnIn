main = do   
   let var = 26 
   
   if var == 0 
      then putStrLn "Number is zero" 
   else if var `rem` 2 == 0 
      then putStrLn "Number is Even" 
   else putStrLn "Number is Odd"