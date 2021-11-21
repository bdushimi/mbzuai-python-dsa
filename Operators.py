#Operators



#Numeric Operators
"""

Python supports different types of arithmetic operations 
that can be performed on literal numbers, variables, or some combination. 

The primary arithmetic operators are:

+ for addition
- for subtraction
* for multiplication
/ for division
% for modulus (returns the remainder)
** for exponentiation
"""

#TO-DO
#Create a variable "result" that would store arithmetic operation on two numbers of your choice.
#Try out an arithmetic operator you have not used
#Print the "result" variable

"""
Precedence : refers to the order of operations
Read more here : https://www.programiz.com/python-programming/precedence-associativity

An arithmetic expression containing different operators will be computed on the basis of operator precedence.
Whenever operators have equal precedence, the expression is computed from the left side
"""

# Different precedence
#print(10 - 3 * 2)  # Multiplication computed first, followed by subtraction

# Same precedence
#print(3 * 20 / 5)  # Multiplication computed first, followed by division
#print(3 / 20 * 5)  # Division computed first, followed by multiplication

#T0-D0
#What should the code below output?
#print((4 * 2) + 6 / 3 - 2)


#Comparison Operators
"""
Comparison operators can be used to compare values in mathematical terms
The result of a comparison is always a bool.
If the comparison is correct, the value of the bool will be True. Otherwise, its value will be False


< less than
> greater than
<= less than or equal to
>= greater than or equal too
== equal to
!= not equal to
"""
#Few examples
# num1 = 5
# num2 = 10
# num3 = 10
# print(num2 > num1)  # 10 is greater than 5
# print(num1 > num2)  # 5 is not greater than 10

# print(num2 == num3)  # Both have the same value
# print(num3 != num1)  # Both have different values

# print(3 + 10 == 5 + 5)  # Both are not equal
# print(3 <= 2)  # 3 is not less than or equal to 2


#Logical Operators
"""
Logical operators are used to combine conditional statements

and : returns True if both statements are True
or : returns True if one of the statements is True
not : returns True if the statement is False
"""

#Few examples
# x = 5
# print(x > 3 and x < 10)

#identity operators
"""
They are used to check if two values (or variables) are located on the same part of the memory. 
Two variables that are equal does not imply that they are identical.


'is' True if the operands are identical (refer to the same objects).
'is not' True if the operands are not identical (do not refer to the same object)
"""

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
x3 = [1,2,3]
y3 = [1,2,3]

# print(x is z)
# returns True because z is the same object as x

# print(x is y)
# returns False because x is not the same object as y, even if they have the same content

# print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# print(x3 is y3)
# Output: False
#x3 and y3 are lists. They are equal but not identical. 
# It is because the interpreter locates them separately in memory although they are equal.