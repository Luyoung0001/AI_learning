# 使用 ndenumerate() 进行枚举迭代
# 枚举是指逐一提及事物的序号。

# 有时，我们在迭代时需要元素的相应索引，对于这些用例，可以使用 ndenumerate() 方法。

import numpy as np
arr = np.array([1,2,3])
for idx, x in np.ndenumerate(arr):
    print(idx,x)
    if x == 3:
        print(type(idx)) # 是一个元组

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

## 这里就解释了为什么是个元组
