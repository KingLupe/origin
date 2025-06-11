#Ask the user for a number n. Use a for loop to print how many numbers from 1 to n are divisible by 3 or 5.
n_str=input("Enter a positive integer 'n': ")
try:
    n=int(n_str)
    if n<=0:
        print("Please enter a positive integer")
        exit()
except ValueError:
    print("Invalid input.Please enter a positive integer")   
    exit()    
count=0

for i in range(1,n+1) :
    if i%3==0 or i%5==0:
        count+=1
print(f"There are {count} numbers from 1 to {n} that are divisible by 3 or 5 ")        


