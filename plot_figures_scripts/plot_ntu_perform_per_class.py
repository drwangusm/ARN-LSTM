import matplotlib.pyplot as plt
import numpy as np

#基于模型训练结果，绘制数据集的各类表标签的性能,水平柱状图显示

# 类别标签
# NTU RGB+D 60类别标签
labels = ['Punch/slap','Kicking','Pushing','Pat on the back','Hugging','Hugging','Giving object',
           'Touch pocket','Shake hands','Walk towards','Walk apart']

# NTU RGB+D 120类别标签
# labels = ['Punch/slapping', 'Kicking', 'Pushing', 'PattingOnBack', 'PointingFinger', 'Hugging', 'GiveSomething', 
#           'TouchingPocket', 'Handshaking', 'WalkingTowards', 'WalkingApart', 'HitWithObject', 'WieldKnife', 
#           'KnockOver', 'GrabStuff', 'ShootWithGun', 'StepOnFoot', 'High-five', 'CheersAndDrink', 
#           'CarryObject', 'TakePhoto', 'Follow', 'Whisper', 'ExchangeThings', 'SupportSomebody', 'RockPaperScissors']

# Cross-Subject 和 Cross-View 的准确率数据 (将数据乘以 100 转换为百分比)
# #ARN-LSTM_inward
cross_subject = [0.7159468438538206,0.7863105175292153,0.7018544935805991,0.7614213197969543,0.7940594059405941,0.8333333333333334,0.7464167585446527,0.8012976480129764,0.7410358565737052,0.9221183800623053,0.8924544666088465]
cross_view = [0.7218844984802432,0.8639876352395672,0.8463576158940397,0.8527315914489311,0.7504587155963303,0.9374167776298269,0.7437934458788481,0.8,0.7873357228195937,0.9085106382978724,0.8974960876369327]

# #ARN-LSTM_outward
# cross_subject = [0.7192691029900332,0.6460767946577629,0.724679029957204,0.7550761421319797,0.7762376237623763,0.865546218487395,0.6923925027563396,0.7858880778588808,0.7264276228419655,0.8372274143302181,0.8933217692974849]
# cross_view = [0.6747720364741642,0.8701700154559505,0.7827814569536424,0.83729216152019,0.7981651376146789,0.9107856191744341,0.7269116186693148,0.8,0.8016726403823178,0.9319148936170213,0.8794992175273866]


# 转换为百分数
cross_subject = [x * 100 for x in cross_subject]
cross_view = [x * 100 for x in cross_view]

# 定义柱状图的位置
x = np.arange(len(labels))
width = 0.35  # 每个柱子的宽度

# 创建子图
fig, ax = plt.subplots(figsize=(10, 8))

# 画柱状图
rects1 = ax.barh(x - width/2, cross_subject, width, label='Cross-Subject')
rects2 = ax.barh(x + width/2, cross_view, width, label='Cross-View')

# 添加标签、标题和自定义x轴刻度
ax.set_xlabel('Accuracy (%)') # The ARN-LSTM_inward method accurancy of 11 mutual actions on NTU RGB+D 60
ax.set_title('Accuracy by action category')
ax.set_yticks(x)
ax.set_yticklabels(labels)
ax.legend()

# 设置 x 轴刻度每 10% 显示一次
ax.set_xticks(np.arange(0, 101, 10))

# 显示百分数格式的 x 轴标签
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}'))

# 调整布局
fig.tight_layout()

plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/NTU-V1/ARN-LSTM_inward-performence_per_class.png',dpi=300,bbox_inches='tight')  #保存并命名图片
# 显示图像
plt.show()
