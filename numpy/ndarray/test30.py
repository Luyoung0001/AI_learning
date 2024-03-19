# 什么是 ufuncs？
# ufuncs 指的是“通用函数”（Universal Functions），它们是对 ndarray 对象进行操作的 NumPy 函数。

# 什么是向量化？
# 将迭代语句转换为基于向量的操作称为向量化。

# 由于现代 CPU 已针对此类操作进行了优化，因此速度更快。
# 对两个列表的元素进行相加：
# list 1: [1, 2, 3, 4]

# list 2: [4, 5, 6, 7]

# 一种方法是遍历两个列表，然后对每个元素求和。
import numpy as np
# 实例
# 如果没有 ufunc，我们可以使用 Python 的内置 zip() 方法：
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z) # 该过程很慢,并且得到的是同类型的 list

# 对此，NumPy 有一个 ufunc，名为 add(x, y)，它会输出相同的结果。

z = np.add(x,y)
print(z) # 直接返回一个 ndarray

