import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31
# 原始数组应该受到对视图所做更改的影响
print(arr)
print(x)