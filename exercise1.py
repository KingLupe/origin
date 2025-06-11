#Ask the user to enter 10 numbers (using a for loop). For each number, print whether it is even or odd
#(use if/else).
numbers_list=[]
print("Please enter 10 numbers")
for i in rangge(10):
  while True:
        try:
            user_input =input(f"Enter number {i+1}: ")
            number=int(user_input)
            numbers_list.append(number)
            if number%2==0:
                print(f"{number} is an even number") 
            else:
                print(f"{number} is an odd number")  
            break
        except  ValueError:
                print("Invalid input.Please enter a valid whole number")
        except Exception as e:
                 print(f"An unexpected error occurred: {e}. Please try again.")
       
print("Thanks,here are the 10 numbers you entered")          
