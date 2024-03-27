import pandas as pd
data = pd.read_csv("./data/stock_day.csv")


print(data.head())

# 索引操作

# 先列后行 拿取数据
print(data['open']['2018-02-27'])
# iloc 索引拿取数据
print(data.iloc[:5,:3])

# 不能 slice 操作 data[:3,:2]





