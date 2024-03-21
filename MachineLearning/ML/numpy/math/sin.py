import numpy as np
import matplotlib.pyplot as plt
 # 准备数据
x = np.linspace(-10,10,1000)
y = np.sin(x)

# 准备画布
plt.figure(figsize=(15,5),dpi=100)

# 绘制图像
plt.plot(x,y,color='g',linestyle=':')

# 显示网格
plt.grid(True,alpha=0.6)

# 保存图像
plt.savefig("math_figure.png")

# 显示图像
plt.show()