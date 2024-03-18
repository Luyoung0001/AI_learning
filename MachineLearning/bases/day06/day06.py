import pandas
from sklearn import linear_model as lm
df = pandas.read_csv("cars.csv")

X = df[['Weight','Volume']]
y = df['CO2']

# print(X)

# print(y)

# 在 sklearn 模块中，我们将使用 LinearRegression() 方法创建一个线性回归对象。

# 该对象有一个名为 fit() 的方法，该方法将独立值和从属值作为参数，并用描述这种关系的数据填充回归对象

regr = lm.LinearRegression()

regr.fit(X,y)

print(regr.coef_)

predict1 = regr.predict([[2300, 1300]])

print(predict1)
