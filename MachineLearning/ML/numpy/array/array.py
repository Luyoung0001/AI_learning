import numpy as np
arr = np.array([[1,2,3,2,1,4],[5,6,1,2,3,1]])

# ndarray 进行计算
arr +=1
print(arr)

arr *=2
print(arr)

# 数组与数组之间的计算
# 数组的形状必须相等,不然就会出现广播机制,例如

arr1 = np.array([[0],[1],[2],[3]])
arr2 = np.array([1,2,3])

arr3 = arr2+arr1
print(arr3)

