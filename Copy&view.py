import numpy as  np
a=np.array([1,2,3])
b=a.copy()
b[0]=0
print("Original array:",a)
print("Copied array:",b)
#Changes are made in either of them are not reflected.
#When we create copy an array,its exact duplicate new array is created which allocates memory.
#means both copy and original array allocates memory separately
#same data ki aik array generate kry gi jo memory allocate kry gi alg se

c=a.view()
c[2]=4
print("Original array:",a)
print("Copied array:",c)
#View do not owns the data.It is the refernce of original array.Changes made in either of them are reflected
#When view is used,it creates a reference to the underlying data of original array.
#Both original & view have pointers to same data buffer.


i=np.array([10,20,30,40,50])
print("Before Slicing:",i)
i[0:3:1]=2
print("after slicing:",i)

#This is important in slicing.When we slice numpy arrays it uses view means the changes will reflect
#in original array as well.So to avoide this means if we want to slice the numpy array withou making 
#any changes in original array we will use copy
g=np.array([1,2,3,4])
#Creates a copy of sliced array
h=g[0:3:].copy()
#Modifying the sliced array
h[0]=4
print(h)

                  #or
v=g.copy()
v[1:2]=10
print(v)