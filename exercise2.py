#Sum until 0
numbers=[]
user_input=None
print("Enter numbers to sum.Enter 0 to exit.")
while user_input !=0:
    try:
        user_input=int(input("Please enter any number "))
        if user_input!=0:
            numbers.append(user_input)
    except ValueError:
        print("Invalid input.Please enter a number ")
        
total_sum=sum(numbers)   
print(f"The sum of the numbers you entered is {total_sum}")    

