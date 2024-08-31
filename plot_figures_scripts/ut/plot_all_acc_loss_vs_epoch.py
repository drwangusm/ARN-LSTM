import pandas as pd
import matplotlib.pyplot as plt
import os
#绘制所有log中准确率和loss变化曲线

# 假设你有一个包含所有fold日志文件的目录结构
base_dir = r'/demo/ARN-LSTM/runs/UT-1/ARN_inward'
num_folds = 10
num_reruns = 5

plt.figure(figsize=(30, 16))

# 绘制Accuracy曲线
plt.subplot(1, 2, 1)
for fold in range(num_folds):
    for rerun in range(num_reruns):
        log_file = os.path.join(base_dir, f'fold_{fold}', f'rerun_{rerun}', 'training.log')
        if os.path.exists(log_file):
            data = pd.read_csv(log_file)
            plt.plot(data['epoch'], data['accuracy'], label=f'Fold {fold} Rerun {rerun}')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Accuracy vs Epoch')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')

# 绘制Loss曲线
plt.subplot(1, 2, 2)
for fold in range(num_folds):
    for rerun in range(num_reruns):
        log_file = os.path.join(base_dir, f'fold_{fold}', f'rerun_{rerun}', 'training.log')
        if os.path.exists(log_file):
            data = pd.read_csv(log_file)
            plt.plot(data['epoch'], data['loss'], label=f'Fold {fold} Rerun {rerun}')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss vs Epoch')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')

plt.tight_layout()

plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/UT-1/TEST.png',dpi=300,bbox_inches='tight') #保存并命名图片
plt.show()
