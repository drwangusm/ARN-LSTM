import matplotlib.pyplot as plt

#绘制折线对比图

# 数据
x = [0.0, 0.5, 1.0, 2.0, 3.0]
y1 = [73.9, 77.0, 77.2, 78.0, 78.7]
y2 = [73.7, 76.1, 77.0, 77.7, 78.0]
y3 = [77.8, 79.8, 79.8, 79.8, 80.2]

# 创建图形
fig, ax = plt.subplots()

# 绘制折线图
ax.plot(x, y1, '-o', label='S-trans&S-rota+RNN', color='green')
ax.plot(x, y2, '-o', label='S-trans+RNN(aug.)', color='cyan')
ax.plot(x, y3, '-o', label='VA-RNN(aug.)', color='red')

# 添加数据点注释
for i, txt in enumerate(y1):
    ax.annotate(f'{txt}', (x[i], y1[i]), textcoords="offset points", xytext=(0,5), ha='center')
for i, txt in enumerate(y2):
    ax.annotate(f'{txt}', (x[i], y2[i]), textcoords="offset points", xytext=(0,5), ha='center')
for i, txt in enumerate(y3):
    ax.annotate(f'{txt}', (x[i], y3[i]), textcoords="offset points", xytext=(0,5), ha='center')

# 设置标题和标签
ax.set_title('NTU RGB+D 60(Cross_subject)')
ax.set_xlabel('#Parameters(million)')
ax.set_ylabel('Accuracy(%)')

# 添加图例
ax.legend()

# 保存图形
plt.savefig('./nturgbd60_cross_sbuject.png', format='png')

# 显示图形
plt.show()
