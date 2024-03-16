import numpy as np

# 视图应该受到对原始数组所做更改的影响。
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 61

print(arr)
print(x)