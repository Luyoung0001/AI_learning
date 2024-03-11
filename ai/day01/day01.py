import numpy as np
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = np.mean(speed)
x1 = np.median(speed)
x2 = stats.mode(speed, keepdims=True)
x3 = np.std(speed)
x4 = np.var(speed)

print(x)

print(x1)

print(x2)

print(x3)

print(x4)

# 标准差和方差是机器学习中经常使用的术语，因此了解如何获取它们以及它们背后的概念非常重要。