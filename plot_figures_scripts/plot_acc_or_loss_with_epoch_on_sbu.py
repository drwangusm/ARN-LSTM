import pandas as pd
import matplotlib.pyplot as plt
import io

# 定义文件路径
data_paths = {
    "ARN-LSTM_inward": r"/demo/ARN-LSTM/runs/SBU/ARN-LSTM_inward/fold_0/rerun_0/training.log",
    "ARN-LSTM_outward": r"/demo/ARN-LSTM/runs/SBU/ARN-LSTM_outward/fold_0/rerun_0/training.log",
    "ARN-LSTM_inward+outward":r"/demo/ARN-LSTM/runs/SBU/ARN-LSTM_inward+outward/fold_0/rerun_0/training.log",
    "ARN-LSTM-fc1_inward+outward":r"/demo/ARN-LSTM/runs/SBU/ARN-LSTM-fc1_inward+outward/fold_0/rerun_0/training.log",
}

# 创建4个子图
fig, axs = plt.subplots(2, 2, figsize=(8, 13))

# 标签列表
labels = ['(a)', '(b)', '(c)', '(d)']


# #绘制准确率变化曲线
# # 遍历文件路径和子图
# for ax, (title, path),label in zip(axs.ravel(), data_paths.items(),labels):#通过 zip(axs.ravel(), data_paths.items()) 将每个子图和数据集进行配对，并在每个子图上绘制对应的曲线图。
#     with open(path, 'r') as file:
#         contend = file.read()

#     # 读取数据
#     df = pd.read_csv(io.StringIO(contend))
    
#     # 绘制准确率曲线
#     ax.plot(df['epoch'], df['accuracy'], label='Training Accuracy')
#     ax.plot(df['epoch'], df['val_accuracy'], label='Validation Accuracy')
#     ax.set_xlabel('Epoch')
#     ax.set_ylabel('Accuracy')
#     ax.set_title(title)
#     ax.legend()
#     ax.grid(True)

#      # 在子图底部添加标签
#     ax.text(0.5, -0.1, label, transform=ax.transAxes, fontsize=14, fontweight='bold',va='center', ha='center')

# # 调整子图布局
# plt.tight_layout()
# plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/SBU/ARN-LSTM_all_accuracy.png', dpi=300, bbox_inches='tight')
# plt.show()


# #绘制损失变化曲线
# # 遍历文件路径和子图
for ax, (title, path),label in zip(axs.ravel(), data_paths.items(),labels):#通过 zip(axs.ravel(), data_paths.items()) 将每个子图和数据集进行配对，并在每个子图上绘制对应的曲线图。
    with open(path, 'r') as file:
        contend = file.read()

    # 读取数据
    df = pd.read_csv(io.StringIO(contend))
    
    # 绘制准确率曲线
    ax.plot(df['epoch'], df['loss'], label='Training Loss')
    ax.plot(df['epoch'], df['val_loss'], label='Validation Loss')
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Loss')
    ax.set_title(title)
    ax.legend()
    ax.grid(True)

     # 在子图底部添加标签
    ax.text(0.5, -0.15, label, transform=ax.transAxes, fontsize=14, fontweight='bold',va='center', ha='center')

# 调整子图布局
plt.tight_layout()
plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/SBU/ARN-LSTM_all_loss.png', dpi=300, bbox_inches='tight')
plt.show()
