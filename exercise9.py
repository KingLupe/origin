'''Ask the user to input a string. Count how many characters are letters and how many are digits using
a for loop and if statements'''

numbers=""
letters=""
str=input("Please input a string: ")
for char in str:
    if char.isdigit():
       numbers+=char
    elif char.isalpha():
       letters+=char   
numbers_len=(len(numbers))
letters_len=(len(letters))
print(f"{str} has {numbers_len} digits and {letters_len} letters")
