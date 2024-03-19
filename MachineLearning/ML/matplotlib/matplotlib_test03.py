import matplotlib.pyplot as plt
import random
# 准备数据
x = range(60)
y_shanghai = [random.uniform(0,30) for i in x]

# 创建画布
plt.figure(figsize=(15,5),dpi=100)

# 绘制曲线
plt.plot(x,y_shanghai)

# 构造 x 轴刻度标签
x_ticks_lable = ["11:{}".format(i) for i in x]
# 构造 y 轴刻度
y_ticks = range(40)

# 修改 x,y 轴坐标的刻度显示

plt.xticks(x[::5],x_ticks_lable[::5])
plt.yticks(y_ticks[::5])

# 增加网格
plt.grid(True,linestyle='--',alpha=0.6)

# 添加描述信息
plt.xlabel("time")
plt.ylabel("temp")

# 添加标题
plt.title("temp changes with time",fontsize=20)

# 图片保存 一定要保存到 show()之前,因为 show()完资源就释放了
plt.savefig("time.png")
# 展示图像
plt.show()
