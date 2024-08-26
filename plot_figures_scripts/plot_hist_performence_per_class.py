import matplotlib.pyplot as plt
import numpy as np

#基于模型训练结果，绘制数据集的各类表标签的性能,柱状图显示

# 类别标签 NTU RGB+D 120
labels = ['Punch/slapping', 'Kicking', 'Pushing', 'PattingOnBack', 'PointingFinger', 'Hugging', 'GiveSomething', 
          'TouchingPocket', 'Handshaking', 'WalkingTowards', 'WalkingApart', 'HitWithObject', 'WieldKnife', 
          'KnockOver', 'GrabStuff', 'ShootWithGun', 'StepOnFoot', 'High-five', 'CheersAndDrink', 
          'CarryObject', 'TakePhoto', 'Follow', 'Whisper', 'ExchangeThings', 'SupportSomebody', 'RockPaperScissors']

# Cross-Subject 和 Cross-Setup 的准确率数据
cross_subject = [70, 60, 65, 72, 80, 85, 75, 68, 77, 82, 50, 40, 30, 60, 55, 78, 50, 85, 70, 73, 80, 78, 65, 74, 90, 85]
cross_setup = [65, 58, 60, 70, 75, 80, 72, 65, 74, 80, 48, 38, 28, 55, 52, 76, 48, 83, 68, 70, 78, 75, 62, 70, 88, 82]

# 定义柱状图的位置
x = np.arange(len(labels))
width = 0.35  # 每个柱子的宽度

# 创建子图
fig, ax = plt.subplots(figsize=(10, 8))

# 画柱状图
rects1 = ax.barh(x - width/2, cross_subject, width, label='Cross-Subject')
rects2 = ax.barh(x + width/2, cross_setup, width, label='Cross-Setup')

# 添加标签、标题和自定义x轴刻度
ax.set_xlabel('Accuracy')
ax.set_title('Accuracy by action category')
ax.set_yticks(x)
ax.set_yticklabels(labels)
ax.legend()

# 调整布局
fig.tight_layout()

plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/NTU-V2/performence_per_class.png',dpi=300,bbox_inches='tight')
# 显示图像
plt.show()
