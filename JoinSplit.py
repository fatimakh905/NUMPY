import numpy as np

#Joining is putting the content of two or more arrays.
a=np.array([5,7,9])
b=np.array([2,44,5])

c=np.concatenate((a,b),axis=0)      
print(c)
d=np.dstack((c))

print(d)
print(np.hstack([a,b]))


#Concatenation and stacking are used for same purpose.But the main differnce is stacking is done along a new 
#axis.
#for 1d array,concatenation can be done vertically only(axis=0)
#For 1d array,stacking can be done in both ways vertivcally and horizontally.
#For 1d array,when i concatenate two arrays,1d array is produced,it will generate 1d array
#for 1d array,when i stack vertically(axis=0) or horizontlly,stacking will be along new axis (2d array produced)

#Same goes for 2d array(Stacking will always be along a new axis)
#vstack and hstack will not be along a new axis it will be just like concatenation.
#For1d array,we can use hstack but concatenation is not posssible horizontally
#Vstack used for adding row vertically and hstack for adding column horizontally.

#Splitting  (Reverse operation of joining)
#There are two methods
#i.split()     ii.array_split()
ar=np.array([[1,2,3,7],[4,5,6,7],[3,5,7,5],[8,44,9,2],[3,66,8,9],[3,5,7,1],[3,64,75,3],[34,31,44,5]])
l=np.vsplit(ar,4)                          
print(l) 
#vsplit means splitting an array on the basis of rows like here i am splitting an array into 4 arrays.
#we will divide the number of total rows over the number given here(8/4=2) so there will be two rows in each
#array.(Total arrays 4)

arr=np.array([[[1,5,8,5],[6,4,3,2]],[[5,6,7,8],[7,8,5,7]],[[2,4,6,5],[33,53,67,6]]])
print(np.hsplit(arr,2))
#hsplit means splitting an array on the basis of columns like here i am splitting a 3d array into 2 arrays.

"""numpy.split:

Requires the array to be split into equal parts.
Raises a ValueError if the array cannot be evenly split.
Suitable for cases where you are certain the array can be split evenly.

numpy.array_split:

Allows splitting into unequal parts.
Does not raise an error if the array cannot be evenly split; the remaining elements are included in the last sub-array.
More flexible and robust for general use when the number of splits may not evenly divide the array."""