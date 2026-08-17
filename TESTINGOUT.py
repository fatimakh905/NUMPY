import numpy as np
x=([3,2,3])
y=([6,4,9])
z=np.stack((x,y))

list1=[3,4,5]
list2=[1,2,1]
list3=[4,6,4]

Arr2d=np.array([[list1],[list2],[list3]])
recolom=Arr2d[:,::-1]
print(recolom)

arr=np.array([1,2,3,4,5])
splited_arr=np.array_split(arr,3)
print(type(splited_arr))
print(splited_arr)

ar=np.array([1,2,3,4])
for i in range(len(ar)):
    print(i)

p=np.array(['a','b','chhdhdh3'])
print(p.dtype)