# 拟合数据集
# 数据集是什么样的？我认为最合适拟合的是多项式回归，因此让我们画一条多项式回归线。
# 要通过数据点画一条线，我们使用 matplotlib 模块的 plott() 方法：

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
np.random.seed(2)

x = np.random.normal(3,1,100)
y = np.random.normal(150,40,100)/x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = np.poly1d(np.polyfit(train_x,train_y,4))

r2 = r2_score(train_y,mymodel(train_x))
r2test = r2_score(test_y,mymodel(test_x))

print(r2)
print(r2test)

myline = np.linspace(0,6,100)
plt.scatter(train_x,train_y)
plt.plot(myline,mymodel(myline))

plt.show()
