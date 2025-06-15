'''Repeatedly ask the user to enter a number using a while loop. Add the numbers together. Stop
when the user enters 0. Then print the total sum'''
numbers=[]
print("Enter numbers to sum.Enter 0 to exit.")
while True: # Use an infinite loop and break explicitly
    try:
        user_input_str=input("Please enter any number ")
        # Check if the user entered '0' to exit
        if user_input_str== '0':
            break #Exit the loop
        number=int(user_input_str)
        numbers.append(number)
    except ValueError:
        print("Invalid input.Please enter a number e. g 4,6,7 ")
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Please try again.")
        
total_sum=sum(numbers)   
print(f"The sum of the numbers you entered is {total_sum}")    

