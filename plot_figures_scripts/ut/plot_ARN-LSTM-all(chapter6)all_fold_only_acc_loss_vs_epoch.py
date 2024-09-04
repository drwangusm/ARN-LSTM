# #同时绘制多张图到一张图上
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import os

# # 定义三个方法的base_dir路径
# base_dirs = [
#     r'/demo/ARN-LSTM/runs/UT-1/RN_joint',
#     r'/demo/ARN-LSTM/runs/UT-1/RN_temp',
#     r'/demo/ARN-LSTM/runs/UT-1/RN_joint+temp'
# ]

# method_names = ['Method 1', 'Method 2', 'Method 3']
# num_folds = 10
# num_reruns = 5

# # 创建空字典用于存储平均值
# avg_accuracy = {method: {} for method in method_names}
# avg_loss = {method: {} for method in method_names}

# # 读取和处理数据
# for method, base_dir in zip(method_names, base_dirs):
#     for fold in range(num_folds):
#         accuracies = []
#         losses = []
#         min_length = None  # 初始化最小长度
        
#         for rerun in range(num_reruns):
#             log_file = os.path.join(base_dir, f'fold_{fold}', f'rerun_{rerun}', 'training.log')
#             if os.path.exists(log_file):
#                 data = pd.read_csv(log_file)
#                 accuracy_values = data['accuracy'].values
#                 loss_values = data['loss'].values
                
#                 if min_length is None:
#                     min_length = len(accuracy_values)
#                 else:
#                     min_length = min(min_length, len(accuracy_values))
                
#                 accuracies.append(accuracy_values)
#                 losses.append(loss_values)
        
#         # 将所有值裁剪到相同的最小长度
#         accuracies = [acc[:min_length] for acc in accuracies]
#         losses = [loss[:min_length] for loss in losses]
        
#         # 计算每个fold的平均accuracy和loss
#         avg_accuracy[method][fold] = np.mean(accuracies, axis=0)
#         avg_loss[method][fold] = np.mean(losses, axis=0)

# # 绘制曲线
# plt.figure(figsize=(18, 12))

# # 绘制平均Accuracy曲线
# plt.subplot(2, 1, 1)
# for method in method_names:
#     for fold in range(num_folds):
#         plt.plot(avg_accuracy[method][fold], label=f'{method} - Fold {fold}')
# plt.xlabel('Epoch')
# plt.ylabel('Average Accuracy')
# plt.title('Average Accuracy vs Epoch for Three Methods')
# plt.legend()

# # 绘制平均Loss曲线
# plt.subplot(2, 1, 2)
# for method in method_names:
#     for fold in range(num_folds):
#         plt.plot(avg_loss[method][fold], label=f'{method} - Fold {fold}')
# plt.xlabel('Epoch')
# plt.ylabel('Average Loss')
# plt.title('Average Loss vs Epoch for Three Methods')
# plt.legend()

# plt.tight_layout()
# plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/UT-1/RN-all-methods_Comparison.png', dpi=300, bbox_inches='tight')  # 保存并命名图片
# plt.show()

#########################################################################################

# # # 绘制一张图的逻辑#
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import os

# # 定义文件路径
# base_dir = r'/demo/ARN-LSTM/runs/UT-1/RN_joint+temp'
# num_folds = 10
# num_reruns = 5

# # 创建空字典用于存储平均值
# avg_accuracy = {}
# avg_loss = {}

# for fold in range(num_folds):
#     accuracies = []
#     losses = []
#     min_length = None  # 初始化最小长度
    
#     for rerun in range(num_reruns):
#         log_file = os.path.join(base_dir, f'fold_{fold}', f'rerun_{rerun}', 'training.log')
#         if os.path.exists(log_file):
#             data = pd.read_csv(log_file)
#             accuracy_values = data['accuracy'].values
#             loss_values = data['loss'].values
            
#             if min_length is None:
#                 min_length = len(accuracy_values)
#             else:
#                 min_length = min(min_length, len(accuracy_values))
            
#             accuracies.append(accuracy_values)
#             losses.append(loss_values)

#     #需要确保所有 rerun 的 accuracy 和 loss 数据的长度一致。 方法：1.找到最小的 epoch 长度并进行裁剪：将每个 rerun 的 accuracy 和 loss 数据裁剪到相同的长度（例如最小的长度），以确保它们的形状一致。2.使用 pandas DataFrame 进行自动对齐：将每个 rerun 的数据存储在 pandas DataFrame 中，它会自动根据 epoch 对齐数据，并填充缺失值。然后再计算平均值。
#     # 将所有值裁剪到相同的最小长度
#     accuracies = [acc[:min_length] for acc in accuracies]
#     losses = [loss[:min_length] for loss in losses]
    
#     # 计算每个fold的平均accuracy和loss
#     avg_accuracy[fold] = np.mean(accuracies, axis=0)
#     avg_loss[fold] = np.mean(losses, axis=0)

# # 绘制曲线
# plt.figure(figsize=(15, 8))

# # 绘制平均Accuracy曲线
# plt.subplot(1, 2, 1)
# for fold in range(num_folds):
#     plt.plot(avg_accuracy[fold], label=f'Fold {fold}')
# plt.xlabel('Epoch')
# plt.ylabel('Average Accuracy (%)')
# plt.title('Average Accuracy vs Epoch')
# plt.legend()

# # 绘制平均Loss曲线
# plt.subplot(1, 2, 2)
# for fold in range(num_folds):
#     plt.plot(avg_loss[fold], label=f'Fold {fold}')
# plt.xlabel('Epoch')
# plt.ylabel('Average Loss')
# plt.title('Average Loss vs Epoch')
# plt.legend()

# plt.tight_layout()
# plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/UT-1/RN_joint+temp(10fold_acc_loss_vs_in_set_1).png', dpi=300, bbox_inches='tight')  # 保存并命名图片
# plt.show()

##############################################################################################
# # 3张图片合并逻辑

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 定义每个方法生成的图像路径(set_1)
image_paths = [
    r'/demo/ARN-LSTM/plot_figures_results/UT-1/RN_joint(10fold_acc_loss_vs_in_set_1).png',
    r'/demo/ARN-LSTM/plot_figures_results/UT-1/RN_temp(10fold_acc_loss_vs_in_set_1).png',
    r'/demo/ARN-LSTM/plot_figures_results/UT-1/RN_joint+temp(10fold_acc_loss_vs_in_set_1).png'
]

# # 定义每个方法生成的图像路径(set_2)
# image_paths = [
#     r'/demo/ARN-LSTM/plot_figures_results/UT-2/RN_joint(10fold_acc_loss_vs_in_set_2).png',
#     r'/demo/ARN-LSTM/plot_figures_results/UT-2/RN_temp(10fold_acc_loss_vs_in_set_2).png',
#     r'/demo/ARN-LSTM/plot_figures_results/UT-2/RN_joint+temp(10fold_acc_loss_vs_in_set_2).png'
# ]

# 创建大图并设置子图
fig, axs = plt.subplots(3, 1, figsize=(12, 20))

# 读取并显示每个图像，同时在底部添加标签
labels = ['(a) RN_joint 10 folds mean accuracy and loss curve', '(b) RN_temp 10 folds mean accuracy and loss curve', '(c) RN_joint+temp 10 folds mean accuracy and loss curve']

for i, image_path in enumerate(image_paths):
    img = mpimg.imread(image_path)
    axs[i].imshow(img)
    axs[i].axis('off')  # 隐藏坐标轴
    axs[i].text(0.5, -0.02, labels[i], transform=axs[i].transAxes, 
                fontsize=14, va='center', ha='center')

# 调整布局以适应标签的显示
plt.tight_layout()

# 保存拼接后的图像
plt.savefig(r'/demo/ARN-LSTM/plot_figures_results/UT-1/RN-all-Combined_Results_Labeled.png', dpi=300, bbox_inches='tight')
plt.show()
