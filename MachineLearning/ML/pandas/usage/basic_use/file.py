import pandas as pd
data = pd.read_csv("../data/stock_day.csv", usecols=["open","close"])
print(data.head())

# 去掉 index
# 数据保存

data.to_csv("./test.csv",columns=["close"], index=False)

data1 = pd.read_csv("./test.csv")
print(data1.head())





