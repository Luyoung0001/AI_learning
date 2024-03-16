# 数组搜索
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x) # 返回一个元组,元组每个元素为数组
print(type(x)) # <class 'tuple'>


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)

print(x)
