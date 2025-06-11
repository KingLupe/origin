#Ask the user for a number. Use a while loop to reverse the digits and print the result.
def reverse_number():
    while True:
        try:
            num_str=input("Enter a non-negative integer")
            num=int(num_str)
            if num<0:
                print("Please enter a non-negative integer")
            else:
                break
            
        except ValueError:
            print("Invalid input.Please enter an integer")   
    reversed_num_str=""  
    temp_num=num
    while temp_num > 0:
        digit=temp_num % 10
        reversed_num_str += str(digit)
        temp_num //=10
    print(f"The reversed number is :{reversed_num_str}")    


if __name__=="__main__":
    reverse_number()
            

            