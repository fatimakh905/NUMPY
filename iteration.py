import numpy as np

#Iteration means going tghrough elements one by one.

arr=np.array([1,3,4,5,6])
for x in arr:
    print(x)


a=np.array([[1,2,3,4,5],[6,7,8,9,10]])
for y in a:
    for i in y:
        print(i)

ar=np.arange(1,16).reshape(3,1,5)
print(ar)
for u in ar:
    for k in u:
        for o in k:
            print(o)

#The function nditer() is used to iterate through each scalar of an array.It is useful as it saves us
#from the difficulty we face when we write for loops to iterate through arrays with high dimentionality.
#This function creates an iterator object which allows to iterate over array element by element.
brr=np.array([[[2,34,4],[5,6,8]],[[5,2,4],[4,7,9]]])
for p in np.nditer(brr):
    print(p)
#here i have used only one loop to iterate through each element of 3d array

#It provides various options to control behaviour of iteration.
# Such as memory access,data types etc.

for w in np.nditer(brr,flags=['buffered'],op_dtypes='S'):
    print(w)

""" Flag is an option that modifies the behaviour of iteration.Flag controls how iteration is performed 
influencing other aspects like memory access,order of iteration,buffering and more.

Commonly used nditer flags are 'buffered','f_index','multi_index','external_loop' and more
In this case 'buffered' is used,it allows buffering during iteration,it allows nditer to handle
us temporary memory for type conversion.
"""

# op_dtpes: this is an argument that specifies the desired output datya type during iteration.
#In this case,The desired output data type is byte string.


#Iterating with Different step size

F=np.arange(1,31).reshape(2,3,5)
print(F)

for c in np.nditer(F[:,2:3:,::2]):
    print(c)
#nditer by default iterates over elements not over rows and matrices.However it can be used to iterate 
#over rows by using specific flags and setting.
#if i do not use nditer function above,it will give me rows.


""" Enumeration means mentioning sequence number of somethings one by one.   
Sometimes We aslo need to mention the index of values during iteration.For this purpose we use ndenumerate().
"""

arrr=np.arange(1,9).reshape(2,4)
print(arrr)
for idx,x in np.ndenumerate(arrr):
    print(idx,x)