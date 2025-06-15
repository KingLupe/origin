'''Ask the user to input a string. Count how many characters are letters and how many are digits using
a for loop and if statements'''

input_string = input("Please enter a string (can include letters, numbers, and symbols): ")

digit_count = 0
letter_count = 0

for char in input_string:
    if char.isdigit():
        digit_count += 1
    elif char.isalpha():
        letter_count += 1
    # You could add an 'else' here if you want to count other characters (symbols, spaces)
    # else:
    #     # handle other characters if needed
    #     pass

print(f"The string '{input_string}' contains:")
print(f"- {letter_count} letters")
print(f"- {digit_count} digits")