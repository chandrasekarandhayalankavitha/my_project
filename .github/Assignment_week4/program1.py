
import numpy as np
twod = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(twod[::-1])
print(twod[:, ::-1])
print(twod[::-1, ::-1])
rev = twod[::-1, ::-1]
print(rev[0,1])
print(rev[1,1] )
print(rev[0,-1])
print(rev.sum())

