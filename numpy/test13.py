# 数组迭代
import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
  print(x)

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

for x in arr:
  for y in x:
    print(y)


