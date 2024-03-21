# np 数组排序
# NumPy ndarray 对象有一个名为 sort() 的函数，该函数将对指定的数组进行排序。
import numpy as np
arr = np.array([3,2,4,7,6])
newarr = np.sort(arr)
print(newarr)
newarr[1]= 100
print(arr)
print(newarr) # 可以看到,此方法返回数组的副本，而原始数组保持不变。

arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

arr = np.array([True, False, True])
print(np.sort(arr))

# 对 2D数组排序
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))
#[[2 3 4]
#[0 1 5]]
