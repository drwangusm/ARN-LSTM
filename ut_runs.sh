#!/bin/bash
# nohup bash ut_runs.sh > ut_runs.log 2>&1&  #服务器后台运行，log保存至 ut_runs.log中

# ##UT joint, no lstm, no fusion
# python3 src/run_protocol.py joint_rel_ave_s1 configs/UT/set_1/joint_rel_ave.cfg UT-1 -n 5 -v 2
# python3 src/run_protocol.py joint_rel_ave_s2 configs/UT/set_2/joint_rel_ave.cfg UT-2 -n 5 -v 2
# python3 src/run_protocol.py joint_rel_att_s1 configs/UT/set_1/joint_rel_att.cfg UT-1 -n 5 -v 2
# python3 src/run_protocol.py joint_rel_att_s2 configs/UT/set_2/joint_rel_att.cfg UT-2 -n 5 -v 2
# python3 src/run_protocol.py joint_no_rel_ave_s1 configs/UT/set_1/joint_no_rel_ave.cfg UT-1 -n 5 -v 2
# python3 src/run_protocol.py joint_no_rel_ave_s2 configs/UT/set_2/joint_no_rel_ave.cfg UT-2 -n 5 -v 2
# python3 src/run_protocol.py joint_no_rel_att_s1 configs/UT/set_1/joint_no_rel_att.cfg UT-1 -n 5 -v 2
# python3 src/run_protocol.py joint_no_rel_att_s2 configs/UT/set_2/joint_no_rel_att.cfg UT-2 -n 5 -v 2

# ##UT temp, no lstm, no fusion
# python3 src/run_protocol.py temp_rel_ave_s1 configs/UT/set_1/temp_rel_ave.cfg UT-1 -n 5 -v 2
# python3 src/run_protocol.py temp_rel_ave_s2 configs/UT/set_2/temp_rel_ave.cfg UT-2 -n 5 -v 2
# python3 src/run_protocol.py temp_rel_att_s1 configs/UT/set_1/temp_rel_att.cfg UT-1 -n 5 -v 2
# python3 src/run_protocol.py temp_rel_att_s2 configs/UT/set_2/temp_rel_att.cfg UT-2 -n 5 -v 2
# python3 src/run_protocol.py temp_no_rel_ave_s1 configs/UT/set_1/temp_no_rel_ave.cfg UT-1 -n 5 -v 2
# python3 src/run_protocol.py temp_no_rel_ave_s2 configs/UT/set_2/temp_no_rel_ave.cfg UT-2 -n 5 -v 2
# python3 src/run_protocol.py temp_no_rel_att_s1 configs/UT/set_1/temp_no_rel_att.cfg UT-1 -n 5 -v 2
# python3 src/run_protocol.py temp_no_rel_att_s2 configs/UT/set_2/temp_no_rel_att.cfg UT-2 -n 5 -v 2

# #UT joint, lstm, no fusion
# python3 src/run_protocol.py joint_rel_ave_lstm_s1 configs/UT/set_1/lstm/joint_rel_ave_lstm.cfg UT-1 -n 5 -t -v 2
# python3 src/run_protocol.py joint_rel_ave_lstm_s2 configs/UT/set_2/lstm/joint_rel_ave_lstm.cfg UT-2 -n 5 -t -v 2
# python3 src/run_protocol.py joint_rel_att_lstm_s1 configs/UT/set_1/lstm/joint_rel_att_lstm.cfg UT-1 -n 5 -t -v 2
# python3 src/run_protocol.py joint_rel_att_lstm_s2 configs/UT/set_2/lstm/joint_rel_att_lstm.cfg UT-2 -n 5 -t -v 2
# python3 src/run_protocol.py joint_no_rel_ave_lstm_s1 configs/UT/set_1/lstm/joint_no_rel_ave_lstm.cfg UT-1 -n 5 -t -v 2
# python3 src/run_protocol.py joint_no_rel_ave_lstm_s2 configs/UT/set_2/lstm/joint_no_rel_ave_lstm.cfg UT-2 -n 5 -t -v 2
# python3 src/run_protocol.py joint_no_rel_att_lstm_s1 configs/UT/set_1/lstm/joint_no_rel_att_lstm.cfg UT-1 -n 5 -t -v 2
# python3 src/run_protocol.py joint_no_rel_att_lstm_s2 configs/UT/set_2/lstm/joint_no_rel_att_lstm.cfg UT-2 -n 5 -t -v 2

# #UT temp, lstm, no fusion
# python3 src/run_protocol.py temp_rel_ave_lstm_s1 configs/UT/set_1/lstm/temp_rel_ave_lstm.cfg UT-1 -n 5 -t -v 2
# python3 src/run_protocol.py temp_rel_ave_lstm_s2 configs/UT/set_2/lstm/temp_rel_ave_lstm.cfg UT-2 -n 5 -t -v 2
# python3 src/run_protocol.py temp_rel_att_lstm_s1 configs/UT/set_1/lstm/temp_rel_att_lstm.cfg UT-1 -n 5 -t -v 2
# python3 src/run_protocol.py temp_rel_att_lstm_s2 configs/UT/set_2/lstm/temp_rel_att_lstm.cfg UT-2 -n 5 -t -v 2
# python3 src/run_protocol.py temp_no_rel_ave_lstm_s1 configs/UT/set_1/lstm/temp_no_rel_ave_lstm.cfg UT-1 -n 5 -t -v 2
# python3 src/run_protocol.py temp_no_rel_ave_lstm_s2 configs/UT/set_2/lstm/temp_no_rel_ave_lstm.cfg UT-2 -n 5 -t -v 2
# python3 src/run_protocol.py temp_no_rel_att_lstm_s1 configs/UT/set_1/lstm/temp_no_rel_att_lstm.cfg UT-1 -n 5 -t -v 2
# python3 src/run_protocol.py temp_no_rel_att_lstm_s2 configs/UT/set_2/lstm/temp_no_rel_att_lstm.cfg UT-2 -n 5 -t -v 2

# #UT two_stream
# python3 src/run_protocol.py ARN_rel_ave_after_s1 configs/UT/set_1/ARN_rel_ave_after.cfg UT-1 -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_rel_ave_after_s2 configs/UT/set_2/ARN_rel_ave_after.cfg UT-2 -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_rel_att_after_s1 configs/UT/set_1/ARN_rel_att_after.cfg UT-1 -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_rel_att_after_s2 configs/UT/set_2/ARN_rel_att_after.cfg UT-2 -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_no_rel_ave_after_s1 configs/UT/set_1/ARN_no_rel_ave_after.cfg UT-1 -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_no_rel_ave_after_s2 configs/UT/set_2/ARN_no_rel_ave_after.cfg UT-2 -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_no_rel_att_after_s1 configs/UT/set_1/ARN_no_rel_att_after.cfg UT-1 -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_no_rel_att_after_s2 configs/UT/set_2/ARN_no_rel_att_after.cfg UT-2 -F middle -n 5 -v 2

# python3 src/run_protocol.py ARN_rel_ave_before_s1 configs/UT/set_1/ARN_rel_ave_before.cfg UT-1 -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN__rel_ave_before_s2 configs/UT/set_2/ARN_rel_ave_before.cfg UT-2 -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_rel_att_before_s1 configs/UT/set_1/ARN_rel_att_before.cfg UT-1 -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_rel_att_before_s2 configs/UT/set_2/ARN_rel_att_before.cfg UT-2 -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_no_rel_ave_before_s1 configs/UT/set_1/ARN_no_rel_ave_before.cfg UT-1 -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_no_rel_ave_before_s2 configs/UT/set_2/ARN_no_rel_ave_before.cfg UT-2 -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_no_rel_att_before_s1 configs/UT/set_1/ARN_no_rel_att_before.cfg UT-1 -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_no_rel_att_before_s2 configs/UT/set_2/ARN_no_rel_att_before.cfg UT-2 -F middle -n 5 -v 2

# #UT two_stream --run error
# python3 src/run_protocol.py ARN_rel_ave_before_lstm_s1 configs/UT/set_1/lstm/ARN_rel_ave_before_lstm.cfg UT-1 -t -F middle -n 5 -v 2 # x
# python3 src/run_protocol.py ARN_rel_ave_before_lstm_s2 configs/UT/set_2/lstm/ARN_rel_ave_before_lstm.cfg UT-2 -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_rel_att_before_lstm_s1 configs/UT/set_1/lstm/ARN_rel_att_before_lstm.cfg UT-1 -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_rel_att_before_lstm_s2 configs/UT/set_2/lstm/ARN_rel_att_before_lstm.cfg UT-2 -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_no_rel_ave_before_lstm_s1 configs/UT/set_1/lstm/ARN_no_rel_ave_before_lstm.cfg UT-1 -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_no_rel_ave_before_lstm_s2 configs/UT/set_2/lstm/ARN_no_rel_ave_before_lstm.cfg UT-2 -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_no_rel_att_before_lstm_s1 configs/UT/set_1/lstm/ARN_no_rel_att_before_lstm.cfg UT-1 -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_no_rel_att_before_lstm_s2 configs/UT/set_2/lstm/ARN_no_rel_att_before_lstm.cfg UT-2 -t -F middle -n 5 -v 2

# python3 src/run_protocol.py ARN_rel_ave_after_lstm_s1 configs/UT/set_1/lstm/ARN_rel_ave_after_lstm.cfg UT-1 -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_rel_ave_after_lstm_s2 configs/UT/set_2/lstm/ARN_rel_ave_after_lstm.cfg UT-2 -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_rel_att_after_lstm_s1 configs/UT/set_1/lstm/ARN_rel_att_after_lstm.cfg UT-1 -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_rel_att_after_lstm_s2 configs/UT/set_2/lstm/ARN_rel_att_after_lstm.cfg UT-2 -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_no_rel_ave_after_lstm_s1 configs/UT/set_1/lstm/ARN_no_rel_ave_after_lstm.cfg UT-1 -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_no_rel_ave_after_lstm_s2 configs/UT/set_2/lstm/ARN_no_rel_ave_after_lstm.cfg UT-2 -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_no_rel_att_after_lstm_s1 configs/UT/set_1/lstm/ARN_no_rel_att_after_lstm.cfg UT-1 -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_no_rel_att_after_lstm_s2 configs/UT/set_2/lstm/ARN_no_rel_att_after_lstm.cfg UT-2 -t -F middle -n 5 -v 2


# # ARN-LSTM fusion inward+outward
python3 src/run_protocol.py ARN-LSTM_inward configs/UT/set_1/ARN-LSTM_inward.cfg UT-1 -n 5 -v 2
python3 src/run_protocol.py ARN-LSTM_outward configs/UT/set_1/ARN-LSTM_outward.cfg UT-1 -n 5 -v 2
python3 src/run_protocol.py ARN-LSTM_inward+outward configs/UT/set_1/ARN-LSTM_inward+outward.cfg UT-1 -F middle -v 2 -n 5
python3 src/run_protocol.py ARN-LSTM-fc1_inward+outward configs/UT/set_1/ARN-LSTM-fc1_inward+outward.cfg UT-1 -F middle -v 2 -n 5

python3 src/run_protocol.py ARN-LSTM_inward configs/UT/set_2/ARN-LSTM_inward.cfg UT-2 -n 5 -v 2
python3 src/run_protocol.py ARN-LSTM_outward configs/UT/set_2/ARN-LSTM_outward.cfg UT-2 -n 5 -v 2
python3 src/run_protocol.py ARN-LSTM-fc1_inward+outward configs/UT/set_2/ARN-LSTM-fc1_inward+outward.cfg UT-2 -F middle -v 2 -n 5
python3 src/run_protocol.py ARN-LSTM_inward+outward configs/UT/set_2/ARN-LSTM_inward+outward.cfg UT-2 -F middle -v 2 -n 5