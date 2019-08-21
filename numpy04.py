# Two Dimensional Numpy
import numpy as np
a = [[1,2,3], [4,5,6], [7,8,9]]
b = np.array(a)
print(b, b.dtype, b.ndim, b.shape, b.size)
print(b[1][1]) # Accessing Element at 2nd Row and 2nd Column
print(b[1][0:2])
print(b[0:2])
print(b[0:2][1])
print(b[0:2,2])

