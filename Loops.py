#Loops
"""
One of the biggest applications of loops is traversing data structures, e.g. lists, tuples, sets, etc. 
In such a case, the loop iterates over the elements of the data structure while performing a set of operations each time
"""

#The for Loop
"""
A for loop uses an iterator to traverse a sequence, e.g. a range of numbers, the elements of a list, etc. 
In simple terms, the iterator is a variable that goes through the list.

The iterator starts from the beginning of the sequence. 
In each iteration, the iterator updates to the next value in the sequence.

Structure:

for val in sequence:
    loop body


Here, val is the variable that takes the value of the item inside the sequence on each iteration.
Loop continues until we reach the last item in the sequence. 
The body of for loop is separated from the rest of the code using indentation.
"""


#Looping through a list of items
# Program to find the sum of all numbers stored in a list

# List of numbers
# numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
# sum = 0

# iterate over the list
# for val in numbers:
    # sum = sum+val

# print("The sum is", sum)


#Looping through a sequence created by range function
"""
In Python, the built-in range() function can be used to create a sequence of integers. 
This sequence can be iterated over through a loop. 

A range is specified in the following format:
range(start, end, step)

'The end' value is not included in the list.

If the start index is not specified, its default value is 0.

'The step' decides the number of steps the iterator jumps ahead after each iteration. 
It is optional and if we don’t specify it, the default step is 1, 
which means that the iterator will move forward by one step after each iteration.
"""

#Check if a number is even or odd
# for i in range(1, 11):  # A sequence from 1 to 10
#     if i % 2 == 0:
#         print(i, " is even")
#     else:
#         print(i, " is odd")


# A loop changes when the step component of a range is specified
# for i in range(1, 11, 3):  # A sequence from 1 to 10 with a step of 3
#     if i % 2 == 0:
#         print(i, " is even")
#     else:
#         print(i, " is odd")


#Let’s double each value in a list using a for loop using the range function
# float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
# print(float_list)

# for i in range(0, len(float_list)):  # Iterator traverses to the last index of the list
#     float_list[i] = float_list[i] * 2

# print(float_list)



#The while loop
"""
The while loop keeps iterating over a certain set of operations as long as a certain condition holds True.
It operates using the following logic: While this condition is true, keep the loop running
"""

#Basic while loop
# a=0
# while a < 10:
# 	print (a)
# 	a+=1



#Let's find if a number is even or odd using a while loop
# a = 1
# while a < 10:
#     if a % 2 == 0:
#         print(a, " is even")
#     else:
#         print(a, " is odd")
#     a += 1



#Cautionary Measures 
"""
Compared to for loops, we should be more careful when creating while loops. 
This is because a while loop has the potential to never end. This could crash a program!

For instance:

while(True):
    print("Hello World")

x = 1
while(x > 0):
    x += 5
"""


#Nested for Loop
"""
A nested loop is a loop inside a loop.
Use case : compare every element in a list with the rest of the elements in the list
"""

#Example :  print two elements whose sum is equal to a certain/given number
# n = 50
# num_list = [10, 4, 23, 6, 18, 27, 47]

# for n1 in num_list:
#     for n2 in num_list:  # Now we have two iterators
#         if(n1 + n2 == n):
#             print(n1, n2)


# The break Keyword
"""
The break statement ends the loop.
The break statement can be used inside a loop or in a function.

Use case : 

If you want to exit the loop because you have found what 
you were looking for and don’t need to make any more computations in the loop
"""

# n = 50
# num_list = [10, 4, 23, 6, 18, 27, 47]
# found = False  # This bool will become true once a pair is found

# for n1 in num_list:
#     for n2 in num_list:
#         if(n1 + n2 == n):
#             found = True  # Set found to True
#             break  # Break inner loop if a pair is found
#     if found:
#         print(n1, n2) # Print the pair
#         break  # Break outer loop if a pair is found

#The continue Keyword#
"""
The continue statement instructs a loop to continue to the next iteration. 
Any code that follows the continue statement is not executed. 

Unlike a break statement, a continue statement does not completely halt a loop
"""

# subjects = ["ML101", "DSA101", "WebDev101", "Statistics101"]

# for subject in range(0, len(subjects)):
#     if subjects[subject] == "DSA101":
#         continue
#         print(subjects[subject])
#     else:
#         print(subjects[subject])


#The pass Keyword
"""
In all practical meaning, the pass statement does nothing to the code execution. 
It can be used to represent an area of code that needs to be written. 
Hence, it is simply there to assist you when 
you haven’t written a piece of code but still need your entire program to execute.

"""
# num_list = list(range(20))
# for num in num_list:
#     pass # You can write code here later on

# print(num_list) 