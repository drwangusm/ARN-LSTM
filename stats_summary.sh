#查看模型训练日志状态，执行命令例子
python src/misc/print_train_stats.py runs/models/UT-1/* -c val_loss

python src/misc/print_train_stats.py runs/models/UT-2/* -c val_loss

python src/misc/parse_train_log.py runs/models/UT-1/final_joint_no_rel_att_s1/fold_0/rerun_0/training.log -c val_loss

python src/misc/parse_train_log.py runs/models/UT-1/final_joint_no_rel_att_s1/fold_0/rerun_1/training.log -c val_loss

#运行summzrizeResults.py
python summarizeResults.py runs/models/UT-1

python summarizeResults.py runs/models/UT-2

python summarizeResults.py runs/models/YMJA


