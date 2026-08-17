import numpy as np
#Coverting one d array in matrix
a=np.array([5,6,7,8,9])
matrix=a.reshape(5,1)
print(matrix)
print(a)
print(matrix.base)   #Points to the array which is used to make this array.(Base or original array)

#Reshape returns view of base array.Any change made to new array will be reflected in original array.

#When we create an array using array function,the array owns its data,when we check its base like a .base 
#it will print none means it is not a view of another array.
#When i create an array from another array using rehsape,it is basically the view of original array.
#matrix is the reshaped view of an array.When i check its base ,it will point to original array a.
g=np.array([[4,5,6],[6,7,8]])
flat=g.reshape(-1)
print("Flatten array:",flat)
flat[0]=10                    #Change in new (reshaped array)

print("Shows original array which is reshaped to make this array:",flat.base)
print("New Array after change:",flat)
print("Base array after change in new arary:",g) 
#The returned array of reshape function can be a view or a copy, depending on the memory layout if possible it returns view.

#flatten(),ravel() used to flatten array.
#Flatten returns a copy and ravel returns view whenever possible.



#Indexing for searching elements
b=np.arange(3,12) 
print(b)
print(b[5])

c=np.array([[1,2,3,4],[6,7,8,9]])
print(c[1,])              #To access full row
print(c[:,2])                #To access full column