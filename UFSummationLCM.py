import numpy as np

#In NumPy, addition refers to the element-wise addition of two arrays.
#Summation in NumPy refers to the process of adding up all the elements of an array 
# or along a specific axis of an array. The np.sum() function is used for this purpose.

a=np.array([1,2,3,4])
b=np.array([6,1,8,9])
print("Summation of an array:",np.sum(a))
print("Summation along specified axis:",np.sum([a,b],axis=0)) #summation along a specific axis

#Cummulative Sum
#Cummulative sum means partially adding the elements in array.
#E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
val=np.cumsum((a,b),axis=1)
print("Commulative Sum:",val)

#In case of summation and product,axis=1 means horizontally (rows),axis=0 means vertically (Columns)


#Products
#To find the product of the elements in an array, use the prod() function.
print("Product of all elements of an array:",np.prod(a))
print("Product along specified axis:",np.prod([a,b],axis=1)) #Product along a specific axis


#Cummulative Product
#Cummulative product means taking the product partially.
#E.g. The partial product of [1, 2, 3, 4] is [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]

val=np.cumprod((a,b),axis=1)
print("Commulative Product:",val)

#Differences
#A discrete difference means subtracting two successive elements.
#E.g. for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]
#To find the discrete difference, use the diff() function.

arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr)
print("Difference:",newarr)

#We can perform this operation repeatedly by giving parameter n.
#E.g. for [1, 2, 3, 4], the discrete difference with n = 2 would be [2-1, 3-2, 4-3] = [1, 1, 1] 
#then, since n=2, we will do it once more, with the new result: [1-1, 1-1] = [0, 0]

#LCM
#The Lowest Common Multiple is the smallest number that is a common multiple of two numbers.
h=4
j=10
print("LCM of two numbers:",np.lcm(h,j))

#LCM of all elements in an array
#To find the Lowest Common Multiple of all values in an array, you can use the reduce() method.
#The reduce() method will use the ufunc,in this case the lcm() function, on each element, and 
#reduce the array by one dimension.
t = np.array([3, 6, 9])

x = np.lcm.reduce(t)

print("LCM of all elements of an array:",x)

#if you want to find lcm of 2d array,you need to flatten the array.















