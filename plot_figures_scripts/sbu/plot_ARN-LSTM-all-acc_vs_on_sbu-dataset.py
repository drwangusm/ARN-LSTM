import matplotlib.pyplot as plt
import numpy as np

# 模拟数据
labels = [
    'Approaching','Departing','Kicking','Punching','Pushing','Hugging','ShakingHands','Exchanging'
]

## ARN-LSTM 系列 Chapter 6## (使用5个fold的return,共25个return中分类识别的准确率的均值)
accuracy_ARN_LSTM_inward = [0.967000, 0.970556, 0.815000,0.886111,0.784000,0.958000,0.753429,0.728016]
accuracy_ARN_LSTM_outward = [0.986111,0.964000,0.935000,0.897333,0.792000,0.912000,0.796286,0.793333] 
accuracy_ARN_LSTM_inward_outward= [0.980000,0.968000,0.925000,0.905000,0.770667, 1.000000,0.866143, 0.717778]
ARN_LSTM_fc1_inward_outward = [0.985000, 0.959111,0.930000,0.913333,0.866667,1.000000,0.873286,0.754921] 

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
# plt.title("NTU RGB+D 60 dataset (Cross_view) action recognition performance comparison")
plt.title("SBU kinect interaction dataset action recognition accuracy comparison")

# 设置x轴刻度并将标签颜色设置为黑色，字体大小设置为18
plt.xticks(ticks=np.arange(len(labels)), labels=labels, rotation=60, ha="right", fontsize=12, color='black')

# 显示网格
plt.grid(True, linestyle='--', alpha=0.6)

# 显示图表
plt.tight_layout()
plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/SBU/ARN-LSTM(chapter 6)-all_acc_vs.png',dpi=300,bbox_inches='tight')
plt.show()
