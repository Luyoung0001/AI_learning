# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.001,5,10)
y = x**x

plt.plot(x,y,'ro-', linewidth=3)
plt.show()