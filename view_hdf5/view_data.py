import h5py

# 打开 .hdf5 文件
# with h5py.File('/demo/ARN-LSTM/runs/models/SBU/ARN_inward/fold_0/rerun_0/relnet_weights-val_acc.hdf5', 'r') as f:
#     # 列出所有的组
#     print("Keys: %s" % f.keys())
#     # 获取文件中第一个数据集的名称
#     a_group_key = list(f.keys())[0]

#     # 获取该数据集
#     data = f[a_group_key]

#     print("data:",data)
#     # 查看数据集的形状和数据类型
#     print(f"{a_group_key} shape: {data.shape}")
#     print(f"{a_group_key} dtype: {data.dtype}")

#     # 如果数据集是可索引的，查看数据集的前几个元素
#     if isinstance(data, h5py.Dataset):
#         print(data[:])


import h5py
import numpy as np

def print_hdf5_structure(file, show_full_data=False, max_elements=10):
    """
    递归地打印HDF5文件的结构，包括组和数据集的详细信息。
    
    参数:
    - file: h5py.File 对象
    - show_full_data: 如果为 True, 显示数据集的完整内容。否则，仅显示前 max_elements 个元素。
    - max_elements: 当 show_full_data 为 False 时，显示的最大元素数量。
    """
    def print_dataset_info(name, obj):
        print(f"Path: {name}")
        print(f"  Type: {type(obj)}")

        # 如果是组
        if isinstance(obj, h5py.Group):
            print(f"  Contains {len(obj.keys())} items")
        
        # 如果是数据集
        elif isinstance(obj, h5py.Dataset):
            print(f"  Dataset shape: {obj.shape}, dtype: {obj.dtype}")
            
            # 将数据集转换为 NumPy 数组
            data = np.array(obj)
            
            # 显示小型数据集的内容，对于较大的数据集，仅显示部分数据
            if show_full_data or obj.size <= max_elements:
                print(f"  Data: {data}")
            else:
                # 仅显示前 max_elements 个元素
                print(f"  Data (first {max_elements} elements): {data.ravel()[:max_elements]}")

        # 打印属性
        if obj.attrs:
            print(f"  Attributes:")
            for key, val in obj.attrs.items():
                print(f"    {key}: {val}")

        print("")

    # 递归遍历HDF5文件
    file.visititems(print_dataset_info)

# 打开HDF5文件并打印结构信息
with h5py.File('/demo/ARN-LSTM/runs/models/SBU/ARN_inward/fold_0/rerun_0/relnet_weights-val_acc.hdf5', 'r') as f:
    # 设定 show_full_data=True 以显示完整数据集，或者显示部分数据集
    print_hdf5_structure(f, show_full_data=False, max_elements=10)
