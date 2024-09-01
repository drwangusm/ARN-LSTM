import matplotlib.pyplot as plt
import numpy as np

# 模拟数据
labels = [
    'Approaching','Departing','Kicking','Punching','Pushing','Hugging','ShakingHands','Exchanging'
]

# ## RN 系列 Chapter 4## (使用fold_0/return_0)
# accuracy_RN_joint = [0.875,0.99,0.875,0.8888888888888888,0.6666666666666666,0.98,0.98,0.25]
# accuracy_RN_temp = [ 0.625,0.875,0.9856,0.8888888888888888,0.96,0.97,0.97,0.375]
# accuracy_RN_joint_temp= [0.99,0.99,0.875,0.8888888888888888,0.6666666666666666,0.99,0.9678,0.625]
# # # 设置图表大小
# plt.figure(figsize=(14, 7))
# # 绘制折线图
# plt.plot(accuracy_RN_joint, 'rx', label='RN_joint', linestyle='--')
# plt.plot(accuracy_RN_temp, 'g^', label='RN_temp', linestyle='--')
# plt.plot(accuracy_RN_joint_temp, 'bo', label='RN_joint_temp', linestyle='--')

## RN 系列 Chapter 4## (使用5个fold的return,共25个return中分类识别的准确率的均值)
accuracy_ARN_joint = [0.978667,0.934556, 0.775000,0.815444,0.706667,0.950000,0.795429,0.630159]
accuracy_ARN_temp = [0.975000,0.957000,0.940000,0.886556,0.778667, 0.940000,0.821857,0.751111]
accuracy_ARN_joint_temp= []
accuracy_ARN_fc1_joint_temp= []
# # 设置图表大小
plt.figure(figsize=(14, 7))
# 绘制折线图
plt.plot(accuracy_ARN_joint, 'rx', label='ARN_joint', linestyle='--')
plt.plot(accuracy_ARN_temp, 'g^', label='ARN_temp', linestyle='--')
plt.plot(accuracy_ARN_joint_temp, 'bo', label='ARN_joint_temd', linestyle='--')
plt.plot(accuracy_ARN_fc1_joint_temp, 'ms', label='ARN-fc1_joint+temp', linestyle='--')



# ## ARN-LSTM 系列 Chapter 6##
# accuracy_ARN_LSTM_inward = [0.875,1.0,0.875,0.8888888888888888,0.6666666666666666,1.0,1.0,0.75]
# accuracy_ARN_LSTM_outward = [1.0,1.0,0.75,1.0,0.6666666666666666,1.0,1.0,0.5]
# accuracy_ARN_LSTM_inward_outward= [0.875,1.0,1.0,0.8888888888888888,0.6666666666666666,1.0,1.0,0.375]
# ARN_LSTM_fc1_inward_outward = [0.875,1.0,0.75,0.7777777777777778,0.6666666666666666,1.0,1.0,0.5]
# # 设置图表大小
# plt.figure(figsize=(14, 7))
# # 绘制折线图
# plt.plot(accuracy_ARN_LSTM_inward, 'rx', label='ARN-LSTM_inward', linestyle='--')
# plt.plot(accuracy_ARN_LSTM_outward, 'g^', label='ARN-LSTM_outward', linestyle='--')
# plt.plot(accuracy_ARN_LSTM_inward_outward, 'bo', label='ARN-LSTM_inward_outward', linestyle='--')
# plt.plot(ARN_LSTM_fc1_inward_outward, 'ms', label='ARN-LSTM_fc1_inward_outward', linestyle='--')

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
plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/SBU/ARN-all_acc_vs.png',dpi=300,bbox_inches='tight')
plt.show()
