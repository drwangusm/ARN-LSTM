import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 绘制NTU RGB+D 60/120的对比混淆矩阵

# NTU-V1 dataset (NTU RGB+D 60)
# 11 classes of mutual actions
classes = ['Punch/slap','Kicking','Pushing','Pat on the back','Point finger','Hugging','Giving object',
           'Touch pocket','Shake hands','Walk towards','Walk apart']

# 注意：混淆矩阵取值均为在最佳epoch下的混淆矩阵
### ARN-LSTM_inward ####
# cross_subject
conf_matrix1 = [[431, 20, 14, 34, 22, 4, 30, 35, 2, 5, 5],
[45, 471, 5, 3, 11, 1, 11, 17, 9, 8, 18],
[41, 3, 492, 31, 0, 29, 7, 39, 2, 5, 52],
[42, 4, 14, 600, 6, 6, 7, 92, 9, 4, 4],
[31, 2, 0, 7, 401, 0, 37, 9, 14, 2, 2],
[31, 3, 5, 11, 0, 595, 3, 44, 2, 7, 13],
[15, 7, 5, 6, 21, 0, 677, 20, 144, 5, 7],
[27, 9, 12, 54, 9, 16, 18, 988, 51, 13, 36],
[5,2, 1, 3, 9, 0,154, 15, 558, 4, 2],
[10, 3, 1, 0, 1, 5, 4, 3, 1, 1184, 72],
[6, 7, 3, 2, 0, 5, 1, 7, 0, 93, 1029]]

# # cross_view
conf_matrix2 = [[475, 24, 33, 59, 8, 9, 16, 20, 2, 8, 4],
[25, 559, 9, 7, 1, 4, 12, 16, 1, 7, 6],
[12, 4, 639, 40, 0, 23, 4, 14, 0, 6, 13],
[10, 3, 39, 718, 3, 6, 6, 48, 3, 5, 1],
[42, 4, 1, 47, 409, 2, 23, 6, 9, 2, 0],
[5, 5, 6,4, 0, 704, 2, 11, 1, 5, 8],
[11, 9, 11, 11, 25, 2, 749, 46, 136, 6, 1],
[13, 9, 27, 102, 8, 31, 17, 996, 23, 7, 12],
[7, 2, 1, 7, 7, 1, 99, 47, 659, 5, 2],
[10, 11, 5, 1, 0, 4, 2, 9, 3, 1281, 84],
[7, 9, 11, 2, 0, 6, 2, 12, 0, 82, 1147]]

### ARN-LSTM_outward ####
#最佳epoch 91
conf_matrix3 = [[433, 11, 26, 29, 30, 6, 12, 35, 3, 6, 11],
[62, 387, 14, 4, 16, 2, 8, 50, 10, 11, 35],
[31, 5, 508, 46, 2, 40, 4, 22, 0, 3, 40],
[31, 2, 16, 595, 5, 8, 7, 114, 3, 1, 6],
[60, 0, 2, 11, 392, 1, 15, 17, 5, 0, 2],
[15, 5, 7, 11, 4, 618, 4, 29, 4, 3, 14],
[24, 6, 15, 5, 40, 3, 628, 41, 130, 7, 8],
[29, 8, 26, 86, 5, 37, 12, 969, 15, 16, 30],
[6, 3, 1, 8, 19, 1, 109, 53, 547, 4, 2],
[14, 3, 0, 3, 3, 4, 6, 14, 0, 1075, 162],
[4, 6, 12, 5, 0, 3, 3, 17, 1, 72, 1030]]

conf_matrix4 = [[444, 50, 27, 55, 24, 9, 9, 24, 2, 7, 7],
[17, 563, 5, 6, 2, 3, 6, 28, 2, 10, 5],
[27, 6, 591, 45, 1, 22, 7, 29, 1, 6, 20],
[20, 3, 31, 705, 2, 5, 6, 65, 4, 0, 1],
[43, 2, 1, 28, 435, 1, 16, 8, 10, 1, 0],
[10, 8, 7, 9, 0, 684, 3, 15, 2, 7, 6],
[21, 22, 6, 12, 24, 1, 732, 38, 146, 3, 2],
[21, 12, 13, 119, 3, 26, 18, 996, 23, 3, 11],
[5, 15, 1, 5, 11, 2, 87, 36, 671, 2, 2],
[10, 16, 5, 3, 1, 3, 5, 23, 0, 1314, 30],
[7, 14, 7, 2, 0, 5, 5, 14, 0, 100, 1124]]

# 设置画布
fig, axes = plt.subplots(2, 2, figsize=(30, 24))
sns.set(font_scale=1.2)

# 绘制第一个混淆矩阵
sns.heatmap(conf_matrix1, annot=True, fmt="d", cmap='coolwarm',ax=axes[0][0], cbar=False, xticklabels=classes, yticklabels=classes)
axes[0][0].set_title('Cross-subject', fontsize=16)
axes[0][0].set_xticklabels(classes, rotation=45,ha="right",fontsize=16)
axes[0][0].set_yticklabels(classes, rotation=0,fontsize=16)

# 绘制第二个混淆矩阵
sns.heatmap(conf_matrix2, annot=True, fmt="d", cmap='coolwarm',ax=axes[0][1], cbar=True, xticklabels=classes, yticklabels=classes)
axes[0][1].set_title('Cross-view', fontsize=16)
axes[0][1].set_xticklabels(classes, rotation=45,ha="right",fontsize=16)
axes[0][1].set_yticklabels(classes, rotation=0,fontsize=16)

# 绘制第3个混淆矩阵
sns.heatmap(conf_matrix3, annot=True, fmt="d", cmap='coolwarm',ax=axes[1][0], cbar=False, xticklabels=classes, yticklabels=classes)
axes[1][0].set_title('Cross-subject', fontsize=16)
axes[1][0].set_xticklabels(classes, rotation=45,ha="right",fontsize=16)
axes[1][0].set_yticklabels(classes, rotation=0,fontsize=16)

# 绘制第4个混淆矩阵
sns.heatmap(conf_matrix4, annot=True, fmt="d", cmap='coolwarm',ax=axes[1][1], cbar=True, xticklabels=classes, yticklabels=classes)
axes[1][1].set_title('Cross-view', fontsize=16)
axes[1][1].set_xticklabels(classes, rotation=45,ha="right",fontsize=16)
axes[1][1].set_yticklabels(classes, rotation=0,fontsize=16)

# 添加下方标签
axes[0][0].text(0.5, -0.25, '(a) The ARN-LSTM_inward cross subject confusion matrix', fontsize=18, fontweight='bold', ha='center', transform=axes[0][0].transAxes)
axes[0][1].text(0.5, -0.25, '(b) The ARN-LSTM_inward cross view confusion matrix', fontsize=18, fontweight='bold', ha='center', transform=axes[0][1].transAxes)
axes[1][0].text(0.5, -0.25, '(c) The ARN-LSTM_outward cross subject confusion matrix', fontsize=18, fontweight='bold', ha='center', transform=axes[1][0].transAxes)
axes[1][1].text(0.5, -0.25, '(d) The ARN-LSTM_outward cross view confusion matrix', fontsize=18, fontweight='bold', ha='center', transform=axes[1][1].transAxes)

# 调整子图之间的垂直间距
plt.subplots_adjust(hspace=0.5)  # 通过 hspace 参数调整垂直间距

# 调整布局
plt.subplots_adjust(bottom=0.1, top=0.9)  # 手动调整画布边距，确保标签可见

# 调整布局
# plt.tight_layout()

plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/ARN-LSTM_cm.png',dpi=300,bbox_inches='tight') #保存并命名图片
plt.show()
