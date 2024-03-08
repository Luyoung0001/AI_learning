#font: utf-8
import numpy as np
import matplotlib.pyplot as plt

p = np.random.rand(10000)
print(p)
plt.hist(p, bins=20, color='g', edgecolor='b')
plt.show()