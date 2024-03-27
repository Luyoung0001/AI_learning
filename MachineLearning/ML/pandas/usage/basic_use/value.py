import pandas as pd
data = pd.read_csv("./data/stock_day.csv")

# 赋值
data["close"] = 1;
print(data.head(5))

# 这种赋值,很灵活
data.close = 10;
print(data.head(5))



