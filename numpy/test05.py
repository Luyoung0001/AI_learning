import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr = np.array(['apple', 'bana尼斯单纯na', 'cherry'])
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='S')
print(arr) #[b'1' b'2' b'3' b'4'] 这个表示字节字符串,用 b 前缀表示
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype) # int32,定义了 4 字节,因此类型就是 int32 了

# arr = np.array(['a', '2', '3'], dtype='i') 这个无法转换

# 转换已有数组的数据类型
# 更改现有数组的数据类型的最佳方法，是使用 astype() 方法复制该数组
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)