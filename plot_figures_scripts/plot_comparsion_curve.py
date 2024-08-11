import pandas as pd
import matplotlib.pyplot as plt

#绘制对比曲线图
# Read the log files into pandas dataframes
log_file_path1 = "/demo/ARN-LSTM/runs/models/UT-1/ARN_no_rel_att_before_s1/fold_9/rerun_0/training.log"
log_file_path2 = "/demo/ARN-LSTM/runs/models/UT-1/ARN_no_rel_att_after_s1/fold_9/rerun_0/training.log"

data1 = pd.read_csv(log_file_path1)
data2 = pd.read_csv(log_file_path2)

# Extract necessary columns
epochs1 = data1['epoch']
accuracy1 = data1['accuracy']
loss1 = data1['loss']

epochs2 = data2['epoch']
accuracy2 = data2['accuracy']
loss2 = data2['loss']

# Plotting accuracy comparison
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(epochs1, accuracy1, label='ARN_no_rel_att_before_s1 Accuracy', marker='o')
plt.plot(epochs2, accuracy2, label='ARN_no_rel_att_after_s1 Accuracy', marker='o')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Accuracy vs. Epochs')
plt.legend()
plt.grid(True)

# Plotting loss comparison
plt.subplot(1, 2, 2)
plt.plot(epochs1, loss1, label='ARN_no_rel_att_before_s1 Loss', marker='o')
plt.plot(epochs2, loss2, label='ARN_no_rel_att_after_s1 Loss', marker='o')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss vs. Epochs')
plt.legend()
plt.grid(True)

# Show the plots
plt.tight_layout()
plt.savefig(r"/demo/ARN-LSTM/plot_figures_results/ARN_no_rel_att_before_after.png",dpi=300,bbox_inches='tight')
plt.show()
