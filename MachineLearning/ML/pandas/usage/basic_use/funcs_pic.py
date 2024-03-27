import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("./data/stock_day.csv")

data = data.sort_index()

print(data.head())

stock_rise = data["p_change"]

# 画图
stock_rise.cumsum().plot()
plt.show()
