import matplotlib.pyplot as plt
import random
# 准备数据
x = range(60)
y_shanghai = [random.uniform(15,18) for i in x]
# 创建画布
plt.figure(figsize=(5,5),dpi=100)
# 绘制曲线
plt.plot(x,y_shanghai)
# 展示图像
plt.show()