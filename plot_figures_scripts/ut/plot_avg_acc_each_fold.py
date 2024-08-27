import matplotlib.pyplot as plt
import numpy as np

#基于模型训练结果，绘制数据集的各fold数据集的平均识别率性能,竖直柱状图显示

# 类别标签
# SBU fold标签
labels = ['fold_0','fold_1','fold_2','fold_3','fold_4','fold_5','fold_6','fold_7','fold_8','fold_9']

# ARN-LSTM_inward,ARN-LSTM_outward,ARN-LSTM_inward+outward 和 ARN-LSTM-fc1_inward+outward 的准确率数据 (将数据乘以 100 转换为百分比)
ARN_LSTM_inward = [0.9955947399139404,0.995652198791504,0.9778761267662048,0.9605262875556946,0.990783393383026]
ARN_LSTM_outward = [0.9867841601371765,0.9956521987915039,0.9734513163566589,0.9780701994895935,0.9953917264938354]
ARN_LSTM_inward_outward = [1.0,1.0,0.9955752491950988,0.9956140518188475,0.9953917264938354]
ARN_LSTM_fc1_inward_outward = [0.9691630005836487,0.9521738886833191,0.9601770043373108,0.9868420958518982,0.9723502397537231]

# 转换为百分数
ARN_LSTM_inward = [x * 100 for x in ARN_LSTM_inward]
ARN_LSTM_outward = [x * 100 for x in ARN_LSTM_outward]
ARN_LSTM_inward_outward = [x * 100 for x in ARN_LSTM_inward_outward]
ARN_LSTM_fc1_inward_outward = [x * 100 for x in ARN_LSTM_fc1_inward_outward]



# 定义柱状图的位置
x = np.arange(len(labels))
width = 0.15  # 每个柱子的宽度

# 创建子图
fig, ax = plt.subplots(figsize=(8, 9))

# # 画柱状图,水平显示
# rects1 = ax.barh(x - width/4, ARN_LSTM_inward, width, label='ARN_LSTM_inward')
# rects2 = ax.barh(x + width/4, ARN_LSTM_outward, width, label='ARN_LSTM_outward')
# rects3 = ax.barh(x + width/4, ARN_LSTM_inward, width, label='ARN_LSTM_inward_outward')
# rects4 = ax.barh(x + width/4, ARN_LSTM_outward, width, label='ARN_LSTM_fc1_inward_outward')

# 画柱状图,垂直显示
rects1 = ax.bar(x - width*1.5, ARN_LSTM_inward, width, label='ARN_LSTM_inward')
rects2 = ax.bar(x - width*0.5, ARN_LSTM_outward, width, label='ARN_LSTM_outward')
rects3 = ax.bar(x + width*0.5, ARN_LSTM_inward, width, label='ARN_LSTM_inward_outward')
rects4 = ax.bar(x + width*1.5, ARN_LSTM_outward, width, label='ARN_LSTM_fc1_inward_outward')


# 添加标签、标题和自定义x轴刻度
ax.set_ylabel('Accuracy (%)') # The ARN-LSTM_inward method accurancy of 11 mutual actions on NTU RGB+D 60
ax.set_xlabel('Fold')
ax.set_title('Average accuracy by each fold of the SBU dataset')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# 设置 y 轴刻度每 10% 显示一次
ax.set_yticks(np.arange(0, 101, 10))

# 显示百分数格式的 y 轴标签
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'fold_{int(y)}'))

# 旋转 X 轴标签以使其垂直显示
# plt.xticks(rotation=45)

# 调整图例的位置，将其放在图形外部的顶部
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2)

# 调整布局
fig.tight_layout()

plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/SBU/ARN-LSTM-all_avg_acc_each_fold.png',dpi=300,bbox_inches='tight')  #保存并命名图片
# 显示图像
plt.show()
