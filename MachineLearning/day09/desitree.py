import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as plting

df = pandas.read_csv("actors.csv")
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

# print(df)

# 然后，我们必须将特征列与目标列分开。

# 特征列是我们尝试从中预测的列，目标列是具有我们尝试预测的值的列。

features = ['Age', 'Experience','Rank','Nationality']

X = df[features]
y = df['Go']

# print(X)
# print(y)

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X,y)
data = tree.export_graphviz(dtree,out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mdtree.png')

img = plt.imread('mdtree.png')
imgplot = plt.imshow(img)
plt.show()