import numpy as np
import matplotlib.pyplot as plt

# 输入数据示例
inputs = np.random.rand(2, 3, 4)  # 2 个样本，每个样本有 3 个对象，每个对象有 4 个特征

# 注意力权重示例
attention_weights = np.random.rand(2, 3, 1)  # 2 个样本，每个样本有 3 个对象，每个对象有 1 个权重

# 加权求和示例
weighted_sum = np.sum(inputs * attention_weights, axis=1)

# 绘图
fig, ax = plt.subplots(2, 1, figsize=(10, 10))

# 输入数据图
ax[0].imshow(inputs[0], cmap='Blues', aspect='auto')
ax[0].set_title('Input Objects (Sample 1)')
ax[0].set_xlabel('Features')
ax[0].set_ylabel('Objects')

# 注意力权重图
ax[1].imshow(attention_weights[0], cmap='Greens', aspect='auto')
ax[1].set_title('Attention Weights (Sample 1)')
ax[1].set_xlabel('Attention')
ax[1].set_ylabel('Objects')

plt.tight_layout()
plt.savefig('IRAttention.png', dpi=600, bbox_inches='tight')
plt.show()
