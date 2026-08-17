import numpy as np
a=np.arange(1,31).reshape(2,3,5)      #no.ofelements=no.of matrices*no.of rows*no.of columns for 3Darray
print("Array:",a)


print(a[1,0,0])              #Indexing to find specific element
print(a[1,:,2])              #Column access
print(a[0,1,:])              #Row access
print(a[0:2:1,::,:1:1])