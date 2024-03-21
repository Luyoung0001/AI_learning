import numpy as np
import matplotlib.pyplot as plt
# 准备数据
x=range(100)
y=[np.sin(i) for i in x]

# 准备画布
plt.figure(figsize=(15,5),dpi=100)

# 画图
plt.scatter(x,y)

# 显示
plt.show()

