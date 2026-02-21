
import numpy as np
three3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(three3d.shape)
print(three3d)
print(three3d.ndim)
print(three3d[0,0,0])
print(three3d[0,1,-1])
print(three3d[1,1,-1])
print(three3d[::-1,::-1,::-1])