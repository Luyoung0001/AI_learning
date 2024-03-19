import matplotlib.pyplot as plt
import random

# 准备数据
x = range(60)
y_shanghai = [random.uniform(15,18) for i in x]
y_beijing = [random.uniform(1,5) for i in x]

# 创建画布,一行二列
# plt.figure(figsize=(15,5),dpi = 100)
fig,axes = plt.subplots(nrows=1,ncols=2,figsize=(15,5),dpi=100)

# 绘制图像
axes[0].plot(x,y_shanghai, label="shanghai",color='g',linestyle='--')
axes[1].plot(x,y_beijing, label="beijing",color='r',linestyle=':')

# 创建坐标
x_ticks_lable = ["11:{}".format(i) for i in x]
y_ticks_lable = range(40)

# 修改坐标显示效果
axes[0].set_xticks(x[::5])
axes[0].set_yticks(y_ticks_lable[::5])
axes[0].set_xticklabels(x_ticks_lable[::5])

axes[1].set_xticks(x[::5])
axes[1].set_yticks(y_ticks_lable[::5])
axes[1].set_xticklabels(x_ticks_lable[::5])

# 添加网格显示
axes[0].grid(True,linestyle="--", alpha=0.6)
axes[1].grid(True,linestyle="--", alpha=0.6)

# 添加描述信息
axes[0].set_xlabel("time")
axes[0].set_ylabel("temp")
axes[0].set_title("temp changes with time",fontsize=20)

axes[1].set_xlabel("time")
axes[1].set_ylabel("temp")
axes[1].set_title("temp changes with time",fontsize=20)

# 添加图例
axes[0].legend(loc="best")
axes[1].legend(loc="best")

# 图像保存
plt.savefig("time2.png")

plt.show()









