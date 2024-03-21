import numpy as np

arr = np.array([61, 62, 63, 64, 65])

# 创建一个空列表
filter_arr = []

# 遍历 arr 中的每个元素
for element in arr:
  # 如果元素大于 62，则将值设置为 True，否则为 False：
  if element > 62:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
# 这样的过滤器有价值

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# 创建一个空列表
filter_arr = []

# 遍历 arr 中的每个元素
for element in arr:
  # 如果元素可以被 2 整除，则将值设置为 True，否则设置为 False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)