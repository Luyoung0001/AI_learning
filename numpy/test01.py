import numpy as np

arr = np.array([1,2,3,4,5,6]) # 函数创建一个 NumPy ndarray 对象
print(arr)
print(np.__version__)
print(type(arr))

arr1 = np.array([[1, 2, 3], [4, 5, 6]]) # 2D
print(arr1)

arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) # 3D
print(arr2)

a = np.array(42) # 0D
b = np.array([1, 2, 3, 4, 5]) # 1D
c = np.array([[1, 2, 3], [4, 5, 6]]) # 2D
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) #3D

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)