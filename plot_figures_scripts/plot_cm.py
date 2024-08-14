import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 绘制对比混淆矩阵

# 示例数据，替换为你的实际混淆矩阵数据
classes = [
    'Punch/slapping', 'Kicking', 'Pushing', 'PattingOnBack', 'PointingFinger',
    'Hugging', 'GiveSomething', 'TouchingPocket', 'Handshaking', 'WalkingTowards',
    'WalkingApart', 'HitWithObject', 'WieldKnife', 'KnockOver', 'GrabStuff',
    'ShootWithGun', 'StepOnFoot', 'High-five', 'CheersAndDrink', 'CarryObject',
    'TakePhoto', 'Follow', 'Whisper', 'ExchangeThings', 'SupportSomebody',
    'RockPaperScissors'
]

# 构造随机数据作为混淆矩阵的例子
np.random.seed(0)
conf_matrix1 = np.random.rand(len(classes), len(classes))
conf_matrix2 = np.random.rand(len(classes), len(classes))

# 归一化矩阵到0-1之间
conf_matrix1 = conf_matrix1 / conf_matrix1.max()
conf_matrix2 = conf_matrix2 / conf_matrix2.max()

# 设置画布
fig, axes = plt.subplots(1, 2, figsize=(15, 6))
sns.set(font_scale=1.2)

# 绘制第一个混淆矩阵
sns.heatmap(conf_matrix1, annot=False, cmap='jet', ax=axes[0], cbar=False, xticklabels=classes, yticklabels=classes)
axes[0].set_title('Cross-Subject', fontsize=16)
axes[0].set_xticklabels(classes, rotation=45,ha="right")
axes[0].set_yticklabels(classes, rotation=0)

# 绘制第二个混淆矩阵
sns.heatmap(conf_matrix2, annot=False, cmap='jet', ax=axes[1], cbar=True, xticklabels=classes, yticklabels=classes)
axes[1].set_title('Cross-Setup', fontsize=16)
axes[1].set_xticklabels(classes, rotation=45,ha="right")
axes[1].set_yticklabels(classes, rotation=0)

# 添加整体图像标题
fig.suptitle('(a)                                (b)', fontsize=14, y=0.02)
plt.tight_layout()
plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/plot_cm.png',dpi=300,bbox_inches='tight')
plt.show()
