import numpy as np
import matplotlib.pyplot as plt
x = np.random.uniform(0.0, 5.0, 250)

print(x)

plt.hist(x,5) # 我们使用上例中的数组绘制 5 条柱状图。
plt.show()

