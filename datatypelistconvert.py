import numpy as np



list=[1,2,3.4]
d=np.array(list,dtype='U32')           #we can use str and U32 or U16 both to convert into string
print(d.itemsize)
#We pass list as a argument ehen we create array so list has differnet types of values while arrays contain
#homogenous data so when we pas  list with diff. data types it will automatically convert.
# We can also explicitly declare which data type we want(conversion which can be accepted only)