import pandas as pd
import numpy as np
import glob

from misc import data_io

#处理一组动作识别任务的数据集，并生成相应的训练和验证数据集。
#从一个预定义的数据目录结构中读取数据文件，构建包含动作、序列、路径等信息的DataFrame对象，并根据不同的折（fold）划分数据集。

DATA_DIR = '/usr/local/inter-rel-net-hockey/data02/sbu/'

""" Folder structure
<set>/
    <action_id>/
        001/
        [002] # not always
        [003] # not always
            depth_...
            rgb_...
            skeleton_pos.txt

Ex: DATA_DIR + '/s01s02/02/001/skeleton_pos.txt'
"""
#21个子集，每个子集对应一个不同的数据集。
SETS = ['s01s02','s01s03','s01s07','s02s01','s02s03','s02s06','s02s07','s03s02',
        's03s04','s03s05','s03s06','s04s02','s04s03','s04s06','s05s02','s05s03',
        's06s02','s06s03','s06s04','s07s01','s07s03']

#分为5份，将数据集分为5个折（fold），用于交叉验证，每个折包含若干个子集。
FOLDS = [
    [ 1,  9, 15, 19],
    [ 5,  7, 10, 16],
    [ 2,  3, 20, 21],
    [ 4,  6,  8, 11],
    [12, 13, 14, 17, 18]]

#8个动作类型，如接近、离开、踢、打等。
ACTIONS = ['Approaching','Departing','Kicking','Punching','Pushing','Hugging',
           'ShakingHands','Exchanging']

# SBU Kinect Interaction Dataset 中的每个动作类型包含以下数量的序列：
# Approaching: 21个序列
# Departing: 21个序列
# Kicking: 21个序列
# Punching: 24个序列
# Pushing: 23个序列
# Hugging: 25个序列
# Shaking Hands: 26个序列
# Exchanging Objects: 26个序列
# 总共有 8 种动作类型，包含 282 个序列。

#从指定的目录中读取数据，并生成一个包含所有数据路径及其相关信息的
def get_ground_truth(data_dir=DATA_DIR):
    setname_lst, fold_lst, seq_lst, action_lst, path_lst = [], [], [], [], []
    for set_id, set_name in enumerate(SETS):
        for action_id in range(len(ACTIONS)):
            search_exp = '{}/{}/{:02}/*'.format(data_dir, set_name, action_id+1)
            paths = glob.glob(search_exp) #查找符合指定模式的路径。
            paths.sort()
            #对每个路径，根据其所属子集找到对应的折，并将这些信息存入不同的列表中。
            for path in paths:
                seq = path.split('/')[-1]
                fold = np.argwhere([ set_id+1 in lst for lst in FOLDS ])[0,0]
                
                setname_lst.append(set_name)
                fold_lst.append(fold)
                seq_lst.append(seq)
                action_lst.append(action_id)
                path_lst.append(path)
    
    dataframe_dict = {'set_name': setname_lst,
                     'fold': fold_lst,
                     'seq': seq_lst,
                     'path': path_lst,
                     'action': action_lst}
    ground_truth = pd.DataFrame(dataframe_dict) #组合成一个DataFrame，称为ground_truth，它包含子集名称、折号、序列号、路径及动作类型。
    return ground_truth

#返回折的编号列表，用于后续函数调用。
def get_folds():
    folds = np.arange(len(FOLDS))
    
    return folds

#获取指定折号以外的数据（训练集）
def get_train_gt(fold_num):
    if fold_num < 0 or fold_num > 5:
        raise ValueError("fold_num must be within 0 and 5, value entered: "+str(fold_num))
    
    ground_truth = get_ground_truth()
    gt_split = ground_truth[ground_truth.fold != fold_num]
    
    return gt_split

#获取指定折号的数据（验证集）
def get_val_gt(fold_num):
    if fold_num < 0 or fold_num > 5:
        raise ValueError("fold_num must be within 0 and 5, value entered: "+str(fold_num))
    
    ground_truth = get_ground_truth()
    gt_split = ground_truth[ground_truth.fold == fold_num]
    
    return gt_split

#通过调用data_io.get_data，从ground_truth中获取实际的数据x和标签y，用于训练
def get_train(fold_num, **kwargs):
    if fold_num < 0 or fold_num > 5:
        raise ValueError("fold_num must be within 0 and 5, value entered: "+str(fold_num))
    
    ground_truth = get_ground_truth()
    gt_split = ground_truth[ground_truth.fold != fold_num]
    
    X, Y = data_io.get_data(gt_split, pose_style='SBU', **kwargs)
    
    return X, Y
#通过调用data_io.get_data，从ground_truth中获取实际验证数据x和标签y，用于验证 
def get_val(fold_num, **kwargs):
    if fold_num < 0 or fold_num > 5:
        raise ValueError("fold_num must be within 0 and 5, value entered: "+str(fold_num))
    
    ground_truth = get_ground_truth()
    gt_split = ground_truth[ground_truth.fold == fold_num]
    
    X, Y = data_io.get_data(gt_split, pose_style='SBU', **kwargs)
    
    return X, Y

