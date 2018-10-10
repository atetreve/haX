import numpy as np
a = np.array([[1,1,1],[2,2,2]])

print(a.shape)
>>> (2, 3)

print(a.sum(axis=0))
>>> [3 3 3]

print(a.sum(axis=1))
>>> [3 6]







a2 = np.array([[[1,1,1],[2,2,2]],[[3,3,3],[4,4,4]]])

print(a2.shape)
>>> (2, 2, 3)

print(a2.sum(axis=0))
>>> [[4 4 4]
 [6 6 6]]

print(a2.sum(axis=1))
>>> [[3 3 3]
 [7 7 7]]

print(a2.sum(axis=2)) #sums each instance individually
>>> [[ 3  6]
 [ 9 12]]
