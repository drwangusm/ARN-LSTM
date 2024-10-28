import pandas as pd
import matplotlib.pyplot as plt
import io

# 定义文件路径
# #ntu120

data_paths = {
    "ARN_joint+motion (Cross subject)": r"/demo/ARN-LSTM/runs/NTU-V2/ARN_joint/fold_cross_subject/rerun_0/training.log",
    "ARN_joint+motion (Cross view)": r"/demo/ARN-LSTM/runs/NTU-V2/ARN_joint/fold_cross_setup/rerun_0/training.log",
    "ARN_temporal+motion (Cross subject)": r"/demo/ARN-LSTM/runs/NTU-V2/ARN_temp/fold_cross_subject/rerun_0/training.log",
    "ARN_temporal+motion (Cross view)": r"/demo/ARN-LSTM/runs/NTU-V2/ARN_temp/fold_cross_setup/rerun_0/training.log",
    "ARN_joint+temporal+motion (Cross subject)":r"/demo/ARN-LSTM/runs/NTU-V2/ARN-LSTM_inward+outward/fold_cross_subject/rerun_0/training.log",
    "ARN_joint+temporal+motion (Cross view)":r"/demo/ARN-LSTM/runs/NTU-V2/ARN-LSTM_inward+outward/fold_cross_setup/rerun_0/training.log",
}

# 创建6个子图
fig, axs = plt.subplots(3, 2, figsize=(14, 20))

# 标签列表
labels = ['(a)', '(b)', '(c)', '(d)','(e)','(f)']


# # ## 绘制准确率变化曲线
# # # # 遍历文件路径和子图
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
#     ax.text(0.5, -0.15, label, transform=ax.transAxes, fontsize=14, fontweight='bold',va='center', ha='center')

# # 调整子图布局
# plt.tight_layout()
# plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/final/ARN_all_accuracy.png', dpi=300, bbox_inches='tight')
# plt.show()


# 绘制损失变化曲线
# 遍历文件路径和子图
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
plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/final/ARN-LSTM_all_loss.png', dpi=300, bbox_inches='tight')
plt.show()
