# 数组重塑
# 重塑意味着更改数组的形状。
# 数组的形状是每个维中元素的数量。
# 通过重塑，我们可以添加或删除维度或更改每个维度中的元素数量。

# 将以下具有 12 个元素的 1-D 数组转换为 2-D 数组。
# 最外面的维度将有 4 个数组，每个数组包含 3 个元素：

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(4,3)
print(newarr)