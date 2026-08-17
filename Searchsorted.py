import numpy as np

#There is a method called searchsorted() which performs a binary search in the array, and returns the 
# index where the specified value would be inserted to maintain the search order
a=np.array([1,3,5])
#The searchsorted() method is assumed to be used on sorted arrays
b=np.searchsorted(a,7,side='right')
print("7 is inserted at index",b)

#By default,side='left'
c=np.searchsorted(a,[2,8])
print(c)
#First it will insert 2 in the original array and tell it index.
#then,it will insert 8 in the original array and tell its index.