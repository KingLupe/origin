1. What is the correct command to check the installed Python version? 
    python --version

2. What symbol is used to write a single-line comment in Python? 
    hash symbol #

3. What file extension is used for Python files?
    .py

4.  Write a Python command that prints 'Hello World!'.
    print("'Hello World!'")

5.  What does REPL stand for? 
    Read-Eval-Print-Loop

6.  What is the output of 3 + 4 * 2?
    11

7.  Which method exits the interactive shell in Python?
    exit() or quit()

8.  What does the following code print? print('Python' * 2) 
    PythonPython

9.  Which command do you use to run a Python script in the terminal? 
    you use the python command followed by the name of your script file. e,g python exercise1.py

10. Write a comment in Python describing the line print('Hi'). 
    #Prints the word Hi

11. Which of the following is a valid variable name? a) 1st_name b) firstName c) @name d) name$  
     b

12. What type is returned by the expression: type(3.14)? 
     float

13. True or False: Python variables are case-sensitive.
    True

14. What does is_learning = True assign to the variable?
    It assigns the Boolean value True to the variable is_learning

15. Fill in the blank: Strings are enclosed in ________ or ________ quotes. 
    Single ' ' or Double " "  

16. What will len('Python') return?
     6,the number of characters in the word 'Python'

17. Concatenate 'Hello' and 'World' with a space in between using + operator. 
    'Hello'+' '+'World'

18. What is the difference between float and int in Python? 
    int is a whole number while float is a decimal number.

19. Write a variable assignment for your favorite book title.
    myFavouriteBook="Animal Farm"

20. Write a print statement that outputs your age using an f-string.
    print(f"I am {26} years old") 

21. What is the result of 7 // 3? 
     2

22. Which operator is used for exponentiation in Python?
     **

23. What does 10 % 3 evaluate to?
     1

24. Write a code snippet that takes two inputs and prints their sum.
    first_number=int(input("Please enter a number: "))
    second_number=int(input("Please enter another number: "))
    sum=first_number+second_number
    print(f"The sum of {first_number} and {second_number} is {sum}")

25. What will the expression 5 == 5 return?
    True

26. What does not True evaluate to? 
    False

27. Which operator returns True if at least one condition is true?
     or

28. How do you convert a string '123' into an integer? 
    by using the int() function i.e int('123')

29. What happens if you try to convert 'abc' to int using int('abc')? 
    You get a ValueError

30. Write a program that asks for a user's name and says Hello.
    user_input=input("What is your name ?")
    print(f"Hello {user_input}")

31. Write a conditional that checks if a number is greater than 100. 
    user_input=input("Kindly enter a number ")
    number=int(user_input) 
    if number > 100:
        print(f"{number} is greater than 100")
    elif number== 100:
        print(f"{number} is equal to 100")
    else:
        print(f"{number} is not greater than 100")

32. What keyword is used for multiple conditions besides if?
        Elif
33. What will the following output?
      x = 10
        if x < 5:
            print('Small')
        else:
            print('Large')   
     Large

34. Write a program that prints numbers from 1 to 5 using a for loop.
     for x in range (1,6):
       print(x) 

35. What does range(3, 7) generate?
     3,4,5 and 6   

36. What loop type continues as long as a condition is true? 
     while loop

37. What keyword exits a loop early?
     break

38. Write a loop that prints even numbers from 2 to 10.
    for x in range(2,11):
       if x % 2==0:
         print(x)

39. What does continue do in a loop?
    The continue keyword in a loop in Python is used to skip the rest of the current iteration of the loop and move to the next iteration.

40. Write a while loop that runs while a variable count is less than 3.
    count=2
    attempts_made=0
    while attempts_made < count:
        user_input=input("Enter a your username: ")
        attempts_made +=1
        if attempts_made ==count:
            print("You have exhausted your attempts")
            break
        else :
            print("Try one more time,you're remaining with one attempt")   

41. How do you define an empty list?
     []    

42. What index accesses the last item in a list?
    -1

43. What does fruits.append('kiwi') do?
    adds 'kiwi' to the to the end of the fruits list.   

44. What happens if you access an index that does not exist in a list?
    You get an IndexError

45. Write a list called colors with at least 3 color names.
    colors=["red","green","white"]

46. What does list.pop() return?
    The list.pop() method in Python returns the item that was removed from the list.

47. What does in check when used with a list?
    When the in operator is used with a list, it checks for membership.Specifically, it checks if a given element (item) exists within the list. It returns True if the item is found in the list, and False otherwise.

48. How do you sort a list called nums?
    nums.sort()
    print(nums)

49. What does len([1, 2, 3]) return?
    The number of items(elements) in the list.

50. Write a for loop to print each color in the colors list.
    colors=["red","green","white"]
    for x in colors:
      print(x)

51. How do you define a function in Python?
    def greeting()

52. What is the keyword to return a value from a function?
    return

53. Write a function that adds two numbers.
    def add_numbers(x,y):
        sum=x+y 
        return  sum
    x=6
    y=5    
    answer=add_numbers(x,y)
    print(f"The sum of {x} and {y} is {answer}")

54. What is the purpose of a docstring in a function?
    It explains what the function does

55. How do you call a function named greet()?
    greet()  

56. Define a function with a default parameter value.
    def greet(name="Guest"):
        print(f"Hello {name} how you doing today?")
    greet()

57. What will power(2, 3) return if power does exponentiation?
    8

58. Write a function that prints 'Good Morning!'
    def greet():
        print("Goodmorning!")
    greet() 

59. What is the output of this function?
    def square(x):
        return x * x
    print(square(4)) 
    Output will be 16

60. Can a function return multiple values in Python? If yes, how?
   Yes, a function can absolutely return multiple values in Python.Python functions achieve this by returning a single tuple (or sometimes a list or other collection), which then allows you to unpack those values when you call the function.

61. What is a dictionary in Python used for?
   A dictionary in Python is a collection of key-value pairs.Each key is unique and is used to store and retrieve values

62. How do you define an empty dictionary?
    {}

63. Create a dictionary with keys "name", "age", and "city".
    person={
    "name":"Lupeta",
     "age": 30,
    "city":"Lusaka"
    }

64. How do you access the value associated with the key "age" in a dictionary?
    person["age"]

65. What does the .get() method do in a dictionary?
    The .get() method in a Python dictionary is used to retrieve the value associated with a given key.

66. How do you add a new key-value pair to a dictionary?
    person["job"]="Engineer" #Adds a new key "job" with value "Engineer".

67. What does dict.keys() return?
    Returns all keys of the dictionary

68. What happens if you try to access a key that doesn't exist using square brackets ([])?
    You get a KeyError

69. How do you remove a key from a dictionary?
    By using the del function e.g del person["name"] 

70. Write a loop that prints each key and value in a dictionary.
     for key,value in person.items():
       print(key,value)

71. What is a tuple?
    A tuple is an ordered, immutable collection of items.

72. How is a tuple different from a list?
    1. A tuple uses parentheses() syntax whereas a list uses square brackets[]
    2. A tuple is immutable whereas a list is mutable.
    
73. How do you define a tuple with 3 elements?
    my_tuple=("Jesus","my","saviour")

74. Can you change the value of an element in a tuple? Why or why not?
    No.Tuples are immutable.

75. What does len((1, 2, 3)) return?
   3

76. How do you access the second item in a tuple named my_tuple?
    mytuple[1]

77. What happens if you try to append to a tuple?
    AttributeError as tuples are immutable

78. Can tuples contain different data types?
    Yes

79. How do you convert a list to a tuple?
    Use the tuple() finction e.g my_tuple=tuple(my_list)

80. When would you prefer to use a tuple instead of a list?
    1. Tuples are perfect for fixed data e.g days of the week,co-ordinates
    2. When you want to protect your data since tuples are immutable.
    3. When you care about performance since  tuples are faster and use less memory than lists,especially   in large  programs or loops

81. What is a set in Python?
    A set is a built-in data type used to store unordered,unique items.

82. How do you define an empty set?
    empty_set=set()

83. What is the difference between a list and a set?
    1. Lists are ordered whereas sets are unordered
    2. Lists allow duplicates whereas in sets,all items must be unique
    
84. Are sets ordered?
    No

85. Can sets contain duplicate values?
    No

86. How do you add an item to a set?
    my_set.add(3)

87. What does set.remove() do?
    Removes an element from the set.

88. What does set.intersection() return?
    The set.intersection() method in Python returns a new set containing only the elements that are common to all the sets involved in the operation.

89. What does set.union() return?
    The set.union() method in Python returns a new set containing all unique elements from all the sets involved in the operation.

90. When would you use a set in Python?
    Sets are used to store multiple items in a single variable.

91. What does the import keyword do?
    The import keyword in Python is fundamental for code organization and reusability. In essence, it allows you to bring code from one Python module (a .py file) or package (a directory of modules) into your current script or interactive session.

92. Name one built-in Python module.
    exercise1.py

93. How do you import only the sqrt function from the math module?
    from math import sqrt

94. What is the purpose of the random module?
    The random module in Python is used to generate pseudo-random numbers and perform random operations. It provides a variety of functions for different types of randomness needs, from simple integer generation to shuffling sequences and drawing samples from various statistical distributions.

95. Write a program that generates a random number between 1 and 10.
    import random

    random_number1=random.randint(1,10)
    random_number2=random.randint(1,10)

    print(f"The random numbers are {random_number1} and {random_number2}")

96. How do you read input from a user in Python?
    userinput=input("What is your name?")
    print(userinput)

97. What does try-except help with in Python?
    The try-except block in Python is a fundamental mechanism for handling errors and exceptions gracefully. Its primary purpose is to prevent your program from crashing when unexpected events or issues occur during execution.

98. try:
    # Code that might cause a division by zero
    numerator = 10
    denominator = int(input("Enter a denominator (cannot be zero): ")) # Get user input

    result = numerator / denominator
    print(f"The result of the division is: {result}")

except ZeroDivisionError:
    # Code to execute if a ZeroDivisionError occurs
    print("Error: You tried to divide by zero! Please enter a non-zero number.")

except ValueError:
    # It's good practice to also handle cases where input is not a valid number
    print("Error: Invalid input! Please enter a whole number.")

except Exception as e:
    # A general catch-all for any other unexpected errors
    print(f"An unexpected error occurred: {e}")

print("Program continues after the try-except block.")
     
99. What does None represent in Python?
    In Python, None is a special constant that represents the absence of a value or a null value. It's not the same as an empty string (""), a zero (0), or False. It's a unique object, and it's the only value of the NoneType data type.

100. What is the best way to continue learning Python after this test?
    1. Deepen my Understanding of Core Concepts
    2. I need to do a recap on loops