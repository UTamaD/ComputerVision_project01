import cv2 as cv
import numpy as np

print(cv.__version__)
print(np.__version__)

arr = [[1,4,2],[7,5,3]]
n_arr = np.array(arr,dtype='float64')
print(arr)
print(n_arr)
print(type(arr))
print(type(n_arr))

print(n_arr.ndim)
print(n_arr.shape)
print(len(n_arr.shape))
print(n_arr.size)

print(n_arr[0:2,0:2])

print(n_arr[1:2,1:2])
print(n_arr[1:2,0:2])
print(n_arr[:,2:3])
print(n_arr[0:2,0:2])


print(np.zeros((2,2)))
print(np.ones((1,2)))
print(np.full((2,2,),7))

print(np.eye(3,k=0))
print(np.identity(3))

print(np.random.random((4,4)))
print(np.random.normal((4,4)))
print(np.random.randint(0,10,(4,4)))
print(np.linspace(0,1,num=5,endpoint=True,retstep=True))
print(np.arange(0.2,1.0,0.1))