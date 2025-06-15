#Multiplication Table
print("Enter a number to get it's multiplication table up to 10")
try: 
 user_input=int(input("Please enter a number: "))
except ValueError:
  print("Invalid value pleease enter a whole number") 
  exit()

  

for i in range(1,11):
 result=user_input*i
 print(f"{user_input} X {i} = {result}")

 

 