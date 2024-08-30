import matplotlib.pyplot as plt
import numpy as np

# ut 标签
labels =  ['Hand Shaking','Hugging','Kicking','Pointing','Punching','Pushing']

# #ut-1
# accuracy_ARN_LSTM_inward = [1.0,1.0,0.0,1.0,1.0,1.0]
# accuracy_ARN_LSTM_outward = [1.0,1.0,0.0,1.0,1.0,0.0]
# accuracy_ARN_LSTM_inward_outward= [ 1.0,1.0,0.0,1.0,1.0,1.0]
# ARN_LSTM_fc1_inward_outward = [1.0,1.0,1.0,1.0,1.0,1.0]


# #ut-2
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
plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/UT-2/ARN-LSTM(set_2)_acc_vs.png',dpi=300,bbox_inches='tight')
plt.show()
