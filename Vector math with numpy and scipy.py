#Multi-dimensional Arrays ndarray

import numpy as np
import random
dims = (2,4)
print(np.ndarray(dims,dtype=float))
'''An array object represents a multidimensional, homogeneous array
 |  of fixed-size items. '''
#ndarray(shape, dtype=float, buffer=None, offset=0,strides=None, order=None)
print(np.zeros(dims,dtype=int))

data = np.random.random(dims) #Return random floats in the half-open interval [0.0, 1.0)
print(data)
print("data[0,1] is",data[0,1])
print("data[:2,:2] is",data[:2,:2])
print("data[1:2,2:4] is",data[1:2,2:4])

print(data+1)
print(data > 0.5)


#Example
x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
     #minimum
x.min()
print(np.min(x,axis = 1))#axis = 1 行内对比
print(np.min(x,axis = 0))#axis = 0 队内对比
     #sum and std
print(x.sum(axis = 0))
print(np.std(x))
     #boolean
print((x > 8).any())#是否存在任何大于8的数
     #sorting
print(np.argsort(x,axis = 0))#return the rank


#####--------------------Basic Linear Algebra
print("--------------------Basic Linear Algebra--------------------")
import scipy.spatial
#create 2 arrays
x = np.array([1.,2.,3.])
y = np.random.normal(size = 3)

#compute vector prodcts
inner1 = np.inner(x,y)
dot1 = np.dot(x,y)
outer1 = np.outer(x,y)

print(inner1,dot1,outer1,sep = "\n")

#normalize vector
x /= scipy.linalg.norm(x)
print(x)
#compute cosine distance
dist = scipy.spatial.distance.cosine(x,y)
print(dist)




















