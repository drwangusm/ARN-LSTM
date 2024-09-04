import os
import pandas as pd

#计算所有fold中每个return（总共25个）的分类识别准确率的平均值


# 定义数据的根目录
root_dir = '/demo/ARN-LSTM/runs/SBU/ARN-LSTM-fc1_inward+outward'

# 存储所有fold的分类识别准确率
all_class_accuracies = []

# 遍历fold_0到fold_4
for fold in range(5):
    fold_dir = os.path.join(root_dir, f'fold_{fold}')
    
    # 遍历return_0到return_4
    for rerun in range(5):
        rerun_dir = os.path.join(fold_dir, f'rerun_{rerun}')
        class_accuracies_file = os.path.join(rerun_dir, 'class_accuracies.csv')
        
        # 读取class_accuracies.csv文件
        if os.path.exists(class_accuracies_file):
            with open(class_accuracies_file, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if "Class Accuracies:" in line:
                        # 提取并解析Class Accuracies部分
                        accuracies = line.split(":")[1].strip().split(',')
                        accuracies = [float(acc) for acc in accuracies]
                        all_class_accuracies.append(accuracies)
        else:
            print(f"File {class_accuracies_file} does not exist.")

# 将所有准确率数据合并为DataFrame
all_class_accuracies_df = pd.DataFrame(all_class_accuracies)

# 计算每个分类的平均值
mean_class_accuracies = all_class_accuracies_df.mean()

# 输出平均值
print("ARN-LSTM,Average Class Accuracies across all folds and reruns:")
print(mean_class_accuracies)
