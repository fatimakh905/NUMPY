import numpy as np
a=np.linspace(0,20,num=5)         #values are printed in float
print(a)

arr=np.array([2,3,4,5])
bb=np.array([3.,5.,7.,8.])
print(arr//bb)

g=[[2,4,6],[1,3,5]]

print(np.cumsum(g,axis=1))   