import pandas as pd
data = pd.read_csv("./data/stock_day.csv")

data.sort_values(by="open",ascending=True)

print(data.head(10))