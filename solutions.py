import math

# Challenge 1
# Write a program that prints out all the elements of the list "numbers" that are less than 5.

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# def printLessThan5(numbers):
#     for number in numbers:
#         if (number < 5):
#             print(number)
            
            
# #invote printLessThan5 function
# printLessThan5(numbers)

# Challenge 2
# Write a Python program which will return true 
# if the two given integer values are equal or their sum or difference is 5.

# def randonFunction(num1, num2):
#     if num1 == num2 or num1+num2 == 5 or abs(num1-num2) == 5: 
#         return True
#     else: 
#         return False
    
    
# print(randonFunction(2,2))


#Challenge 3:
#Write a Python program to compute the distance between the points (x1, y1) and (x2, y2)

# def computeDistance(x1, y1, x2, y2):
#     return math.sqrt(((x2-x1)**2) - ((y2-y1)**2))
    
# print(round(computeDistance(1,2,5,1),2))

#Challenge 4:
# Define a function named count that takes a single parameter. 
# The parameter is a string. The string will contain a single word divided into syllables by hyphens, such as these: "ba-na-na", "Data", "me-ta"
# Your function should count the number of syllables and return it.
# The call count("ho-tel") should return 2

# def numOfWords(string):
#     hyphensCount=0
#     for char in string:
#         if(char == "-"):
#             hyphensCount += 1
#     if(hyphensCount > 0):
#         hyphensCount += 1
#         return hyphensCount
#     else:
#         hyphensCount += 1
#         return hyphensCount
        
# print(numOfWords("ho-tel-serena"))

#Challenge 5:
# Define a function named up_down that takes a single number as its parameter. 
# Your function return a tuple containing two numbers; the first should be one lower than the parameter, and the second should be one higher.
# For example, calling up_down(0) should return (-1, 1).

# def up_down(number):
#     lower = number - 1
#     upper = number + 1
#     up_down_pair = (lower, upper)
#     return up_down_pair

# print(up_down(4))

#Challenge 6:
#Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones
#Your function should return the number of consecutive zeros in the string
#For instance, with this input "10011010001100", the function will return 3

# def consecutive_zeros(string):
#     maxCount = 0
#     zerosCount = 0
#     for val in string:
#         if val == "0":
#             zerosCount += 1
#         else:
#             if maxCount < zerosCount:
#                 maxCount = zerosCount
#             zerosCount = 0
#     if maxCount < zerosCount:
#         maxCount = zerosCount
    
#     return maxCount
    
# print(consecutive_zeros("10011010001100000"))
# print(consecutive_zeros("10011010001100"))


#Challenge 7:
# Write a Python program to check whether variable is integer or string or float.
# def checkType(data):

#     if "str" in str(type(data)):
#         print(data, "is a string")
#     if "int" in str(type(data)):
#         print(data, "is an integer")
#     if "float" in str(type(data)):
#         print(data, "is a float")

# checkType("2")
# checkType(2)
# checkType(2.0)

#Challenge 8:
# Write a Python program to count and display the vowels of a given text.

# def countVowels(str):
#     vowelsCount=0
#     for char in str:
#         if char == "o" or char == "i" or char == "e" or char == "u" or char == "a":
#             vowelsCount += 1
#     return vowelsCount
    
# print(countVowels("Judge James"))
# print(countVowels("dhfgty"))


#Challenge 9:
#Write a Python program to count the occurrences of each characher in a given sentence

# def countCharFreq(str):
#     #create an dictionary
#     nums_dic = {}
#     for char in str:
#         char = char.lower()
#         if char.rstrip() != "" and not nums_dic.get(char):
#             nums_dic[char]=1
#         elif nums_dic.get(char) :
#              nums_dic[char] += 1
#     print(nums_dic)
    
# countCharFreq("Data")
# countCharFreq("God is Good and Amazing")


#Challenge 10:
# Write a Python program which solve the equation:
# ax+by=c
# dx+ey=f
# Print the values of x, y where a, b, c, d, e and f are given.

#Solved using Determinants approach
# def resolve(a,b,c,d,e,f):
    
#     #The value of this determinant is found by finding the difference between 
#     # the diagonally down product and the diagonally up product
#     D = a*e - b*d
    
#     if D != 0:
        
#         # The x‐determinant or Dx is formed by taking the constant terms 
#         # from the system and placing them in the x‐coefficient positions and retaining the y‐coefficients.
        
#         Dx = (c*e - b*f)
#         x = Dx / D
        
#         # The y-determinant or Dy is formed by taking the constant terms 
#         # from the system and placing them in the y‐coefficient positions and retaining the x‐coefficients.

#         Dy = (a*f - c*d)
#         y = Dy / D
        
#         print(x, y)

# resolve(1,2,4,3,-5,1)

#Assignment Day 1:
#Problem statement:
"""
The Fibonacci sequence is a series of numbers where every number is the sum of the two numbers before it. 
The first two numbers are 0 and 1:

You must write the fib() function which takes in a positive integer, n, and returns the n-th Fibonacci number. 
Your function must use any of the loops (for loop or while loop).

Sample input
n=7

Sample output
8
"""

# def fib(n):
#     # The first and second values will always be fixed
#     first = 0
#     second = 1

#     if n < 1:
#         return -1

#     if n == 1:
#         return first

#     if n == 2:
#         return second

#     count = 3  # Starting from 3 because we already know the first two values
#     while count <= n:
#         fib_n = first + second
#         first = second
#         second = fib_n
#         count += 1  # Increment count in each iteration
#     return fib_n


# n = 3
# print(fib(n))










    
    



