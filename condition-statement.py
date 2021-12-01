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

# num = 5
# num2 = 20
# if (num == num2):  # The condition is true
#     print("The num is equal to num2")  # The code is executed
# else:
#     print("The num is not equal to num2")

# if num > 5:  # The condtion is false
#     print("The number is greater than 5")  # The code is not executed


"""
You can use logical operators to create more complex conditions in the if statement. 
For example, you may want to satisfy multiple clauses for the expression to be True.
"""

# num = 12
# if num % 2 == 0 and num % 3 == 0 and num % 4 == 0:
#     # Only works when num is a multiple of 2, 3, and 4
#     print("The number is a multiple of 2, 3, and 4")

# if (num % 5 == 0 and num % 6 == 0):
#     # Only works when num is either a multiple of 5 or 6
#     print("The number is a multiple of 5 and/or 6")

"""
Nested if Statements
"""
num = 73

if num >= 0 and num <= 100:
    if num >= 50 and num <= 75:
        if num >= 60 and num <= 70:
            print("The number is in the 60-70 range")


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
# if num > 5:
#     print("The number is greater than 5")
# if (num % 2 == 0):
#     print("The number is even")
# if (not num % 2 == 0):
#     print("The number is odd")


# if-elif-else example
# num = 10
# if num > 5:
#     print("The number is greater than 5")
# elif num % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd and less than or equal to 5")



#Challenge 1

"""
Description: 

A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A

Given a student's marks, write a program that prints the corresponding grade.
"""

#Challenge 2
"""

A student will not be allowed to sit in exam if his/her attendence is less than 75%.

Create variables that hold the following data : 
Number of classes held
Number of classes attended.

Write a program that prints percentage of class attended and 
print if the student is allowed to sit in exam or not.
"""

#Challenge 3

"""
Given a user's first name, write a program that displays the length of their first name. 
Note: To find the length of a string, use the len() function.
"""

#Challenge 4
"""
Given a user's first name and last name. 

Write a program that joins them together with a space between
and display the name and the length of whole name.

Note: 
To find the length of a string, use the len() function.
To join strings, use the + operator.

"""


#Challenge 5
"""
Given user's first name and last name. If the length
of their first name is under five characters, join their first name and last name together 
together (without a space) and display their full names
in upper case. If the length of the first name is five
or more characters, display their first name in
lower case. 

Note:
To join strings, use the + operator.
To convert a string to upper case, use the upper() function.
To convert a string to lower case, use the lower() function.
"""


#Challenge 6
"""
Given the radius of a circle 
Write a program that works out the area of the circle.
"""
