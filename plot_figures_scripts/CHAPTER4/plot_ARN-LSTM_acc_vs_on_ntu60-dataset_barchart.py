# import matplotlib.pyplot as plt
# import numpy as np

# # ntu rgb+d 60标签
# labels = [
#     'Punch/slap','Kicking','Pushing','Pat on the back','Point finger','Hugging','Giving object','Touch pocket','Shake hands','Walk towards','Walk apart'
# ]

# # #cross_subject
# # accuracy_ARN_LSTM_inward = [0.7159468438538206,0.7863105175292153,0.7018544935805991,0.7614213197969543,0.7940594059405941,0.8333333333333334,0.7464167585446527,0.8012976480129764,0.7410358565737052,0.9221183800623053,0.8924544666088465]
# # accuracy_ARN_LSTM_outward = [0.7192691029900332,0.6460767946577629,0.724679029957204,0.7550761421319797,0.7762376237623763,0.865546218487395,0.6923925027563396,0.7858880778588808,0.7264276228419655,0.8372274143302181,0.8933217692974849]
# # accuracy_ARN_LSTM_inward_outward= [ 0.7641196013289037,0.7729549248747913,0.7945791726105563,0.7918781725888325,0.7801980198019802,0.8823529411764706,0.7585446527012127,0.8175182481751825,0.8061088977423638,0.9158878504672897,0.8872506504770165]
# # ARN_LSTM_fc1_inward_outward = [ 0.7990033222591362,0.8063439065108514,0.8174037089871612,0.815989847715736,0.80990099009901,0.9103641456582633,0.7618522601984564,0.7980535279805353,0.7397078353253652,0.8901869158878505,0.8907198612315698]


# #cross_view
# accuracy_ARN_LSTM_inward = [0.7218844984802432,0.8639876352395672,0.8463576158940397,0.8527315914489311,0.7504587155963303,0.9374167776298269,0.7437934458788481,0.8,0.7873357228195937,0.9085106382978724,0.8974960876369327]
# accuracy_ARN_LSTM_outward = [0.6747720364741642,0.8701700154559505,0.7827814569536424,0.83729216152019,0.7981651376146789,0.9107856191744341,0.7269116186693148,0.8,0.8016726403823178,0.9319148936170213,0.8794992175273866]
# accuracy_ARN_LSTM_inward_outward= [0.7872340425531915,0.8578052550231839,0.8940397350993378,0.7624703087885986,0.8752293577981651,0.9360852197070573,0.7368421052631579,0.8321285140562249,0.8530465949820788,0.9056737588652483,0.9006259780907668]
# ARN_LSTM_fc1_inward_outward = [0.8358662613981763,0.8887171561051005,0.8543046357615894,0.8396674584323041,0.8605504587155963,0.933422103861518,0.7358490566037735,0.8096385542168675,0.8148148148148148,0.9340425531914893,0.9194053208137715]


# # 设置图表大小
# plt.figure(figsize=(14, 7))

# # 绘制折线图
# plt.plot(accuracy_ARN_LSTM_inward, 'rx', label='ARN-LSTM_inward', linestyle='--')
# plt.plot(accuracy_ARN_LSTM_outward, 'g^', label='ARN-LSTM_outward', linestyle='--')
# plt.plot(accuracy_ARN_LSTM_inward_outward, 'bo', label='ARN-LSTM_inward_outward', linestyle='--')
# plt.plot(ARN_LSTM_fc1_inward_outward, 'ms', label='ARN-LSTM_fc1_inward_outward', linestyle='--')

# # 添加图例
# plt.legend()

# # 添加标签和标题
# plt.xlabel("Action Classes", fontsize=12, color='black')
# plt.ylabel("Accuracy (%)")
# plt.title("NTU RGB+D 60 dataset (Cross_view) action recognition performance comparison")

# # 设置x轴刻度并将标签颜色设置为黑色，字体大小设置为18
# plt.xticks(ticks=np.arange(len(labels)), labels=labels, rotation=60, ha="right", fontsize=12, color='black')

# # 显示网格
# plt.grid(True, linestyle='--', alpha=0.6)

# # 显示图表
# plt.tight_layout()
# plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/CHAPTER4/ARN-LSTM_ntu60_cv_acc_bar.png',dpi=300,bbox_inches='tight')
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# ntu rgb+d 60 标签
labels = [
    'Punch/slap', 'Kicking', 'Pushing', 'Pat on the back', 'Point finger', 
    'Hugging', 'Giving object', 'Touch pocket', 'Shake hands', 'Walk towards', 'Walk apart'
]

# # 原始数据 (Cross_view)
# accuracy_inward = np.array([0.7218844984802432, 0.8639876352395672, 0.8463576158940397, 0.8527315914489311, 0.7504587155963303, 0.9374167776298269, 0.7437934458788481, 0.8, 0.7873357228195937, 0.9085106382978724, 0.8974960876369327]) 
# accuracy_outward = np.array([0.6747720364741642, 0.8701700154559505, 0.7827814569536424, 0.83729216152019, 0.7981651376146789, 0.9107856191744341, 0.7269116186693148, 0.8, 0.8016726403823178, 0.9319148936170213, 0.8794992175273866]) 
# accuracy_inward_outward = np.array([0.7872340425531915, 0.8578052550231839, 0.8940397350993378, 0.7624703087885986, 0.8752293577981651, 0.9360852197070573, 0.7368421052631579, 0.8321285140562249, 0.8530465949820788, 0.9056737588652483, 0.9006259780907668]) 
# fc1_inward_outward = np.array([0.8358662613981763, 0.8887171561051005, 0.8543046357615894, 0.8396674584323041, 0.8605504587155963, 0.933422103861518, 0.7358490566037735, 0.8096385542168675, 0.8148148148148148, 0.9340425531914893, 0.9194053208137715]) 

# #Cross_Subject
accuracy_inward = [0.7159468438538206,0.7863105175292153,0.7018544935805991,0.7614213197969543,0.7940594059405941,0.8333333333333334,0.7464167585446527,0.8012976480129764,0.7410358565737052,0.9221183800623053,0.8924544666088465] 
accuracy_outward = [0.7192691029900332,0.6460767946577629,0.724679029957204,0.7550761421319797,0.7762376237623763,0.865546218487395,0.6923925027563396,0.7858880778588808,0.7264276228419655,0.8372274143302181,0.8933217692974849] 
accuracy_inward_outward= [ 0.7641196013289037,0.7729549248747913,0.7945791726105563,0.7918781725888325,0.7801980198019802,0.8823529411764706,0.7585446527012127,0.8175182481751825,0.8061088977423638,0.9158878504672897,0.8872506504770165] 
fc1_inward_outward = [ 0.7990033222591362,0.8063439065108514,0.8174037089871612,0.815989847715736,0.80990099009901,0.9103641456582633,0.7618522601984564,0.7980535279805353,0.7397078353253652,0.8901869158878505,0.8907198612315698] 

# 设置条形图参数
x = np.arange(len(labels))  # 标签位置
width = 0.2  # 每个条形的宽度

# 创建图表
fig, ax = plt.subplots(figsize=(16, 8))

# 绘制四组条形图
rects1 = ax.bar(x - 1.5*width, accuracy_inward, width, label='ARN-LSTM_inward', color='indianred', edgecolor='black', linewidth=0.5)
rects2 = ax.bar(x - 0.5*width, accuracy_outward, width, label='ARN-LSTM_outward', color='mediumseagreen', edgecolor='black', linewidth=0.5)
rects3 = ax.bar(x + 0.5*width, accuracy_inward_outward, width, label='ARN-LSTM_inward_outward', color='cornflowerblue', edgecolor='black', linewidth=0.5)
rects4 = ax.bar(x + 1.5*width, fc1_inward_outward, width, label='ARN-LSTM_fc1_inward_outward', color='orchid', edgecolor='black', linewidth=0.5)

# 添加标签和标题
ax.set_xlabel("Action Classes", fontsize=14, fontweight='bold')
ax.set_ylabel("Accuracy (%)", fontsize=14, fontweight='bold')
ax.set_title("NTU RGB+D 60 Dataset (Cross_Subject) action recognition performance comparison", fontsize=16, pad=20)

# 设置 X 轴
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=11, color='black')

# 设置 Y 轴范围（建议 0-105 以留出顶部空间）
ax.set_ylim(0, 1.1)

# 添加图例
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.0), ncol=4, frameon=True, fontsize=11)

# 添加网格线（仅 Y 轴，增加可读性）
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True) # 确保网格线在条形图下方

# 自动调整布局，防止标签被裁剪
plt.tight_layout()

# 保存并显示
# 注意：请确保 /demo/ARN-LSTM/... 路径在你的环境下存在，否则会报错
plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/CHAPTER4/ARN-LSTM_ntu60_cs_acc_bar.png', dpi=300, bbox_inches='tight')
plt.show()