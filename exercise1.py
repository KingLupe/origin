#Ask the user to enter 10 numbers (using a for loop). For each number, print whether it is even or odd
#(use if/else).
NUM_COUNT=10
numbers_list=[]
print(F"Please enter {NUM_COUNT} numbers")
for i in range(NUM_COUNT):
  while True:
        try:
            user_input =input(f"Enter number {i+1}: ")
            number=int(user_input)
            numbers_list.append(number)
            if number%2==0:
                print(f"{number} is an even number") 
            else:
                print(f"{number} is an odd number")  
            break #Exits the inner while loop once a valid number is entered.
        except  ValueError:
                print("Invalid input.Please enter a valid whole number(e.g 4,7,-7)")
        except Exception as e:
                 print(f"An unexpected error occurred: {e}. Please try again.")
       
print("\nThanks,here are the 10 numbers you entered")   
for num in numbers_list:
     print(num,end=" ") #Prints numbers on one line separated by a space.
print() #adds a newline at the end.           
