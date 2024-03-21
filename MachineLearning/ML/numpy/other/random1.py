import numpy as np
import matplotlib.pyplot as plt

# 创建随机数组
# 正态分布
x1 = np.random.normal(1.75, 1, 100000000)  # 将数组长度减小为100000

plt.figure(figsize=(15, 5), dpi=100)
plt.hist(x1, 1000)  # 减小直方图的箱子数为1000
plt.show()

# 四只股票 5 天的涨幅
stock_change = np.random.normal(0,1,[4,5])

# 均匀分布
x2 = np.random.uniform(-1,1,10000000)
plt.figure(figsize=(15,5),dpi=100)
plt.hist(x2,bins=1000)
plt.show()

