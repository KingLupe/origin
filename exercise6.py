#Using a for loop, print numbers from 1 to 50. But print 'Fizz' for multiples of 3, 'Buzz' for multiples of 
# 5, and 'FizzBuzz' for both.
for number in range(1,51):
   output=""
   if number %3==0: 
    output +="Fizz"    
   if number %5==0:
    output +="Buzz"
     # If output is still empty, it means no conditions were met, so print the number
   if output: # This checks if the 'output' string is not empty
        print(output)
   else:
        print(number)

