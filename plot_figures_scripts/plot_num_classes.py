import matplotlib.pyplot as plt

# 数据
categories = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] #行为类别
values = [20, 8, 6, 4, 3, 2, 2, 1]                      #数量

# 创建图形和子图
fig, ax = plt.subplots()

# 绘制条形图
plt.bar(categories, values, color='skyblue')  # 可以更改为其他颜色，例如 'red', 'green', 'blue', 'orange'

# 去除顶部和右侧的边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# 去除横向网格线
ax.yaxis.grid(True)

# 添加标题和标签
plt.xlabel('Classes')
plt.ylabel('Number of class (K)')

plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/NTU-V1/class.png',dpi=300,bbox_inches='tight')  #保存并命名图片
# 显示图形
plt.show()
