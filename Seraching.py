#For searching a specific value in an array,where() method is used.It returns the index of the value.

import numpy as np

a=np.array([3,5,6,4,9,4,4,4])

print(np.where(a==6)) 

b=a.reshape(2,2,2)
print(b)

print(np.where(b==5))

#It is used to serach odd and even values in a array.
c=np.where(b%2==1)
print("Searching odd values'indexes:",c)
values_at_those_indexes=b[c]
print("Searching the odd values at those indexes:",values_at_those_indexes)