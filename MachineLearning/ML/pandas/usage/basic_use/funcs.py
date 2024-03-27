import pandas as pd
data = pd.read_csv("./data/stock_day.csv")


# 整体描述
print(data.describe())

# mode 众数
print(data.max())

print(data.min())


