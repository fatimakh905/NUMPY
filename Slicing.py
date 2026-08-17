import numpy as np
#Slicing is a way to extract subset of data from numpy array.it can also access single element.

a=np.array([10,20,30,40,50,60,70])
print(a[1::])        
print(a[::2])  
print(a[:5:])
a[1:3:1]=0
print(a)

#Reverse order
print(a[-6:-5:-1])        #It is necessary to give step as -1 if we want to access data in reverse order.
print(a[-1:-5:-1])          
#Instead of error Empty array appear in these cases 
#i.If i wanted to access reverse order but did not write the step as -1
#ii.If i do not write step as -1 or give step positive and start and stop are negative(means i want to access values in reverse)
#iii,if i wanted to access in normal order but i write the step as -1(reverse order)

#2d array
b=np.array([[1,2,3],[4,6,7],[1,9,6]])
print(b[1,])
print(b[:,2])
print(b[1::,0:2:])

#3d array
c=np.array([[[10,20],[30,40]],[[6,7],[16,14]]])
print(c[0,:,:])       #To acccess any complete matrix in 3d array
print(c[0:2:1,::,:1:1])