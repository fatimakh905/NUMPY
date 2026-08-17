import numpy as np
import pandas as pd
arr=np.array([1,2,3,4])

print("Array:",arr)
print(type(arr))     #this will return the class of object

print(type(arr[3]))     #This will print type of element

new_arr=np.append(arr,5)              #insertion at the end
print("After inserting at the end of array:",new_arr)         
#if i want that my original array is not affected
#by this operation and a new array is returned then  i will assign it to another name(array)

arr=np.insert(arr,0,0)      #insertion at the begining
print("Inserting at the begining",arr)

arr=np.insert(arr,3,7)                   #inserting in the middle(index,value at index)
print("Inserting in the middle",arr)


arr=np.delete(arr,-1)                     #deletion(only index)
print("After deletion",arr)                           