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
print(List[0]) # [1, 2]

# The elements of the inner list can be accessed using the index of the inner list.
# Add one more square bracket to access its elements 

print(List[0][0]) # 1

