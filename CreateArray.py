import numpy as np
#From list and tuple
A=np.array([1,2,3])

#for array with specific values
c=np.zeros(2,dtype='i4')               #i4=int32=4B,int64=i8=8B,U32=128,U16=64,float=8B,str=4B
d=np.ones(3)
e=np.full((2,6),16)                         #used to generate array with specific   full(length,value/number)
f=np.empty((2,3,3))

#For specific sequence and ranges
b=np.arange(2,11,2)
g=np.linspace(0,1,num=6).reshape(2,3)          #It is used to generate evenly spaced values within specified range
h=np.logspace(0,2,40).reshape(2,4,5)
print(len(g)) 
print(e)                      
#it tells us the length of 1darray.For 2D array,it tells the number of rows(size of first dimension).
#For 3D array,it tells the number  of layers(size of first dimension)

#For identity and digonal matrices
i=np.identity(4)
j=np.diag([1,2,3,4,5]) 
k=np.eye(3,5)                 #for identity matri
print(j)
#Random arrays
l=np.random.rand(4,1,4)            #Uniform ditribution(random numbers between 0 and 1)
n=np.random.randn(4)               #normal distribution
v=np.zeros(3)
print(v)