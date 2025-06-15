'''Set a predefined password (e.g. 'python123'). Ask the user to guess it using a while loop. Give them
3 chances'''
CORRECT_PASSWORD= "python123"
MAX_ATTEMPTS=3
attempts_made=0
while attempts_made < MAX_ATTEMPTS:
 guess=input("Enter your password: ")
 attempts_made +=1
 if guess==CORRECT_PASSWORD:
  print("Correct,you're now looged in")
  break #Exits the loops immediately on success
 elif attempts_made < MAX_ATTEMPTS:
  print(f"Password incorrect,you have {MAX_ATTEMPTS - attempts_made} attempts remaining.Try again")
  
 else:
  print(f"You have exceeded your {MAX_ATTEMPTS} attempts.Access denied")
 