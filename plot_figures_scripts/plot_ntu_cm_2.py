import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 绘制NTU RGB+D 60/120的对比混淆矩阵

# NTU-V1 dataset (NTU RGB+D 60)
# 11 classes of mutual actions
classes = ['Punch/slap','Kicking','Pushing','Pat on the back','Point finger','Hugging','Giving object',
           'Touch pocket','Shake hands','Walk towards','Walk apart']

# 注意：混淆矩阵取值均为在最佳epoch下的混淆矩阵
### ARN-LSTM_inward+outward ####
# cross_subject 121
conf_matrix1 = [[460, 18, 18, 29, 13, 4, 14, 31, 3, 4, 8],
[47, 463, 6, 4, 7, 4, 14, 30, 3, 10, 11],
[25, 5, 557, 18, 3, 42, 6, 20, 1, 2, 22],
[29, 4, 12, 624, 5, 8, 2, 81, 15, 0, 8],
[52, 4, 0, 14, 394, 0, 23, 7, 10, 1, 0],
[14, 5, 5, 7, 3, 630, 8, 26, 0, 5, 11],
[14, 6, 9, 5, 21, 2, 688, 20, 131, 3, 8],
[23, 14, 17, 62, 3, 24, 22, 1008, 17, 9, 34],
[5, 4, 0, 3, 4, 0, 104, 18, 607, 4, 4],
[11, 7, 4, 1, 2, 5, 2, 9, 0, 1176, 67],
[5, 8, 2, 1, 2, 6, 6, 12, 0, 88, 1023]]

# # cross_view
conf_matrix2 = [[518, 20, 37, 13, 21, 7, 11, 16, 6, 8, 1],
[30, 555, 9, 2, 8, 2, 11, 13, 1, 9, 7],
[14, 1, 675, 13, 1, 9, 6, 23, 0, 4, 9],
[26, 3, 70, 642, 2, 4, 5, 81, 5, 0, 4],
[28, 2, 4, 6, 477, 0, 10, 8, 9, 1, 0],
[10, 4, 10, 2, 0, 703, 3, 6, 2, 8,3],
[14, 6, 10, 3, 36, 0, 742, 26, 164, 4, 2],
[23, 5, 34, 64, 6, 27, 18, 1036, 19, 5, 8],
[5, 0, 0, 2, 12, 0, 82, 20, 714, 0, 2],
[18, 14, 9, 3, 4, 5, 5, 10, 0, 1277, 65],
[3, 4, 9, 0, 2, 11, 6, 11, 0, 81, 1151]]

# 设置画布
fig, axes = plt.subplots(1, 2, figsize=(15, 8))
sns.set(font_scale=1.2)

# 绘制第一个混淆矩阵
sns.heatmap(conf_matrix1, annot=True, fmt="d", cmap='coolwarm',ax=axes[0], cbar=False, xticklabels=classes, yticklabels=classes)
axes[0].set_title('Cross-subject', fontsize=16)
axes[0].set_xticklabels(classes, rotation=45,ha="right",fontsize=16)
axes[0].set_yticklabels(classes, rotation=0,fontsize=16)

# 绘制第二个混淆矩阵
sns.heatmap(conf_matrix2, annot=True, fmt="d", cmap='coolwarm',ax=axes[1], cbar=True, xticklabels=classes, yticklabels=classes)
axes[1].set_title('Cross-view', fontsize=16)
axes[1].set_xticklabels(classes, rotation=45,ha="right",fontsize=16)
axes[1].set_yticklabels(classes, rotation=0,fontsize=16)

# 添加下方标签
axes[0].text(0.5, -0.5, '(a) ARN-LSTM_inward+outward ', fontsize=18, fontweight='bold', ha='center', transform=axes[0].transAxes)
axes[1].text(0.5, -0.5, '(b) ARN-LSTM_inward+outward ', fontsize=18, fontweight='bold', ha='center', transform=axes[1].transAxes)

# 调整布局
plt.tight_layout()

plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/NTU-V1/ARN-LSTM_inward+outward_cm.png',dpi=300,bbox_inches='tight') #保存并命名图片
plt.show()
