import numpy as np

""" Filtering:Getting some elements out of an existing array and creating a new array out of them is called
filtering.
In numpy,you filter an array using a boolean index list.
A boolean index list is a list of booleans corresponding to indexes in the array.
If the value at an index is True that element is contained in the filtered array, if the value at that index
is False that element is excluded from the filtered array.
"""
ar=np.array([1,2,3,4,5,6])
boolean=[True,False,True,False,True,False]
filtered_array=[]
filtered_array=ar[boolean]
print(filtered_array)

#The common use is to filter the array based on conditions.

#Filter array to get elements above 50
arr=np.array([50,51,49,53,54])
filter=[]
for c in arr:

    if c>50:
        filter.append(True)
    else:
        filter.append(False)

new_array=arr[filter]
print("Boolean array:",filter)

print("Filtered array:",new_array)

#Another eaiser method to filter array

#Filtering even numbers from array
a=np.array([1,2,3,4,5,6,7,8,9,10])

filt=a%2==0
NewArray=a[filt]
print(filt)
print("Even mumbers:",NewArray)
# ----->'a%2==0' creates a boolean list where each element is either true or false based on condition.
# On matching the values of array with boolean list,array is filtered

