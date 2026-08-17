import numpy as np

#Sorting means putting elements in an ordered sequence.

a=np.array([3,7,1,0])
b=np.array(["apple","cherry","banana"])
print(np.sort(b))

#Sorting can be done on array of any data type.
#This method returns a copy of the array, leaving the original array unchanged

#2d array.It sorts every row.
c=a.reshape(2,2)
print(np.sort(c))

