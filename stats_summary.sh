#查看模型训练日志状态，执行命令例子 print log info
python src/misc/print_train_stats.py runs/models/UT-1/* -c val_loss

python src/misc/print_train_stats.py runs/models/UT-2/* -c val_loss

python src/misc/parse_train_log.py runs/models/UT-1/joint_no_rel_att_s1/fold_0/rerun_0/training.log -c val_loss

python src/misc/parse_train_log.py runs/models/UT-1/joint_no_rel_att_s1/fold_0/rerun_1/training.log -c val_loss

#run print_summarize_results.py
#UT-1
python print_summarize_results.py runs/models/UT-1/ARN_no_rel_att_after_s1
python print_summarize_results.py runs/models/UT-1/ARN_no_rel_att_before_s1
python print_summarize_results.py runs/models/UT-1/ARN_no_rel_ave_after_s1
python print_summarize_results.py runs/models/UT-1/ARN_no_rel_ave_before_s1
python print_summarize_results.py runs/models/UT-1/ARN_rel_att_after_s1
python print_summarize_results.py runs/models/UT-1/ARN_rel_att_before_s1
python print_summarize_results.py runs/models/UT-1/ARN_rel_ave_after_s1
python print_summarize_results.py runs/models/UT-1/ARN_rel_ave_before_s1
python print_summarize_results.py runs/models/UT-1/joint_no_rel_att_lstm_s1
python print_summarize_results.py runs/models/UT-1/joint_no_rel_att_s1
python print_summarize_results.py runs/models/UT-1/joint_no_rel_ave_lstm_s1
python print_summarize_results.py runs/models/UT-1/joint_no_rel_ave_s1
python print_summarize_results.py runs/models/UT-1/joint_rel_att_lstm_s1
python print_summarize_results.py runs/models/UT-1/joint_rel_att_s1
python print_summarize_results.py runs/models/UT-1/joint_rel_ave_lstm_s1
python print_summarize_results.py runs/models/UT-1/joint_rel_ave_s1
python print_summarize_results.py runs/models/UT-1/temp_no_rel_att_lstm_s1
python print_summarize_results.py runs/models/UT-1/temp_no_rel_att_s1
python print_summarize_results.py runs/models/UT-1/temp_no_rel_ave_lstm_s1
python print_summarize_results.py runs/models/UT-1/temp_no_rel_ave_s1
python print_summarize_results.py runs/models/UT-1/temp_rel_att_lstm_s1
python print_summarize_results.py runs/models/UT-1/temp_rel_att_s1
python print_summarize_results.py runs/models/UT-1/temp_rel_ave_lstm_s1
python print_summarize_results.py runs/models/UT-1/temp_rel_ave_s1

#ut-2
# python print_summarize_results.py runs/models/UT-2


#SBU
python print_summarize_results.py runs/models/SBU/joint_rel_ave
python print_summarize_results.py runs/models/SBU/joint_rel_att
python print_summarize_results.py runs/models/SBU/joint_no_rel_ave
python print_summarize_results.py runs/models/SBU/joint_no_rel_att
python print_summarize_results.py runs/models/SBU/temp_rel_ave
python print_summarize_results.py runs/models/SBU/temp_rel_att
python print_summarize_results.py runs/models/SBU/temp_no_rel_ave
python print_summarize_results.py runs/models/SBU/temp_no_rel_att
python print_summarize_results.py runs/models/SBU/joint_rel_ave_lstm
python print_summarize_results.py runs/models/SBU/joint_rel_att_lstm
python print_summarize_results.py runs/models/SBU/joint_no_rel_ave_lstm
python print_summarize_results.py runs/models/SBU/joint_no_rel_att_lstm
python print_summarize_results.py runs/models/SBU/temp_rel_ave_lstm
python print_summarize_results.py runs/models/SBU/temp_rel_att_lstm
python print_summarize_results.py runs/models/SBU/temp_no_rel_ave_lstm
python print_summarize_results.py runs/models/SBU/temp_no_rel_att_lstm
python print_summarize_results.py runs/models/SBU/ARN_rel_ave_before
python print_summarize_results.py runs/models/SBU/ARN_rel_att_before
python print_summarize_results.py runs/models/SBU/ARN_no_rel_ave_before
python print_summarize_results.py runs/models/SBU/ARN_no_rel_att_before
python print_summarize_results.py runs/models/SBU/ARN_rel_ave_after
python print_summarize_results.py runs/models/SBU/ARN_rel_att_after
python print_summarize_results.py runs/models/SBU/ARN_no_rel_ave_after
python print_summarize_results.py runs/models/SBU/ARN_no_rel_att_after
python print_summarize_results.py runs/models/SBU/ARN_rel_ave_before_lstm
python print_summarize_results.py runs/models/SBU/ARN_rel_att_before_lstm
python print_summarize_results.py runs/models/SBU/ARN_no_rel_ave_before_lstm
python print_summarize_results.py runs/models/SBU/ARN_no_rel_att_before_lstm
python print_summarize_results.py runs/models/SBU/ARN_rel_ave_after_lstm
python print_summarize_results.py runs/models/SBU/ARN_rel_att_after_lstm
python print_summarize_results.py runs/models/SBU/ARN_no_rel_ave_after_lstm
python print_summarize_results.py runs/models/SBU/ARN_no_rel_att_after_lstm

#NTU-V1
python print_summarize_results.py runs/models/NTU-V1/joint_rel_ave
python print_summarize_results.py runs/models/NTU-V1/joint_rel_att
python print_summarize_results.py runs/models/NTU-V1/joint_no_rel_ave
python print_summarize_results.py runs/models/NTU-V1/joint_no_rel_att
python print_summarize_results.py runs/models/NTU-V1/temp_rel_ave
python print_summarize_results.py runs/models/NTU-V1/temp_rel_att
python print_summarize_results.py runs/models/NTU-V1/temp_no_rel_ave
python print_summarize_results.py runs/models/NTU-V1/temp_no_rel_att
python print_summarize_results.py runs/models/NTU-V1/ARN_rel_ave_before
python print_summarize_results.py runs/models/NTU-V1/ARN_rel_att_before
python print_summarize_results.py runs/models/NTU-V1/ARN_no_rel_ave_before
python print_summarize_results.py runs/models/NTU-V1/ARN_no_rel_att_before
python print_summarize_results.py runs/models/NTU-V1/ARN_rel_ave_after
python print_summarize_results.py runs/models/NTU-V1/ARN_rel_att_after
python print_summarize_results.py runs/models/NTU-V1/ARN_no_rel_ave_after
python print_summarize_results.py runs/models/NTU-V1/ARN_no_rel_att_after
python print_summarize_results.py runs/models/NTU-V1/temp_rel_ave_lstm
python print_summarize_results.py runs/models/NTU-V1/temp_rel_att_lstm
python print_summarize_results.py runs/models/NTU-V1/temp_no_rel_ave_lstm
python print_summarize_results.py runs/models/NTU-V1/temp_no_rel_att_lstm
python print_summarize_results.py runs/models/NTU-V1/joint_rel_ave_lstm
python print_summarize_results.py runs/models/NTU-V1/joint_rel_att_lstm
python print_summarize_results.py runs/models/NTU-V1/joint_no_rel_ave_lstm
python print_summarize_results.py runs/models/NTU-V1/joint_no_rel_att_lstm
python print_summarize_results.py runs/models/NTU-V1/ARN_rel_ave_before_lstm
python print_summarize_results.py runs/models/NTU-V1/ARN_rel_att_before_lstm
python print_summarize_results.py runs/models/NTU-V1/ARN_no_rel_ave_before_lstm
python print_summarize_results.py runs/models/NTU-V1/ARN_no_rel_att_before_lstm
python print_summarize_results.py runs/models/NTU-V1/ARN_rel_ave_after_lstm
python print_summarize_results.py runs/models/NTU-V1/ARN_rel_att_after_lstm
python print_summarize_results.py runs/models/NTU-V1/ARN_no_rel_ave_after_lstm
python print_summarize_results.py runs/models/NTU-V1/ARN_no_rel_att_after_lstm


#NTU-2
python print_summarize_results.py runs/models/NTU-V2/joint_rel_ave
python print_summarize_results.py runs/models/NTU-V2/joint_rel_att
python print_summarize_results.py runs/models/NTU-V2/joint_no_rel_ave
python print_summarize_results.py runs/models/NTU-V2/joint_no_rel_att
python print_summarize_results.py runs/models/NTU-V2/temp_rel_ave
python print_summarize_results.py runs/models/NTU-V2/temp_rel_att
python print_summarize_results.py runs/models/NTU-V2/temp_no_rel_ave
python print_summarize_results.py runs/models/NTU-V2/temp_no_rel_att
python print_summarize_results.py runs/models/NTU-V2/ARN_rel_ave_before
python print_summarize_results.py runs/models/NTU-V2/ARN_rel_att_before
python print_summarize_results.py runs/models/NTU-V2/ARN_no_rel_ave_before
python print_summarize_results.py runs/models/NTU-V2/ARN_no_rel_att_before
python print_summarize_results.py runs/models/NTU-V2/ARN_rel_ave_after
python print_summarize_results.py runs/models/NTU-V2/ARN_rel_att_after
python print_summarize_results.py runs/models/NTU-V2/ARN_no_rel_ave_after
python print_summarize_results.py runs/models/NTU-V2/ARN_no_rel_att_after
python print_summarize_results.py runs/models/NTU-V2/temp_rel_ave_lstm
python print_summarize_results.py runs/models/NTU-V2/temp_rel_att_lstm
python print_summarize_results.py runs/models/NTU-V2/temp_no_rel_ave_lstm
python print_summarize_results.py runs/models/NTU-V2/temp_no_rel_att_lstm
python print_summarize_results.py runs/models/NTU-V2/joint_rel_ave_lstm
python print_summarize_results.py runs/models/NTU-V2/joint_rel_att_lstm
python print_summarize_results.py runs/models/NTU-V2/joint_no_rel_ave_lstm
python print_summarize_results.py runs/models/NTU-V2/joint_no_rel_att_lstm
python print_summarize_results.py runs/models/NTU-V2/ARN_rel_ave_before_lstm
python print_summarize_results.py runs/models/NTU-V2/ARN_rel_att_before_lstm
python print_summarize_results.py runs/models/NTU-V2/ARN_no_rel_ave_before_lstm
python print_summarize_results.py runs/models/NTU-V2/ARN_no_rel_att_before_lstm
python print_summarize_results.py runs/models/NTU-V2/ARN_rel_ave_after_lstm
python print_summarize_results.py runs/models/NTU-V2/ARN_rel_att_after_lstm
python print_summarize_results.py runs/models/NTU-V2/ARN_no_rel_ave_after_lstm
python print_summarize_results.py runs/models/NTU-V2/ARN_no_rel_att_after_lstm




