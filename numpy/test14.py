# 使用 nditer() 迭代数组: 从非常基本的迭代到非常高级的迭代都可以使用

# 迭代每个标量元素
# 在基本的 for 循环中，迭代遍历数组的每个标量，我们需要使用 n 个 for 循环，对于具有高维数的数组可能很难编写。

import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)
