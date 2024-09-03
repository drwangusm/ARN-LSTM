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

# ## RN 系列 Chapter 4## (使用5个fold的return,共25个return中分类识别的准确率的均值)
# accuracy_ARN_joint = [0.978667,0.934556, 0.775000,0.815444,0.706667,0.950000,0.795429,0.630159]
# accuracy_ARN_temp = [0.975000,0.957000,0.940000,0.886556,0.778667, 0.940000,0.821857,0.751111]
# accuracy_ARN_joint_temp= []
# accuracy_ARN_fc1_joint_temp= []
# # # 设置图表大小
# plt.figure(figsize=(14, 7))
# # 绘制折线图
# plt.plot(accuracy_ARN_joint, 'rx', label='ARN_joint', linestyle='--')
# plt.plot(accuracy_ARN_temp, 'g^', label='ARN_temp', linestyle='--')
# plt.plot(accuracy_ARN_joint_temp, 'bo', label='ARN_joint_temd', linestyle='--')
# plt.plot(accuracy_ARN_fc1_joint_temp, 'ms', label='ARN-fc1_joint+temp', linestyle='--')


## chapter 5 ##
#以下分类准确率，均为return的准确率，求取准确率的平均值
acc_ARN_joint = [0.978667,0.934556,0.775000,0.815444,0.706667,0.950000,0.795429,0.630159]
acc_ARN_temp = [0.975000,0.957000,0.940000,0.886556,0.778667,0.940000,0.821857,0.751111]
acc_ARN_joint_temp = [ 0.995556,0.972000,0.925000,0.904667,0.832000,0.930000, 0.878714,0.748254]
ARN_fc1_joint_temp = [1.000000,0.968000, 0.950000,0.894111,0.866667,0.964000,0.869143,0.761984]
ARN_inward_no_motion = [0.965000, 0.955556,0.830000, 0.812222,0.594000,0.960000,0.806000,0.567302]
ARN_inward = [0.968000,0.987556,0.865000,0.895556,0.736667,0.968000,0.798857,0.715556]
ARN_outward_no_motion = [ 1.000000,0.976000,0.940000,0.905667,0.778667,0.934000,0.849714,0.762063]
ARN_outward = [0.990000,0.988000,0.935000,0.882333,0.742667,0.936000,0.805429,0.761349]
ARN_inward_outward_no_motin = [0.995000,0.968000,0.935000,0.914444,0.829333,0.960000,0.857857,0.778095]
ARN_inward_outward = [0.975000,0.960000,0.940000,0.913889,0.842667,0.984000,0.840286,0.745397]
ARN_fc1_inward_outward = [0.980000,0.988000,0.925000,0.920556,0.818667,0.982000,0.839000, 0.730397]

# 设置图表大小
plt.figure(figsize=(14, 7))
# 绘制折线图
plt.plot(acc_ARN_joint, 'ro', label='ARN_joint', linestyle='--')   # 红色圆圈
plt.plot(acc_ARN_temp, 'g^', label='ARN_temp', linestyle='--')   # 绿色上三角
plt.plot(acc_ARN_joint_temp, 'bs', label='ARN_joint_temp', linestyle='--')  # 蓝色方块
plt.plot(ARN_fc1_joint_temp, 'md', label='ARN-fc1_joint_temp', linestyle='--')  # 品红色菱形

plt.plot(ARN_inward_no_motion, 'cv', label='ARN_inward_no_motion', linestyle='--')  # 青色下三角
plt.plot(ARN_inward, 'r>', label='ARN_inward', linestyle='--')  # 红色右三角
plt.plot(ARN_outward_no_motion, 'g<', label='ARN_outward_no_motion', linestyle='--')  # 绿色左三角
plt.plot(ARN_outward, 'b*', label='ARN_outward', linestyle='--')  # 蓝色星号

plt.plot(ARN_inward_outward_no_motin, 'yx', label='ARN_inward_outward_no_motin', linestyle='--')  # 黄色 X 符号
plt.plot(ARN_inward_outward, 'k+', label='ARN_inward_outward', linestyle='--')  # 黑色加号
plt.plot(ARN_fc1_inward_outward, 'o', color='#000080', label='ARN_fc1_inward_outward', linestyle='--')  # 白色五边形


# 常见的标记符号:
# 'o' : 圆圈
# 's' : 方块
# '^' : 上三角
# 'v' : 下三角
# '>' : 右三角
# '<' : 左三角
# 'd' : 菱形
# 'x' : X 符号
# '+' : 加号
# '*' : 星号
# 常见的颜色代码:
# 'r' : 红色
# 'g' : 绿色
# 'b' : 蓝色
# 'c' : 青色
# 'm' : 品红色
# 'y' : 黄色
# 'k' : 黑色
# 'w' : 白色


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
plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/SBU/ARN(chapter5-sbu)-all_acc_vs.png',dpi=300,bbox_inches='tight')
plt.show()
