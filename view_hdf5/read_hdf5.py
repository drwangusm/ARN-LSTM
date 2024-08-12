import h5py

def print_attrs(name, obj):
    print(f"{name}:")
    for key, val in obj.attrs.items():
        print(f"    {key}: {val}")

def visit_items(name, obj):
    print(f"{name} ({type(obj)})")
    if isinstance(obj, h5py.Dataset):
        print(f"  Dataset shape: {obj.shape}, dtype: {obj.dtype}")
    elif isinstance(obj, h5py.Group):
        print(f"  Group with {len(obj.keys())} items")

# 打开 .hdf5 文件
with h5py.File('/demo/ARN-LSTM/runs/models/SBU/ARN_inward/fold_0/rerun_0/relnet_weights-val_acc.hdf5', 'r') as f:
    # 递归打印文件中的所有组和数据集
    f.visititems(visit_items)

    # 打印某个特定对象的属性
    f.visititems(print_attrs)
