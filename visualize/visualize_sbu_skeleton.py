#download the dataset url
#The SBU Kinect Interaction dataset is a Kinect captured human activity recognition dataset depicting two person interaction. It contains 282 skeleton sequences and 6822 frames of 8 classes. There are 15 joints for each skeleton.

# 下载SBU骨骼数据集方法
# Set01= "http://vision.cs.stonybrook.edu/~kiwon/Datasets/SBU_Kinect_Interactions/s01s02.zip"
# Set02= "http://vision.cs.stonybrook.edu/~kiwon/Datasets/SBU_Kinect_Interactions/s01s03.zip"
# Set03= "http://vision.cs.stonybrook.edu/~kiwon/Datasets/SBU_Kinect_Interactions/s01s07.zip"
# Set04= "http://vision.cs.stonybrook.edu/~kiwon/Datasets/SBU_Kinect_Interactions/s02s01.zip"
# Set05= "http://vision.cs.stonybrook.edu/~kiwon/Datasets/SBU_Kinect_Interactions/s02s03.zip"
# Set06= "http://vision.cs.stonybrook.edu/~kiwon/Datasets/SBU_Kinect_Interactions/s02s06.zip"
# Set07= "http://vision.cs.stonybrook.edu/~kiwon/Datasets/SBU_Kinect_Interactions/s02s07.zip"
# Set08= "http://vision.cs.stonybrook.edu/~kiwon/Datasets/SBU_Kinect_Interactions/s03s02.zip"
# Set09= "http://vision.cs.stonybrook.edu/~kiwon/Datasets/SBU_Kinect_Interactions/s03s04.zip"
# Set10= "http://vision.cs.stonybrook.edu/~kiwon/Datasets/SBU_Kinect_Interactions/s03s05.zip"
# Set11= "http://vision.cs.stonybrook.edu/~kiwon/Datasets/SBU_Kinect_Interactions/s03s06.zip"
# Set12= "http://vision.cs.stonybrook.edu/~kiwon/Datasets/SBU_Kinect_Interactions/s04s02.zip"
# Set13= "http://vision.cs.stonybrook.edu/~kiwon/Datasets/SBU_Kinect_Interactions/s04s03.zip"
# Set14= "http://vision.cs.stonybrook.edu/~kiwon/Datasets/SBU_Kinect_Interactions/s04s06.zip"
# Set15= "http://vision.cs.stonybrook.edu/~kiwon/Datasets/SBU_Kinect_Interactions/s05s02.zip"
# Set16= "http://vision.cs.stonybrook.edu/~kiwon/Datasets/SBU_Kinect_Interactions/s05s03.zip"
# Set17= "http://vision.cs.stonybrook.edu/~kiwon/Datasets/SBU_Kinect_Interactions/s06s02.zip"
# Set18= "http://vision.cs.stonybrook.edu/~kiwon/Datasets/SBU_Kinect_Interactions/s06s03.zip"
# Set19= "http://vision.cs.stonybrook.edu/~kiwon/Datasets/SBU_Kinect_Interactions/s06s04.zip"
# Set20= "http://vision.cs.stonybrook.edu/~kiwon/Datasets/SBU_Kinect_Interactions/s07s01.zip"
# Set21= "http://vision.cs.stonybrook.edu/~kiwon/Datasets/SBU_Kinect_Interactions/s07s03.zip"

# import urllib 
# #import requests

# for i in range(1,22):
#     s='%02d' % i
#     #print(s)
#     name="Set"+s
#     print(name)
#     url=locals()[name]
#     urllib.request.urlretrieve(url,"./dataset/demo_{}.zip".format(i))

# 解压下载的SBU数据集
# import os
# import time
# import zipfile
# def unzip(sourceFile, targetPath):
#     '''
#     :param sourceFile: 待解压zip路径
#     :param targetPath: 目标文件目录
#     :return:
#     '''
#     file = zipfile.ZipFile(sourceFile, 'r')
#     file.extractall(targetPath)
#     print('success to unzip file!')

# source="./dataset"
# target="./unzip"
# for i in range(1,22):   
#     filename="demo_"+str(i)
#     path=os.path.join(source,filename+".zip")
#     print(path)
#     target_path=os.path.join(target,str(i))
#     unzip(path,target_path)

# # 删除zip包
# import os
# import shutil
# target="/home/xuanchi/Pose_recognition/SBU/unzip"
# for i in range(1,22):   
#     #filename="demo_"+str(i)
#     #path=os.path.join(source,filename+".zip")
#     #print(path)
#     target_path=os.path.join(target,str(i))
#     del_path = os.path.join(target_path,"__MACOSX")
#     shutil.rmtree(del_path)
#     print(i)   


import os
import matplotlib.pyplot as plt

def process_skeleton_file(file_path, output_dir):
    with open(file_path) as f:
        data = f.readlines()

    for frame_number, row in enumerate(data):
        posture = row
        posture_data = [x.strip() for x in posture.split(',')]

        joint_info = {}
        for i, n in enumerate(range(1, len(posture_data), 3)):
            joint_info[i+1] = [1280 - float(posture_data[n])*2560, 960 - (float(posture_data[n+1])/1.2)*1920, posture_data[n+2]]
        
        person_1 = {k: joint_info[k] for k in range(1, 16)}
        person_2 = {k-15: joint_info[k] for k in range(16, 31)}
        joint_details = {
            1: 'HEAD', 2: 'NECK', 3: 'TORSO', 4: 'LEFT_SHOULDER',
            5: 'LEFT_ELBOW', 6: 'LEFT_HAND', 7: 'RIGHT_SHOULDER',
            8: 'RIGHT_ELBOW', 9: 'RIGHT_HAND', 10: 'LEFT_HIP',
            11: 'LEFT_KNEE', 12: 'LEFT_FOOT', 13: 'RIGHT_HIP',
            14: 'RIGHT_KNEE', 15: 'RIGHT_FOOT'
        }
        connect_map = [[1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 7, 8, 10, 11, 13, 14],
                       [2, 3, 4, 7, 4, 7, 10, 13, 5, 6, 8, 9, 11, 12, 14, 15]]

        plt.figure()
        for key, value in person_1.items():
            plt.plot(value[0], value[1], 'bo')
        for m, n in zip(connect_map[0], connect_map[1]):
            plt.plot((person_1[m][0], person_1[n][0]), (person_1[m][1], person_1[n][1]), 'b--')

        for key, value in person_2.items():
            plt.plot(value[0], value[1], 'go')
        for m, n in zip(connect_map[0], connect_map[1]):
            plt.plot((person_2[m][0], person_2[n][0]), (person_2[m][1], person_2[n][1]), 'g--')

        plt.title(f'Frame {frame_number}')
        plt.xlim(-1280, 1280)
        plt.ylim(-960, 960)
        
        # Define output path for each frame
        output_frame_path = os.path.join(output_dir, f'{frame_number:04d}.png')
        plt.savefig(output_frame_path)
        plt.close()

def recursive_process_directory(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file == 'skeleton_pos.txt':
                input_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, input_dir)
                output_dir_path = os.path.join(output_dir, relative_path)
                
                # Create directory if it doesn't exist
                os.makedirs(output_dir_path, exist_ok=True)
                
                process_skeleton_file(input_file_path, output_dir_path)
                print(f"Processed {input_file_path}")

# 主函数
def main():
    input_directory = r'/usr/local/inter-rel-net-hockey/data02/sbu/'  # 替换为 SBU 数据集的根目录路径
    output_directory = r'/demo/ARN-LSTM/visualize/results/sbu/'  # 替换为你希望保存图片的文件夹路径

    recursive_process_directory(input_directory, output_directory)

if __name__ == '__main__':
    main()



#运行一个脚本并将输出重定向到默认的 nohup.out 文件
# cmd: nohup python visualize_sbu_skeneton.py &  
 
#运行一个命令并将输出重定向到指定的文件
# cmd: nohup python visualize_sbu_skeneton.py > output_sbu.log 2>&1 &

#运行一个程序，但不生成输出文件
# cmd: nohup python visualize_sbu_skeneton.py > /dev/null 2>&1 &
