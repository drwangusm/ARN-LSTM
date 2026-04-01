import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 绘制SBU的对比混淆矩阵

# 8 classes of mutual actions
classes = ['Approaching','Departing','Kicking','Punching','Pushing','Hugging','ShakingHands','Exchanging']

### RN-joint ####
conf_matrix1 = [[7,0,0,1,0,0,0,0],
[0,8,0,0,0,0,0,0],
[0,0,7,0,0,0,1,0],
[0,0,0,8,0,0,0,1],
[0,0,0,0,2,0,1,0],
[0,0,0,0,0,4,0,0],
[0,0,0,0,0,0,7,0],
[2,1,0,0,1,0,2,2],
]

## RN-temp ##
conf_matrix2 = [[5,2,0,1,0,0,0,0],
[1,7,0,0,0,0,0,0],
[0,0,8,0,0,0,0,0],
[0,0,0,8,0,1,0,0],
[0,0,0,0,3,0,0,0],
[0,0,0,0,0,4,0,0],
[0,0,0,0,0,0,7,0],
[1,0,0,1,2,0,1,3],
]

## RN-joint+temp ##
conf_matrix3 = [[8,0,0,0,0,0,0,0],
[0,8,0,0,0,0,0,0],
[0,0,7,0,0,0,0,1],
[0,0,0,8,0,1,0,0],
[0,0,0,0,2,0,1,0],
[0,0,0,0,0,4,0,0],
[0,0,0,0,0,0,7,0],
[1,0,0,0,1,0,1,5],
]

# 🔹 修改这里：3行1列（垂直排列）
fig, axes = plt.subplots(3, 1, figsize=(12, 26))
sns.set(font_scale=1.2)

# 第1个
sns.heatmap(conf_matrix1, annot=True, fmt="d", cmap='coolwarm',
            ax=axes[0], cbar=True, xticklabels=classes, yticklabels=classes)
axes[0].set_title('Confusion matrix using joint stream', fontsize=16)
axes[0].set_xticklabels(classes, rotation=45, ha="right", fontsize=16)
axes[0].set_yticklabels(classes, rotation=0, fontsize=16)

# 第2个
sns.heatmap(conf_matrix2, annot=True, fmt="d", cmap='coolwarm',
            ax=axes[1], cbar=True, xticklabels=classes, yticklabels=classes)
axes[1].set_title('Confusion matrix using temporal stream', fontsize=16)
axes[1].set_xticklabels(classes, rotation=45, ha="right", fontsize=16)
axes[1].set_yticklabels(classes, rotation=0, fontsize=16)

# 第3个
sns.heatmap(conf_matrix3, annot=True, fmt="d", cmap='coolwarm',
            ax=axes[2], cbar=True, xticklabels=classes, yticklabels=classes)
axes[2].set_title('Confusion matrix using joint and temporal stream', fontsize=16)
axes[2].set_xticklabels(classes, rotation=45, ha="right", fontsize=16)
axes[2].set_yticklabels(classes, rotation=0, fontsize=16)

# 下方标签
axes[0].text(0.5, -0.35, '(a) RN_joint', fontsize=18,
             fontweight='bold', ha='center', transform=axes[0].transAxes)
axes[1].text(0.5, -0.35, '(b) RN_temp', fontsize=18,
             fontweight='bold', ha='center', transform=axes[1].transAxes)
axes[2].text(0.5, -0.35, '(c) RN_joint+temp', fontsize=18,
             fontweight='bold', ha='center', transform=axes[2].transAxes)

plt.tight_layout()
plt.subplots_adjust(hspace=0.5)   # 🔹 增加垂直间距（数值可调：0.4~0.8）

plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/SBU/RN-all_cm_v.png',
            dpi=300, bbox_inches='tight')
plt.show()