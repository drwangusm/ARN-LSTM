import matplotlib.pyplot as plt
import numpy as np

#基于模型训练结果，绘制数据集的各类表标签的性能,柱状图显示

# 类别标签 NTU RGB+D 120
labels = ['Punch/slapping', 'Kicking', 'Pushing', 'PattingOnBack', 'PointingFinger', 'Hugging', 'GiveSomething', 
          'TouchingPocket', 'Handshaking', 'WalkingTowards', 'WalkingApart', 'HitWithObject', 'WieldKnife', 
          'KnockOver', 'GrabStuff', 'ShootWithGun', 'StepOnFoot', 'High-five', 'CheersAndDrink', 
          'CarryObject', 'TakePhoto', 'Follow', 'Whisper', 'ExchangeThings', 'SupportSomebody', 'RockPaperScissors']

# Cross-Subject 和 Cross-Setup 的准确率数据
cross_subject = [0.6240875912408759,0.677536231884058,0.7862318840579711,0.7608695652173914,0.7065217391304348,0.9379562043795621,0.5144927536231884,0.7490909090909091,0.6340579710144928,0.9413919413919414,0.855072463768116,0.43478260869565216,0.28125,0.6545138888888888,0.6313043478260869,0.40347826086956523,0.6904347826086956,0.8975694444444444,0.8591304347826086,0.8940972222222222,0.7951388888888888,0.7795138888888888,0.7373913043478261,0.7982608695652174,0.7773913043478261,0.765625]
cross_view = [0.6052104208416834,0.7290836653386454,0.7892644135188867,0.7440476190476191,0.738430583501006,0.8791666666666667,0.49404761904761907,0.6461232604373758,0.753968253968254,0.9298597194388778,0.8727634194831014,0.3665987780040733,0.3800813008130081,0.769857433808554,0.6036585365853658,0.5387755102040817,0.7291242362525459,0.75,0.7987804878048781,0.890020366598778,0.7331975560081466,0.823170731707317,0.6802443991853361,0.8008130081300813,0.7408163265306122,0.7235772357723578]

# 定义柱状图的位置
x = np.arange(len(labels))
width = 0.35  # 每个柱子的宽度

# 创建子图
fig, ax = plt.subplots(figsize=(10, 8))

# 画柱状图
rects1 = ax.bar(x - width/2, cross_subject, width, label='Cross-Subject')
rects2 = ax.bar(x + width/2, cross_view, width, label='Cross-View')

# 添加标签、标题和自定义x轴刻度
ax.set_xlabel('Accuracy')
ax.set_title('Accuracy by action category')
ax.set_yticks(x)
ax.set_yticklabels(labels)
ax.legend()

# 调整布局
fig.tight_layout()

plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/NTU-V2/ARN-LSTM_outward_performence_per_class_2.png',dpi=300,bbox_inches='tight')
# 显示图像
plt.show()
