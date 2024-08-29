
#UT-Interaction 数据集包含 6 类人机交互的连续执行视频：握手、指向、拥抱、推、踢和拳。提供了这些交互的真实标签，包括时间间隔和边界框。
#总共有 20 个长度在 1 分钟左右的视频序列。每个视频每次交互至少包含一次执行，因此平均每个视频执行 8 次人类活动。视频中出现了几名具有
#超过 15 种不同服装条件的参与者。视频采用720*480分辨率，30fps拍摄，视频中人物身高约200像素。

import json
import os
import matplotlib.pyplot as plt

# 定义骨骼的连接关系（根据实际数据集的关键点顺序进行修改）
connections = [
    (0, 1),  # 鼻子到脖子
    (1, 2), (2, 3), (3, 4),  # 右肩 -> 右肘 -> 右手腕
    (1, 5), (5, 6), (6, 7),  # 左肩 -> 左肘 -> 左手腕
    (1, 8), (8, 9), (9, 10),  # 脖子 -> 右髋 -> 右膝 -> 右脚踝
    (1, 11), (11, 12), (12, 13),  # 脖子 -> 左髋 -> 左膝 -> 左脚踝
    (0, 14), (0, 15),  # 鼻子 -> 右眼 -> 左眼
    (14, 16), (15, 17),  # 右眼 -> 右耳, 左眼 -> 左耳
    (1, 18), (18, 19),  # 脖子 -> 胸部中心
    (10, 20), (13, 21)  # 右脚踝 -> 右脚，左脚踝 -> 左脚
]

# 可视化单帧骨骼数据并保存图片
def plot_and_save_skeleton(keypoints, connections, save_path):
    fig, ax = plt.subplots()
    
    for connection in connections:
        start_idx, end_idx = connection
        start_point = keypoints[start_idx * 3:start_idx * 3 + 2]
        end_point = keypoints[end_idx * 3:end_idx * 3 + 2]

        ax.plot([start_point[0], end_point[0]], [start_point[1], end_point[1]], 'r--')

    ax.scatter(keypoints[::3], keypoints[1::3], color='b')
    ax.set_title("2D Skeleton Visualization")
    plt.gca().invert_yaxis()

    # 创建目录（如果不存在）
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    # 保存图片
    plt.savefig(save_path)
    plt.close(fig)  # 关闭图像以节省内存

# 处理单个文件并保存骨骼数据的可视化图像
def visualize_frame(file_path, output_dir,base_dir):
    with open(file_path, 'r') as f:
        data = json.load(f)

    if len(data['people']) > 0:
        keypoints = data['people'][0]['pose_keypoints_2d']

        # 生成保存路径
        save_path = os.path.join(output_dir, os.path.relpath(file_path, base_dir))
        save_path = save_path.replace('_keypoints.json', '.png')
        
        plot_and_save_skeleton(keypoints, connections, save_path)
    else:
        print(f"No skeleton data found in {file_path}")

# 遍历指定文件夹并处理所有帧
def visualize_directory(root_dir, output_dir):
    base_dir = root_dir
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('_keypoints.json'):
                file_path = os.path.join(subdir, file)
                print(f"Visualizing {file_path}")
                visualize_frame(file_path, output_dir,base_dir)



def main():
    input_directory = r'/usr/local/inter-rel-net-hockey/data02/ut-interaction/'  # 替换为 UT 数据集的根目录路径
    output_directory = r'/demo/ARN-LSTM/visualize/results/ut/'  # 替换为你希望保存图片的文件夹路径


    # 运行脚本处理整个数据集
    visualize_directory(input_directory, output_directory)



if __name__=='__main__':
    main()