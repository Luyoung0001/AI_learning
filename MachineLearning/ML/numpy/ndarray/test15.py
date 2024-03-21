# 迭代不同数据类型的数组
# 我们可以使用 op_dtypes 参数，并传递期望的数据类型，以在迭代时更改元素的数据类型。
# NumPy 不会就地更改元素的数据类型（元素位于数组中），因此它需要一些其他空间来执行此操作.
# 该额外空间称为 buffer，为了在 nditer() 中启用它，我们传参 flags=['buffered']。
import numpy as np
arr = np.array([1,2,33,4])
for x in np.nditer(arr,flags=['buffered'],op_dtypes=['S']):
    print(x) # 字节字符串

