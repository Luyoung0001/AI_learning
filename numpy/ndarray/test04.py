# 数组裁切
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5]) # [2 3 4 5]

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:]) # [5 6 7]

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4]) # [1 2 3 4]

arr = np.array([1, 2, 3, 4, 5, 6, 7]) # 负裁切
print(arr[-3:-1]) # [5 6]

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2]) # [2 4]

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2]) # [1 3 5 7]

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4]) # [7 8 9]

# 从两个元素中返回索引 2
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2]) # [3 8]

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4]) # [[2 3 4] [7 8 9]]