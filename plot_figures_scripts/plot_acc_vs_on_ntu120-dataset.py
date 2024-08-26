import matplotlib.pyplot as plt
import numpy as np

# 模拟数据
labels = [
    'Punch/slap','Kicking','Pushing','Pat on the back','Point finger','Hugging','Giving object',
           'Touch pocket','Shake hands','Walk towards','Walk apart','HitWithObject','WieldKnife','KnockOver',
            'GrabStuff','ShootWithGun','StepOnFoot','High-five','CheersAndDrink',
            'CarryObject','TakePhoto','Follow','Whisper','ExchangeThings','SupportSomebody','RockPaperScissors'
]
accuracy_RN_joint = [0.875,1.0,0.875,0.8888888888888888,0.6666666666666666,1.0,1.0,0.25]
accuracy_RN_temp = [0.625,0.875,1.0,0.8888888888888888,1.0,1.0,1.0,0.375]
accuracy_RN_joint_temp= [1.0,1.0,0.875,0.8888888888888888,0.6666666666666666,1.0,1.0,0.625]
# 设置图表大小
plt.figure(figsize=(14, 7))

# 绘制折线图
plt.plot(accuracy_RN_joint, 'rx', label='RN_joint', linestyle='--')
plt.plot(accuracy_RN_temp, 'g^', label='RN_temp', linestyle='--')
plt.plot(accuracy_RN_joint_temp, 'bo', label='RN_joint_temp', linestyle='--')

# 添加图例
plt.legend()

# 添加标签和标题
plt.xlabel("Action Classes")
plt.ylabel("Accuracy (%)")
plt.title("NTU RGB+D 120 dataset action recognition performance comparison")

# 设置x轴刻度并将标签颜色设置为黑色，字体大小设置为18
plt.xticks(ticks=np.arange(len(labels)), labels=labels, rotation=60, ha="right", fontsize=12, color='black')

# 显示网格
plt.grid(True, linestyle='--', alpha=0.6)

# 显示图表
plt.tight_layout()
plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/NTU-V2/ARN-LSTM_acc_vs.png',dpi=300,bbox_inches='tight')
plt.show()
