import pandas as pd
import numpy as np

# pd.DataFrame(data=None, index=None, columns=None)



# score = np.random.randint(40,100,(10,5))
# stu = ['同学_'+str(i) for i in range(10)]
# score_df = pd.DataFrame(score,columns=['语文','数学','英语','化学','生物'],index=stu)
# print(score_df)

# # 索引值的设置

# # 不能设置其中一个索引
# # score_df.index[2] = "同学1"
# score_df.reset_index(drop=True)
# print(score_df)


df = pd.DataFrame({'month':[1,4,7,10],'year':[2012,2014,2013,2014],'sale':[55,40,84,31]})
print(df)
# 设定索引值
df1 = df.set_index(['year','month'])
print(df1)
print(df1.index)


