# 要衡量模型是否足够好，我们可以使用一种称为训练/测试的方法。

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2)

# 从数据集开始
# 从要测试的数据集开始。
# 我们的数据集展示了商店中的 100 位顾客及其购物习惯。


x = np.random.normal(3,1,100)
y = np.random.normal(150,40,100)/x

plt.scatter(x,y)
plt.show()

# 拆分训练/测试
# 训练集应该是原始数据的 80％ 的随机选择。
# 测试集应该是剩余的 20％。

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

# 显示训练集
# 显示与训练集相同的散点图：

plt.scatter(train_x,train_y)
plt.show()

# 显示测试集
# 为了确保测试集不是完全不同，我们还要看一下测试集:

plt.scatter(test_x,test_y)
plt.show()

