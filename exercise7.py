#Ask the user to input 5 numbers. Use a loop and if statements to find and print the largest number.
numbers_list=[]
print("Please enter 5 numbers")
large=None
for i in range(5):
    while True:
        try:
            user_input=input(f"Enter number {i+1} ")
            number=int(user_input)
            numbers_list.append(number)
            
            break
        except ValueError:
            print("Invalid value.Please enter an integer")   
            break 
    if large is None or number>large:
                large=number
if large is not None:                
                print(f"{large} is the largest number")        