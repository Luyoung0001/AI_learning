# 数组过滤
# 从现有数组中取出一些元素并从中创建新数组称为过滤（filtering）

# 在 NumPy 中，我们使用布尔索引列表来过滤数组。
# 布尔索引列表是与数组中的索引相对应的布尔值列表。
# 如果索引处的值为 True，则该元素包含在过滤后的数组中；如果索引处的值为 False，则该元素将从过滤后的数组中排除。
import numpy as np

arr = np.array([61, 62, 63, 64, 65])

x = [True, False, True, False, True]

newarr = arr[x]

print(newarr)
# 新过滤器仅包含过滤器列表有值 True 的值，所以在这种情况下，索引为 0 和 2、4
# 这种过滤方法很繁琐,基本没啥用




