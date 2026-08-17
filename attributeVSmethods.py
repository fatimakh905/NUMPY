import numpy as np
#Attributes hold the state of object,Do not perform any specific task,Accessed without paranthesis
aa=np.array([[[1,2,3],[4,5,6]],[[5,6,7],[0,4,1]]])



print(aa)
print("Shape of array:",aa.shape)
print("Size of array:",aa.size)
print("Data type of array:",aa.dtype)
print("Number of dimensions:",aa.ndim)
print("Bytes allocated:",aa.itemsize)
print("Transpose:",aa.T) #T seems like a method  but it is an attribute as it returns the transposed view of a

#Methods perform specific task ,Accessed with paranthesis
a=np.arange(1,16).reshape(3,5)
print(a)
print("Sum of all elements of array:",a.sum())
print("Maximum number in array:",a.max())
print("Minimum number in array:",a.min())
print("Mean:",a.mean())
print("Standard deviation:",a.std())
print(np.sum(a))               #Another method


arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
cum_sum_2d = np.cumsum(arr_2d)
print("Original 2D array:\n", arr_2d)
print("Cumulative sum of 2D array:", cum_sum_2d)
print("Commulative Sum:",a.cumsum())
#The cumulative sum of an array is a sequence
#where each element is the sum of all previous elements including the current one


#If we find the commulative sum of a 2d,3d array,it will result in !d array.