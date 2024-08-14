import tensorflow as tf
from tensorflow.python.summary.summary_iterator import summary_iterator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 步骤 1：解析 .tfevents 文件
event_file = '/demo/ARN-LSTM/runs/models/UT-1/ARN-LSTM_inward+outward/fold_0/rerun_0/class_accuracy_logs/events.out.tfevents.1723596127.gzgs-Default-string.2162162.0.v2'

def parse_tfevents(file):
    data = {}
    for e in summary_iterator(file):
        for v in e.summary.value:
            if v.tag not in data:
                data[v.tag] = []
            data[v.tag].append((e.step, v.simple_value))
    return data

data = parse_tfevents(event_file)

print("data",data)

# 步骤 2：生成消融矩阵
# 根据解析后的数据生成消融矩阵（这里假设你从 data 中提取了多个模型的准确率）
model_accuracies = {
    'model_1': [0.95, 0.94, 0.96],
    'model_2': [0.92, 0.91, 0.93],
    'model_3': [0.88, 0.89, 0.90],
}

ablation_matrix = pd.DataFrame(model_accuracies)

# 步骤 3：绘制消融矩阵
plt.figure(figsize=(10, 8))
sns.heatmap(ablation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Ablation Matrix')
plt.xlabel('Model Configurations')
plt.ylabel('Experiments')
plt.savefig("./cm.png",dpi=300,bbox_inches='tight')
plt.show()
