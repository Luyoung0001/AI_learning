# 直接从数组创建过滤器
# 上例是 NumPy 中非常常见的任务，NumPy 提供了解决该问题的好方法。

# 我们可以在条件中直接替换数组而不是 iterable 变量，它会如我们期望地那样工作。

import numpy as np
arr = np.array([61,1,2,3,4])
filter_arr = arr > 2
newarr = arr[filter_arr]
print(newarr)
