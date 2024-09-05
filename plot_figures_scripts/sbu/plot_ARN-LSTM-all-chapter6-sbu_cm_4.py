import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 绘制SBU的对比混淆矩阵

# 8 classes of mutual actions
classes = ['Approaching','Departing','Kicking','Punching','Pushing','Hugging','ShakingHands','Exchanging']

# 注意：混淆矩阵取值均为在最佳epoch下的混淆矩阵
### ARN-LSTM_inward ####
conf_matrix1 = [
[7,0,0,1,0,0,0,0],
[0,8,0,0,0,0,0,0],
[0,1,6,0,0,0,0,1],
[0,0,0,9,0,0,0,0],
[0,0,0,0,3,0,0,0],
[0,0,0,0,0,4,0,0],
[0,0,0,0,1,0,6,0],
[2,1,0,1,0,0,0,4],
]

## ARN-LSTM_outward ##
conf_matrix2 = [
[8,0,0,0,0,0,0,0],
[0,8,0,0,0,0,0,0],
[0,0,8,0,0,0,0,0],
[0,0,0,9,0,0,0,0],
[0,0,0,0,2,0,1,0],
[0,0,0,0,0,4,0,0],
[0,0,0,0,0,0,7,0],
[3,0,0,0,2,0,1,2],
]

## ARN-LSTM_inward+outward ##
conf_matrix3 = [
[7,0,0,1,0,0,0,0],
[0,8,0,0,0,0,0,0],
[0,0,8,0,0,0,0,0],
[0,0,0,8,0,1,0,0],
[0,0,0,0,2,0,1,0],
[0,0,0,0,0,4,0,0],
[0,0,0,0,0,0,7,0],
[3,0,0,0,1,0,1,3],
]

## ARN-LSTM-fc1_inward+outward ##
conf_matrix4 = [
[10,0,0,0,0,0,0,0],
[0,7,0,0,0,0,3,0],
[0,0,8,0,0,0,0,0],
[0,0,0,10,0,0,0,0],
[0,0,0,0,5,0,0,0],
[0,0,0,0,0,5,0,0],
[0,0,0,0,3,0,7,0],
[0,0,0,0,0,0,0,7],
]

# 设置画布
fig, axes = plt.subplots(2, 2, figsize=(22, 18))
sns.set(font_scale=1.2)

# 绘制第1个混淆矩阵
sns.heatmap(conf_matrix1, annot=True, fmt="d", cmap='coolwarm',ax=axes[0][0], cbar=True, xticklabels=classes, yticklabels=classes)
axes[0][0].set_title('Confusion matrix with inward sequences', fontsize=16)
axes[0][0].set_xticklabels(classes, rotation=45,ha="right",fontsize=16)
axes[0][0].set_yticklabels(classes, rotation=0,fontsize=16)

# 绘制第2个混淆矩阵
sns.heatmap(conf_matrix2, annot=True, fmt="d", cmap='coolwarm',ax=axes[0][1], cbar=True, xticklabels=classes, yticklabels=classes)
axes[0][1].set_title('Confusion matrix with outward sequences', fontsize=16)
axes[0][1].set_xticklabels(classes, rotation=45,ha="right",fontsize=16)
axes[0][1].set_yticklabels(classes, rotation=0,fontsize=16)

# 绘制第3个混淆矩阵
sns.heatmap(conf_matrix3, annot=True, fmt="d", cmap='coolwarm',ax=axes[1][0], cbar=True, xticklabels=classes, yticklabels=classes)
axes[1][0].set_title('Confusion matrix with inward and outward sequences', fontsize=16)
axes[1][0].set_xticklabels(classes, rotation=45,ha="right",fontsize=16)
axes[1][0].set_yticklabels(classes, rotation=0,fontsize=16)

# 绘制第4个混淆矩阵
sns.heatmap(conf_matrix4, annot=True, fmt="d", cmap='coolwarm',ax=axes[1][1], cbar=True, xticklabels=classes, yticklabels=classes)
axes[1][1].set_title('Confusion matrix using full connection with inward and outward sequences', fontsize=16)
axes[1][1].set_xticklabels(classes, rotation=45,ha="right",fontsize=16)
axes[1][1].set_yticklabels(classes, rotation=0,fontsize=16)

# 添加下方标签
axes[0][0].text(0.5, -0.25, '(a) ARN-LSTM_inward ', fontsize=18, fontweight='bold', ha='center', transform=axes[0][0].transAxes)
axes[0][1].text(0.5, -0.25, '(b) ARN-LSTM_outward ', fontsize=18, fontweight='bold', ha='center', transform=axes[0][1].transAxes)
axes[1][0].text(0.5, -0.25, '(b) ARN-LSTM_inward+outward ', fontsize=18, fontweight='bold', ha='center', transform=axes[1][0].transAxes)
axes[1][1].text(0.5, -0.25, '(d) ARN-LSTM-fc1_inward+outward ', fontsize=18, fontweight='bold', ha='center', transform=axes[1][1].transAxes)

# 调整布局
plt.tight_layout()

plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/SBU/ARN-LSTM-all-chapter6_cm_4.png',dpi=300,bbox_inches='tight') #保存并命名图片
plt.show()
