#What is a functions
"""
A set of reusable operations.

You can pass data, known as parameters, into a function.

A function can return data as a result.


"""

#Why use functions
"""
Think of a function as a box which performs a task. We give it an input and it returns an output.

We don’t need to write the set of instructions again for a different input, we could just call the function again.

Functions are useful because they make the code concise and simple.
"""

#Suppose we want to find the smaller value between two integers:
# num1 = 10
# num2 = 40
# if num1 < num2:
#     minimum = num1
# else:
#     minimum = num2
# print(minimum)

# num1 = 250
# num2 = 120
# if num1 < num2:
#     minimum = num1
# else:
#     minimum = num2
# print(minimum)

# num1 = 100
# num2 = 100
# if num1 < num2:
#     minimum = num1
# else:
#     minimum = num2
# print(minimum)

#Solution with min() function
# minimum = min(10, 40)
# print(minimum)

# minimum = min(10, 100, 1, 1000)  # It even works with multiple arguments
# print(minimum)

# minimum = min("Superman", "Batman")  # And with different data types
# print(minimum)


#user defined function
"""
Keyword def that marks the start of the function header.

A function name to uniquely identify the function. Function naming follows the same rules of writing identifiers in Python.

Parameters (arguments) through which we pass values to a function. They are optional.

A colon (:) to mark the end of the function header.

Optional documentation string (docstring) to describe what the function does.

One or more valid python statements that make up the function body. Statements must have the same indentation level (usually 4 spaces).

An optional return statement to return a value from the function
"""

# def greet(name):
#     """
#     This function greets to
#     the person passed in as
#     a parameter
#     """
#     print("Hello, " + name + ". Good morning!")


#How to call a function in python?
"""
Once we have defined a function, we can call it from another function, program, or even the Python prompt. 
To call a function we simply type the function name with appropriate parameters.

Note: In python, the function definition should always be present before the function call
"""
# greet('Peter')

#Scope and Lifetime of variables
"""
Scope of a variable is the portion of a program where the variable is recognized. 
Parameters and variables defined inside a function are not visible from outside the function. 
Hence, they have a local scope.

The lifetime of a variable is the period throughout which the variable exists in the memory.
 The lifetime of variables inside a function is as long as the function executes.

They are destroyed once we return from the function. 
Hence, a function does not remember the value of a variable from its previous calls.

"""

#Example to illustrate the scope of a variable inside a function.
# def my_func():
# 	x = 10
# 	print("Value inside function:",x)

# x = 20
# my_func()
# print("Value outside function:",x)



#Excercise
"""
In this exercise, you must implement the rep_cat function. 
You are given two integers, x and y, as arguments. 
You must convert them into strings. 
The string value of x must be repeated 10 times and the string value of y must be repeated 5 times.

At the end, y will be concatenated to x and the resulting string must returned.

Sample Input #
x = 3
y = 4

Sample Output #
'333333333344444'
"""