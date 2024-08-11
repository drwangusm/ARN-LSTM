import pandas as pd
import matplotlib.pyplot as plt
import io

## plot Accuracy curve with epoch 

# 将数据转换为pandas DataFrame
data_path = r"../runs/models/NTU-V2/ARN-LSTM_outward/fold_cross_setup/rerun_0/training.log"  #训练日志数据

with open(data_path, 'r') as file:
    contend = file.read()

    df = pd.read_csv(io.StringIO(contend))
    # print("df:",df)
    # 绘制准确率随epoch变化的曲线图
    plt.figure(figsize=(12, 6))
    plt.plot(df['epoch'], df['accuracy'], label='Training Accuracy')
    plt.plot(df['epoch'], df['val_accuracy'], label='Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.title('Accuracy over Epochs')
    plt.legend()
    plt.grid(True)
    plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/ARN-LSTM_outward_accuracy.png',dpi=300,bbox_inches='tight')
    plt.show()

    # 绘制损失率随epoch变化的曲线图
    plt.figure(figsize=(12, 6))
    plt.plot(df['epoch'], df['loss'], label='Training Loss')
    plt.plot(df['epoch'], df['val_loss'], label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Loss over Epochs')
    plt.legend()
    plt.grid(True)
    plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/ARN-LSTM_outward_loss.png',dpi=300,bbox_inches='tight')
    plt.show()