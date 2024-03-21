# 拆分 NumPy 数组
# 拆分是连接的反向操作。

# 连接（Joining）是将多个数组合并为一个，拆分（Spliting）将一个数组拆分为多个。

# 我们使用 array_split() 分割数组，将要分割的数组和分割数传递给它。
import numpy as np
arr = np.array([1,2,3,4,5,6])
newarr = np.split(arr,3)

print(newarr) # [array([1, 2]), array([3, 4]), array([5, 6])]

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)

print(newarr) # 如果数组中的元素少于要求的数量，它将从末尾进行相应调整。
# newarr = np.split(arr, 4) 不会正常工作
print(newarr)


