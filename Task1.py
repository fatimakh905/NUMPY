import numpy as np
a=np.arange(10)
print("Original array:",a)
odd_numbers=a[a%2==0]      #Boolean array is used here

print("Odd numbers in array :",odd_numbers)

a[a%2!=0]=-1

print("Replacing odd numbers with '-1'",a)

aar_2d=a.reshape(2,5)

print("After reshaping",aar_2d)


a=[1,2,7,8]
b=[5,2,9,7]

v=np.vstack((a,b))
h=np.hstack((a,b))

print("Vertically stacked",v)
print("Horizontally stacked",h)




