#Conditional Statements
"""
To handle conditional statements, Python follows a particular convention:

if condtional statement is True:
    # execute expression1
    pass
else:
    # execute expression2
    pas
"""

#If statement
"""
if the condition holds True, execute the code to be executed. Otherwise, skip it and move on.
Keep the indentation correct. Python uses indentation to highlight the blocks of code instead of curly braces.
By default, Python uses four spaces for indentation

"""

#Few examples

#Simple if statement

num = 5
# if (num == 5):  # The condition is true
#     print("The number is equal to 5")  # The code is executed

# if num > 5:  # The condtion is false
#     print("The number is greater than 5")  # The code is not executed


"""
You can use logical operators to create more complex conditions in the if statement. 
For example, you may want to satisfy multiple clauses for the expression to be True.
"""

num = 12
# if num % 2 == 0 and num % 3 == 0 and num % 4 == 0:
#     # Only works when num is a multiple of 2, 3, and 4
#     print("The number is a multiple of 2, 3, and 4")

# if (num % 5 == 0 and num % 6 == 0):
#     # Only works when num is either a multiple of 5 or 6
#     print("The number is a multiple of 5 and/or 6")

"""
Nested if Statements
"""
# num = 73

# if num >= 0 and num <= 100:
#     if num >= 50 and num <= 75:
#         if num >= 60 and num <= 70:
#             print("The number is in the 60-70 range")


# if-else statement 

# num = 60
# if num <= 50:
#     print("The number is less than or equal to 50")
# else:
#     print("The number is greater than 50")


#Conditional Expressions 
"""
Conditional expressions use the functionality of an if-else statement in a different way.
The expression returns an output based on the condition we provide. This output can be stored in a variable.

A conditional expression can be written in the following way:

output_value1 if condition else output_value2
"""

# num = 60
# output = "The number is less than or equal to 50" \
#     if num <= 50 else "The number is greater than 50"

# print(output)


#The if-elif-else Statement
"""
It allows us to create multiple conditions easily.
elif stands for else if, indicating that if the previous condition fails, try this one.
"""

# Let’s write an if-elif-else 
# statement which checks the state of a traffic signal and generates the appropriate response:

# light = "Red"

# if light == "Green":
#     print("Go")

# elif light == "Yellow":
#     print("Caution")

# elif light == "Red":
#     print("Stop")

# else:
#     print("Incorrect light signal")



"""
An important thing to keep in mind is that an 'if-elif-else or if-elif' statement IS NOT 
the same as multiple if statements. if statements act independently.

If the conditions of two successive ifs are True, both statements will be executed.

On the other hand, in if-elif-else, when a condition evaluates to True, 
the rest of the statement’s conditions are not evaluated.
"""

#If example
# num = 10
if num > 5:
    print("The number is greater than 5")
if (num % 2 == 0):
    print("The number is even")
if (not num % 2 == 0):
    print("The number is odd")


# if-elif-else example
# num = 10
# if num > 5:
#     print("The number is greater than 5")
# elif num % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd and less than or equal to 5")

