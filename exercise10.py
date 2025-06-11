'''Ask the user for a number. Use a for loop and if statements to determine if it's a prime number.'''
n=int(input("Please enter a number: "))
is_prime=True

if n <=1:
    is_prime=False
else:    
  for x in range(2,int(n**0.5) + 1):
    if n % x != 0:
        is_prime=True
        print(f"{n} is a prime number")
    else:
         
         print(f"{n} is not a prime number")  
    break