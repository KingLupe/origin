#Using a for loop, print numbers from 1 to 50. But print 'Fizz' for multiples of 3, 'Buzz' for multiples of 
# 5, and 'FizzBuzz' for both.
for x in range(1,51):
   if x%3==0 and x%5==0:
     print(f"{x} FizzBuzz")
   elif  x%3==0 :
      print(f"{x} Fizz")
   elif x%5==0:
      print(f"{x} Buzz")
   else:
      print(x)

