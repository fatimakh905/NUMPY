import numpy as np

# Creating two 2D array and finding common items
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[5, 6, 7], [8, 9, 10], [11, 12, 13]])
common_elements = np.intersect1d(a, b)
print("Common elements:", common_elements)

# Removing all items in a that are present in b
a_removed = np.setdiff1d(a, b)
print("Array a after removing elements present in b:", a_removed)

# Reversing the columns of a 2D array arr
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr_reversed = arr[:, ::-1]
print("Array with reversed columns:\n", arr_reversed)

# Creating a 2D array of shape 5x3 with random decimal numbers between 5 and 10
random_array = 5 + 5 * np.random.random((5, 3))
#This method is used to generate random numbers between 0 and 1 but here we have generated decimalnumbers
#b/w 5 and 10.It will generate decimal numbers 0-5 theen it will add the numbers with 5.Now the numbers will 
#be b/w 5 and 10.
print("Random 5x3 array with decimals between 5 and 10:\n", random_array)

# Creating a 5x5 matrix with values 1, 2, 3, 4 just below the diagonal
below_diagonal_matrix = np.diag(np.arange(1, 5), k=-1)
print("5x5 matrix with values 1,2,3,4 just below the diagonal:\n", below_diagonal_matrix)

# PART 3: Creating the pattern using only numpy functions
a = np.array([1, 2, 3])
repeat_elements = np.repeat(a, 3)  #Repeat each element three times.
tile_elements = np.tile(a, 3)       #Repeat all the three numbers like 1,2,3
pattern = np.concatenate((repeat_elements, tile_elements))  #joining both arrays

print("Pattern array:", pattern)
