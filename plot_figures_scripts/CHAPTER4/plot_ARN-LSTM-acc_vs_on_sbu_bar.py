import matplotlib.pyplot as plt
import numpy as np

# 动作类别标签
labels = [
    'Approaching', 'Departing', 'Kicking', 'Punching', 
    'Pushing', 'Hugging', 'ShakingHands', 'Exchanging'
]

# ## ARN-LSTM 系列 Chapter 6 ##
# 数据为 5 个 fold 的平均准确率
accuracy_ARN_LSTM_inward = [0.967000, 0.970556, 0.815000, 0.886111, 0.784000, 0.958000, 0.753429, 0.728016]
accuracy_ARN_LSTM_outward = [0.986111, 0.964000, 0.935000, 0.897333, 0.792000, 0.912000, 0.796286, 0.793333] 
accuracy_ARN_LSTM_inward_outward = [0.980000, 0.968000, 0.925000, 0.905000, 0.770667, 1.000000, 0.866143, 0.717778]
ARN_LSTM_fc1_inward_outward = [0.985000, 0.959111, 0.930000, 0.913333, 0.866667, 1.000000, 0.873286, 0.754921] 

# 设置图表大小
plt.figure(figsize=(14, 8))

# 设置条形图参数
x = np.arange(len(labels))  # 标签位置
n_models = 4                # 模型数量
total_width = 0.8           # 一组条形的总宽度
bar_width = total_width / n_models  # 每个条形的宽度

# 绘制分组条形图
plt.bar(x - 1.5 * bar_width, accuracy_ARN_LSTM_inward, bar_width, 
        label='ARN-LSTM_inward', color='#F8766D', edgecolor='black', alpha=0.9)
plt.bar(x - 0.5 * bar_width, accuracy_ARN_LSTM_outward, bar_width, 
        label='ARN-LSTM_outward', color='#7CAE00', edgecolor='black', alpha=0.9)
plt.bar(x + 0.5 * bar_width, accuracy_ARN_LSTM_inward_outward, bar_width, 
        label='ARN-LSTM_inward_outward', color='#00BFC4', edgecolor='black', alpha=0.9)
plt.bar(x + 1.5 * bar_width, ARN_LSTM_fc1_inward_outward, bar_width, 
        label='ARN-LSTM_fc1_inward_outward', color='#C77CFF', edgecolor='black', alpha=0.9)

# 添加图例
plt.legend(loc='upper right', frameon=True, shadow=True, fontsize=10)

# 添加标签和标题
plt.xlabel("Action Classes", fontsize=12, fontweight='bold', color='black')
plt.ylabel("Accuracy", fontsize=12, fontweight='bold')
plt.title("SBU Kinect Interaction Dataset Action Recognition Accuracy Comparison (Chapter 6)", 
          fontsize=14, pad=20)

# 设置x轴刻度
plt.xticks(ticks=x, labels=labels, rotation=45, ha="right", fontsize=11, color='black')

# 设置y轴范围，预留上方空间显示 1.0 满分
plt.ylim(0, 1.15) 
plt.yticks(np.arange(0, 1.1, 0.1))

# 显示网格（仅Y轴）
plt.grid(axis='y', linestyle='--', alpha=0.6)

# 自动调整布局
plt.tight_layout()

# 保存图表（根据需要修改路径）
plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/CHAPTER4/ARN-LSTM_sbu-all_acc_bar.png', dpi=300, bbox_inches='tight')

plt.show()