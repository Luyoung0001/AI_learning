import random
import time
import numpy as np

a = []

for i in range(1000000):
    a.append(random.random())

start_time = time.time()
sum0 = sum(a)
end_time = time.time()
print(f"使用Python内置的sum函数计算列表a的总和：{sum0}")
print(f"计算时间：{end_time - start_time} 秒")


b = np.array(a)
start_time = time.time()
sum1 = np.sum(b)
end_time = time.time()
print(f"使用NumPy的sum函数计算NumPy数组b的总和：{sum1}")
print(f"计算时间：{end_time - start_time} 秒")

# 可以看到,ndarray 的性能比原生 python 快很多
