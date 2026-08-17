import numpy as np
list1=[3,4,5]
list2=[1,2,1]
list3=[4,6,4]
arr=np.array([[list1],[list2],[list3]])
recolom=arr[:,::-1]
print("Array is",recolom)

#Flatten the array
b=arr.reshape(-1)
print(b)
#When only one argument -1 is given in reshape method ,it will flatten every type of array whether its 2d 
#or 3d into 1d array.