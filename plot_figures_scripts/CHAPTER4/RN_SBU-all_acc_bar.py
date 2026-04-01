import matplotlib.pyplot as plt
import numpy as np

# 动作类别标签
labels = [
    'Approaching', 'Departing', 'Kicking', 'Punching', 
    'Pushing', 'Hugging', 'ShakingHands', 'Exchanging'
]

# RN 系列数据集 (Chapter 4)
accuracy_RN_joint = [0.875, 0.99, 0.875, 0.8888888888888888, 0.6666666666666666, 0.98, 0.98, 0.25]
accuracy_RN_temp = [0.625, 0.875, 0.9856, 0.8888888888888888, 0.96, 0.97, 0.97, 0.375]
accuracy_RN_joint_temp = [0.99, 0.99, 0.875, 0.8888888888888888, 0.6666666666666666, 0.99, 0.9678, 0.625]

# 设置图表大小
plt.figure(figsize=(12, 7))

# 设置条形图参数
x = np.arange(len(labels))  # 标签位置
width = 0.25  # 单个条形的宽度

# 绘制分组条形图
# 使用不同的颜色和微小的透明度增加视觉层次感
rects1 = plt.bar(x - width, accuracy_RN_joint, width, label='RN_joint', 
                 color='#E63946', edgecolor='black', alpha=0.85)
rects2 = plt.bar(x, accuracy_RN_temp, width, label='RN_temp', 
                 color='#2A9D8F', edgecolor='black', alpha=0.85)
rects3 = plt.bar(x + width, accuracy_RN_joint_temp, width, label='RN_joint+temp', 
                 color='#457B9D', edgecolor='black', alpha=0.85)

# 添加图例
plt.legend(loc='upper right', frameon=True, shadow=True)

# 添加标签和标题
plt.xlabel("Interaction Action Classes", fontsize=12, fontweight='bold', labelpad=10)
plt.ylabel("Accuracy", fontsize=12, fontweight='bold')
plt.title("SBU Kinect Interaction Dataset Accuracy Comparison", fontsize=14, pad=20)

# 设置x轴刻度
plt.xticks(ticks=x, labels=labels, rotation=45, ha="right", fontsize=11, color='black')

# 设置y轴范围（预留顶部空间给图例）
plt.ylim(0, 1.15) 

# 添加水平网格线，辅助观察准确率数值
plt.grid(axis='y', linestyle='--', alpha=0.5)

# 自动优化布局，防止底部标签显示不全
plt.tight_layout()

# 保存图表（根据您的路径需求取消注释）
plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/CHAPTER4/RN-all_acc_bar.png', dpi=300, bbox_inches='tight')

# 显示图表
plt.show()