import matplotlib.pyplot as plt
import numpy as np

# 模拟数据
labels = [
    'Approaching', 'Departing', 'Kicking', 'Punching', 
    'Pushing', 'Hugging', 'ShakingHands', 'Exchanging'
]

# --- Chapter 5 数据定义 ---
acc_ARN_joint = [0.978667, 0.934556, 0.775000, 0.815444, 0.706667, 0.950000, 0.795429, 0.630159]
acc_ARN_temp = [0.975000, 0.957000, 0.940000, 0.886556, 0.778667, 0.940000, 0.821857, 0.751111]
acc_ARN_joint_temp = [0.995556, 0.972000, 0.925000, 0.904667, 0.832000, 0.930000, 0.878714, 0.748254]
ARN_fc1_joint_temp = [1.000000, 0.968000, 0.950000, 0.894111, 0.866667, 0.964000, 0.869143, 0.761984]
ARN_inward_no_motion = [0.965000, 0.955556, 0.830000, 0.812222, 0.594000, 0.960000, 0.806000, 0.567302]
ARN_inward = [0.968000, 0.987556, 0.865000, 0.895556, 0.736667, 0.968000, 0.798857, 0.715556]
ARN_outward_no_motion = [1.000000, 0.976000, 0.940000, 0.905667, 0.778667, 0.934000, 0.849714, 0.762063]
ARN_outward = [0.990000, 0.988000, 0.935000, 0.882333, 0.742667, 0.936000, 0.805429, 0.761349]
ARN_inward_outward_no_motin = [0.995000, 0.968000, 0.935000, 0.914444, 0.829333, 0.960000, 0.857857, 0.778095]
ARN_inward_outward = [0.975000, 0.960000, 0.940000, 0.913889, 0.842667, 0.984000, 0.840286, 0.745397]
ARN_fc1_inward_outward = [0.980000, 0.988000, 0.925000, 0.920556, 0.818667, 0.982000, 0.839000, 0.730397]

# 组合所有数据以便迭代绘图
data_list = [
    (acc_ARN_joint, 'ARN_joint', '#e6194B'),
    (acc_ARN_temp, 'ARN_temp', '#3cb44b'),
    (acc_ARN_joint_temp, 'ARN_joint_temp', '#ffe119'),
    (ARN_fc1_joint_temp, 'ARN-fc1_joint_temp', '#4363d8'),
    (ARN_inward_no_motion, 'ARN_inward_no_motion', '#f58231'),
    (ARN_inward, 'ARN_inward', '#911eb4'),
    (ARN_outward_no_motion, 'ARN_outward_no_motion', '#42d4f4'),
    (ARN_outward, 'ARN_outward', '#f032e6'),
    (ARN_inward_outward_no_motin, 'ARN_inward_outward_no_motin', '#bfef45'),
    (ARN_inward_outward, 'ARN_inward_outward', '#fabed4'),
    (ARN_fc1_inward_outward, 'ARN_fc1_inward_outward', '#000080')
]

# 设置图表大小
plt.figure(figsize=(18, 9))

# 计算条形位置
x = np.arange(len(labels))
total_width = 0.85  # 总宽度占刻度的比例
n_groups = len(data_list)
bar_width = total_width / n_groups

# 绘制条形
for i, (vals, name, color) in enumerate(data_list):
    # 计算每组条形的偏移量
    offset = (i - (n_groups - 1) / 2) * bar_width
    plt.bar(x + offset, vals, width=bar_width, label=name, color=color, edgecolor='black', linewidth=0.5)

# 添加标签和标题
plt.xlabel("Action Classes", fontsize=14, fontweight='bold')
plt.ylabel("Accuracy", fontsize=14, fontweight='bold')
plt.title("SBU Kinect Interaction Dataset Action Recognition Accuracy Comparison (Bar Chart)", fontsize=16, pad=20)

# 设置刻度
plt.xticks(ticks=x, labels=labels, rotation=30, ha="right", fontsize=12)
plt.yticks(np.arange(0, 1.1, 0.1))
plt.ylim(0, 1.25)  # 留出顶部空间放图例

# 显示网格（仅Y轴）
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 添加图例：分三列显示，防止横向太长
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 0.98), ncol=3, fontsize=10, frameon=True)

# 显示图表
plt.tight_layout()

# 保存路径请根据需要修改
plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/CHAPTER4/ARN_SBU-all_acc_bar.png', dpi=300, bbox_inches='tight')

plt.show()