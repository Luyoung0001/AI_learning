import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[1])

# 访问 2D 数据和 C/C++等语言都不同

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st dim: ', arr[0, 1])
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('5th element on 2nd dim: ', arr[1, 4])
