# 用堆栈函数连接数组
# 堆栈与级联相同，唯一的不同是堆栈是沿着新轴完成的。
# 我们可以沿着第二个轴连接两个一维数组，这将导致它们彼此重叠，即，堆叠（stacking）。
# 我们传递了一系列要与轴一起连接到 concatenate() 方法的数组。如果未显式传递轴，则将其视为 0。

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)

print(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2)) # NumPy 提供了一个辅助函数：hstack() 沿行堆叠。

print(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2)) # NumPy 提供了一个辅助函数：vstack() 沿列堆叠。

print(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))

print(arr)
