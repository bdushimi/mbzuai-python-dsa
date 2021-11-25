# TOPIC : MULTI-DIMENSIONAL LIST/ARRAY

# Multidimensional Array/List concept can be explained as a technique of defining and storing the data on a format 
# with more than one dimension (i.e. more than one dimension of data).



# In nutshel, when a list has other lists in as elements, 
# it forms a multidimensional list or array. 

# For example:
List = [ [1, 2], [2,5], [5,1] ]



# Accessing multidimensional data is done by using the indexing operator. 
# The elements of the outer list can be accessed using the index of the outer list.


#For example:
# print(List[0]) # [1, 2]

# The elements of the inner list can be accessed using the index of the inner list.
# Add one more square bracket to access its elements 

# print(List[0][0]) # 1

# Access multi-dimensional list with the help of loop.
# for record in List:
#     print(record)

# Access multidimensional list using square brackets and for loop

# for i in range(len(List)) : # len(List) is the length of the outer list 
#     for j in range(len(List[i])) :  # len(List[i]) is the length of the inner list
#         print(List[i][j], end=" ") 
#     print()


# Methods on Multidimensional lists

# Add a sublist to a multidimensional list
# List.append([20, 25])
# print(List)


# Extend a sublist 
# List[0].extend([11, 33])
# print(List)


# Practical Example : Matrices

# In Python, we can implement a matrix as a nested list (list inside a list). 
# We can treat each element as a row of the matrix.

# Program to add two matrices using nested loop

# X = [[6,4,-1],
#     [14 ,0,6],
#     [3 ,8,1]]

# Y = [[2,8,1],
#     [4,5,3],
#     [9,5,1]]

# result = [[0,0,0],
#          [0,0,0],
#          [0,0,0]]

# for i in range(len(X)):
#    for j in range(len(X[0])):
#        result[i][j] = X[i][j] + Y[i][j]

# for r in result:
#    print(r)

# Program to transpose a matrix using a nested loop
# Transpose of a matrix is obtained by swapping the rows and columns of the matrix.


# X = [[6,2],
#     [8 ,4],
#     [9 ,0]]

# result = [[0,0,0],
#          [0,0,0]]

# # iterate through rows
# for i in range(len(X)):
#    # iterate through columns
#    for j in range(len(X[0])):
#        result[j][i] = X[i][j]

# for r in result:
#    print(r)


 

