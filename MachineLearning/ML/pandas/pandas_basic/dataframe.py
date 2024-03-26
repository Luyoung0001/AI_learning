import pandas as pd
import numpy as np

pd.DataFrame(data=None, index=None, columns=None)

arr = pd.DataFrame(np.random.randn(2,3))
print(arr)

score = np.random.randint(40,100,(10,5))
stu = ['同学'+str(i) for i in range(10)]
score_df = pd.DataFrame(score,columns=['语文','数学','英语','化学','生物'],index=stu)
print(score_df)

# 属性

print(score_df.T)
print(score_df.head(5))
print(score_df.tail(5))
print(score_df.values)
print(score_df.index)
print(score_df.columns)