import matplotlib.pyplot as plt
import numpy as np

# ut 标签
labels =  ['Hand Shaking','Hugging','Kicking','Pointing','Punching','Pushing']

# #ut-1
# accuracy_ARN_LSTM_inward = [0.680000,0.99,0.240000,0.99,0.315217, 0.734694]
# accuracy_ARN_LSTM_outward = [0.70,0.98,0.32,0.90,0.377551,0.608696]
# accuracy_ARN_LSTM_inward_outward= [0.820000,1.0,0.36,0.92,0.357143,0.760870]
# ARN_LSTM_fc1_inward_outward = [0.76,1.0,0.420000,0.900000,0.285714,0.760870]

#ut-2
accuracy_ARN_LSTM_inward = []
accuracy_ARN_LSTM_outward = []
accuracy_ARN_LSTM_inward_outward= []
ARN_LSTM_fc1_inward_outward = []


# 设置图表大小
plt.figure(figsize=(14, 7))

# 绘制折线图
plt.plot(accuracy_ARN_LSTM_inward, 'rx', label='ARN-LSTM_inward', linestyle='--')
plt.plot(accuracy_ARN_LSTM_outward, 'g^', label='ARN-LSTM_outward', linestyle='--')
plt.plot(accuracy_ARN_LSTM_inward_outward, 'bo', label='ARN-LSTM_inward_outward', linestyle='--')
plt.plot(ARN_LSTM_fc1_inward_outward, 'ms', label='ARN-LSTM_fc1_inward_outward', linestyle='--')

# 添加图例
plt.legend()

# 添加标签和标题
plt.xlabel("Action Classes", fontsize=12, color='black')
plt.ylabel("Accuracy (%)")
plt.title("UT-interaction dataset (set_2) action recognition performance comparison")

# 设置x轴刻度并将标签颜色设置为黑色，字体大小设置为18
plt.xticks(ticks=np.arange(len(labels)), labels=labels, rotation=60, ha="right", fontsize=12, color='black')

# 显示网格
plt.grid(True, linestyle='--', alpha=0.6)

# 显示图表
plt.tight_layout()
plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/UT-1/ARN-LSTM-all(set_2)_acc_vs.png',dpi=300,bbox_inches='tight')
plt.show()
