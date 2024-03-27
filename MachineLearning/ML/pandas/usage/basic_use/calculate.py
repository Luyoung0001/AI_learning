import pandas as pd
data = pd.read_csv("./data/stock_day.csv")
# 算术运算
# 加法
print(data.head())
print(data["open"].add(10))

print(data["open"] > 23)

print(data[(data["open"] > 20) & (data["open"] < 24)])



