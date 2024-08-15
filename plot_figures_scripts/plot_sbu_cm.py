import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, Normalize
# SBU dataset 
classes = ['Approaching','Departing','Kicking','Punching','Pushing','Hugging','ShakingHands','Exchanging'
]

conf_arr = [[7, 0 ,0 ,1 ,0, 0 ,0 ,0],
[0, 8 ,0, 0, 0, 0, 0 ,0],
[0, 0, 7,0, 0 ,0 ,0 ,1],
[0, 0, 0, 8, 0, 1, 0, 0],
[0, 0,0,0 ,2 ,0, 1, 0],
[0, 0, 0, 0, 0, 4, 0, 0],
[0, 0, 0, 0, 0, 0, 7, 0],
[3, 0, 0, 0, 1, 0, 1, 3]]


# 自定义渐变颜色
colors = ['#ffffff', '#ffcccc', '#ff6666', '#ff0000', '#990000']
custom_cmap = LinearSegmentedColormap.from_list('custom_cmap', colors)

# 归一化对象，定义最小值和最大值
norm = Normalize(vmin=0, vmax=np.max(conf_arr))

norm_conf = []
for i in conf_arr:
    a = 0
    tmp_arr = []
    a = sum(i, 0)
    for j in i:
        tmp_arr.append(float(j)/float(a))
    norm_conf.append(tmp_arr)

fig = plt.figure()
plt.clf()
ax = fig.add_subplot(111)
ax.set_aspect(1)
res = ax.imshow(np.array(conf_arr), cmap=custom_cmap, norm=norm, interpolation='nearest')

# 获取矩阵的宽度和高度
width, height = np.array(conf_arr).shape

# 使用 range 替换 xrange
for x in range(width):
    for y in range(height):
        ax.annotate(str(conf_arr[x][y]), xy=(y, x),
                    horizontalalignment='center',
                    verticalalignment='center',
                    color='black')

cb = fig.colorbar(res)

# 调整 alphabet 使其不会超出索引范围
alphabet = classes[:width]
plt.xticks(range(width), alphabet, rotation=45, ha="right")
plt.yticks(range(height), alphabet)

# 自动调整子图布局
plt.tight_layout()

plt.savefig('sbu_cm.png', format='png')
plt.show()

