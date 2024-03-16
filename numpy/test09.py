import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)
# 每个 NumPy 数组都有一个属性 base，如果该数组拥有数据，则这个 base 属性返回 None。
# 否则，base 属性将引用原始对象。