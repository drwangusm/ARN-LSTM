# pip install h5py
# pip install tables

import pandas as pd

# 读取 HDF5 文件中的表格数据
df = pd.read_hdf('/demo/ARN-LSTM/runs/models/SBU/ARN_inward/fold_0/rerun_0/relnet_weights-val_acc.hdf5', 'sbu')

# 查看数据框
print(df.head())
