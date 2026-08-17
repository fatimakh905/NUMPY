import numpy as np

arr=np.arange(1,8,2) #to create array        arange(start(0),end,step(1))
print(arr)

#To create two dimenional array(matrix) using arange method ,it is necessary to use reshape(rows,columns)
a=np.arange(1,13).reshape(6,2)
print(a)
# rows * columns =no.of elements


# To create matrix or one dimensional array with zeros
z=np.zeros((2,4),dtype=int)
print(z)

# To create matrix or two dimensional array with zeros
o=np.ones((2,4))
print(o)