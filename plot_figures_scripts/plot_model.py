import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Concatenate, Dense
from tensorflow.keras.utils import plot_model

# 定义输入层
person1_inputs = [Input(shape=(98,), name=f'person1_object{i}') for i in range(15)]
person2_inputs = [Input(shape=(98,), name=f'person2_object{i}') for i in range(15)]

# 将所有的 person1 和 person2 输入连接到一个中间层
concatenated = Concatenate()([*person1_inputs, *person2_inputs])

# 定义功能层
g_theta_inter = Dense(500, activation='relu', name='g_theta_inter')(concatenated)

# 定义输出层
output = Dense(1, activation='sigmoid', name='output')(g_theta_inter)

# 创建模型
model = Model(inputs=[*person1_inputs, *person2_inputs], outputs=output)

# 可视化模型
plot_model(model, to_file='./plot_figures_results/rel_net_model.png', show_shapes=True, show_layer_names=True)

# 打印模型摘要
model.summary()
