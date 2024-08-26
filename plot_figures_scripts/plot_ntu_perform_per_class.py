import matplotlib.pyplot as plt
import numpy as np

#基于模型训练结果，绘制数据集的各类表标签的性能,水平柱状图显示

# 类别标签
# NTU RGB+D 60类别标签
labels = ['Punch/slap','Kicking','Pushing','Pat on the back','Hugging','Hugging','Giving object',
           'Touch pocket','Shake hands','Walk towards','Walk apart']

# Cross-Subject 和 Cross-View 的准确率数据 (将数据乘以 100 转换为百分比)
# #ARN-LSTM_inward
# cross_subject = [0.7159468438538206,0.7863105175292153,0.7018544935805991,0.7614213197969543,0.7940594059405941,0.8333333333333334,0.7464167585446527,0.8012976480129764,0.7410358565737052,0.9221183800623053,0.8924544666088465]
# cross_view = [0.7218844984802432,0.8639876352395672,0.8463576158940397,0.8527315914489311,0.7504587155963303,0.9374167776298269,0.7437934458788481,0.8,0.7873357228195937,0.9085106382978724,0.8974960876369327]

# #ARN-LSTM_outward
# cross_subject = [0.7192691029900332,0.6460767946577629,0.724679029957204,0.7550761421319797,0.7762376237623763,0.865546218487395,0.6923925027563396,0.7858880778588808,0.7264276228419655,0.8372274143302181,0.8933217692974849]
# cross_view = [0.6747720364741642,0.8701700154559505,0.7827814569536424,0.83729216152019,0.7981651376146789,0.9107856191744341,0.7269116186693148,0.8,0.8016726403823178,0.9319148936170213,0.8794992175273866]

# ARN-LSTM_inward+outward
# cross_subject=[0.7641196013289037,0.7729549248747913,0.7945791726105563,0.7918781725888325,0.7801980198019802,0.8823529411764706,0.7585446527012127,0.8175182481751825,0.8061088977423638,0.9158878504672897,0.8872506504770165]
# cross_view = [0.7872340425531915,0.8578052550231839,0.8940397350993378,0.7624703087885986,0.8752293577981651,0.9360852197070573,0.7368421052631579,0.8321285140562249,0.8530465949820788,0.9056737588652483,0.9006259780907668]

#ARN-LSTM-fc1_inward+outward
# cross_subject=[0.7990033222591362,0.8063439065108514,0.8174037089871612,0.815989847715736,0.80990099009901,0.9103641456582633,0.7618522601984564,0.7980535279805353,0.7397078353253652,0.8901869158878505,0.8907198612315698]
# cross_view = [0.8358662613981763,0.8887171561051005,0.8543046357615894,0.8396674584323041,0.8605504587155963,0.933422103861518,0.7358490566037735,0.8096385542168675,0.8148148148148148,0.9340425531914893,0.9194053208137715]

# NTU RGB+D 120类别标签
# labels = ['Punch/slapping', 'Kicking', 'Pushing', 'PattingOnBack', 'PointingFinger', 'Hugging', 'GiveSomething', 
#           'TouchingPocket', 'Handshaking', 'WalkingTowards', 'WalkingApart', 'HitWithObject', 'WieldKnife', 
#           'KnockOver', 'GrabStuff', 'ShootWithGun', 'StepOnFoot', 'High-five', 'CheersAndDrink', 
#           'CarryObject', 'TakePhoto', 'Follow', 'Whisper', 'ExchangeThings', 'SupportSomebody', 'RockPaperScissors']

cross_subject=[]
cross_view=[]

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

plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/NTU-V2/ARN-LSTM-fc1_inward+outward-performence_per_class.png',dpi=300,bbox_inches='tight')  #保存并命名图片
# 显示图像
plt.show()
