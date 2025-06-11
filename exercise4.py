#Password guessing game.
password= "python123"
attempts=0
while attempts<3:
 guess=input("Enter your password: ")
 attempts+=1
 if guess==password:
  print("Correct,you're now looged in")
  break
 elif attempts==3:
  print("You've exceeded your attempts")
  
 else:
  print("password incorrect,try again")
 