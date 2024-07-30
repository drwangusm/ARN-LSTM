#!/bin/bash
# nohup bash sbu_runs.sh > sbu_runs.log 2>&1&  #服务器后台运行，log保存至 sbu_runs.log中

# #SBU joint, no lstm, no fusion
# python3 src/run_protocol.py joint_rel_ave configs/SBU/no-lstm/joint_rel_ave.cfg SBU -n 5
# python3 src/run_protocol.py joint_rel_att configs/SBU/no-lstm/joint_rel_att.cfg SBU -n 5
# python3 src/run_protocol.py joint_no_rel_ave configs/SBU/no-lstm/joint_no_rel_ave.cfg SBU -n 5
# python3 src/run_protocol.py joint_no_rel_att configs/SBU/no-lstm/joint_no_rel_att.cfg SBU -n 5

# #SBU temp, no lstm, no fusion
# python3 src/run_protocol.py temp_rel_ave configs/SBU/no-lstm/temp_rel_ave.cfg SBU -n 5
# python3 src/run_protocol.py temp_rel_att configs/SBU/no-lstm/temp_rel_att.cfg SBU -n 5
# python3 src/run_protocol.py temp_no_rel_ave configs/SBU/no-lstm/temp_no_rel_ave.cfg SBU -n 5
# python3 src/run_protocol.py temp_no_rel_att configs/SBU/no-lstm/temp_no_rel_att.cfg SBU -n 5


# #SBU joint, lstm no fusion
# python3 src/run_protocol.py joint_rel_ave_lstm configs/SBU/lstm/joint_rel_ave_lstm.cfg SBU -n 5 -t
# python3 src/run_protocol.py joint_rel_att_lstm configs/SBU/lstm/joint_rel_att_lstm.cfg SBU -n 5 -t
# python3 src/run_protocol.py joint_no_rel_ave_lstm configs/SBU/lstm/joint_no_rel_ave_lstm.cfg SBU -n 5 -t
# python3 src/run_protocol.py joint_no_rel_att_lstm configs/SBU/lstm/joint_no_rel_att_lstm.cfg SBU -n 5 -t

# ##SBU temp, lstm no fusion
# python3 src/run_protocol.py temp_rel_ave_lstm configs/SBU/lstm/temp_rel_ave_lstm.cfg SBU -n 5 -t
# python3 src/run_protocol.py temp_rel_att_lstm configs/SBU/lstm/temp_rel_att_lstm.cfg SBU -n 5 -t
# python3 src/run_protocol.py temp_no_rel_ave_lstm configs/SBU/lstm/temp_no_rel_ave_lstm.cfg SBU -n 5 -t
# python3 src/run_protocol.py temp_no_rel_att_lstm configs/SBU/lstm/temp_no_rel_att_lstm.cfg SBU -n 5 -t


# #SBU no lstm, fusion
# python3 src/run_protocol.py ARN_rel_ave_before configs/SBU/lstm-fusion/ARN_rel_ave_before.cfg SBU -F middle -n 5
# python3 src/run_protocol.py ARN_rel_att_before configs/SBU/lstm-fusion/ARN_rel_att_before.cfg SBU -F middle -n 5
# python3 src/run_protocol.py ARN_no_rel_ave_before configs/SBU/lstm-fusion/ARN_no_rel_ave_before.cfg SBU -F middle -n 5
# python3 src/run_protocol.py ARN_no_rel_att_before configs/SBU/lstm-fusion/ARN_no_rel_att_before.cfg SBU -F middle -n 5

# python3 src/run_protocol.py ARN_rel_ave_after configs/SBU/lstm-fusion/ARN_rel_ave_after.cfg SBU -F middle -n 5
# python3 src/run_protocol.py ARN_rel_att_after configs/SBU/lstm-fusion/ARN_rel_att_after.cfg SBU -F middle -n 5
# python3 src/run_protocol.py ARN_no_rel_ave_after configs/SBU/lstm-fusion/ARN_no_rel_ave_after.cfg SBU -F middle -n 5
# python3 src/run_protocol.py ARN_no_rel_att_after configs/SBU/lstm-fusion/ARN_no_rel_att_after.cfg SBU -F middle -n 5



# #SBU lstm fusion -- run error
# python3 src/run_protocol.py ARN_rel_ave_before_lstm configs/SBU/lstm-fusion/ARN_rel_ave_before_lstm.cfg SBU -t -F middle -n 5
# python3 src/run_protocol.py ARN_rel_att_before_lstm configs/SBU/lstm-fusion/ARN_rel_att_before_lstm.cfg SBU -t -F middle -n 5
# python3 src/run_protocol.py ARN_no_rel_ave_before_lstm configs/SBU/lstm-fusion/ARN_no_rel_ave_before_lstm.cfg SBU -t -F middle -n 5
# python3 src/run_protocol.py ARN_no_rel_att_before_lstm configs/SBU/lstm-fusion/ARN_no_rel_att_before_lstm.cfg SBU -t -F middle -n 5

# python3 src/run_protocol.py ARN_rel_ave_after_lstm configs/SBU/lstm-fusion/ARN_rel_ave_after_lstm.cfg SBU -t -F middle -n 5
# python3 src/run_protocol.py ARN_rel_att_after_lstm configs/SBU/lstm-fusion/ARN_rel_att_after_lstm.cfg SBU -t -F middle -n 5
# python3 src/run_protocol.py ARN_no_rel_ave_after_lstm configs/SBU/lstm-fusion/ARN_no_rel_ave_after_lstm.cfg SBU -t -F middle -n 5
# python3 src/run_protocol.py ARN_no_rel_att_after_lstm configs/SBU/lstm-fusion/ARN_no_rel_att_after_lstm.cfg SBU -t -F middle -n 5

# ARN-LSTM fusion inward+outward
python3 src/run_protocol.py ARN-LSTM_inward configs/SBU/ARN-LSTM_inward.cfg SBU -n 1
python3 src/run_protocol.py ARN-LSTM_outward configs/SBU/ARN-LSTM_outward.cfg SBU -n 1
python3 src/run_protocol.py ARN-LSTM-fc1_inward+outward configs/SBU/ARN-LSTM-fc1_inward+outward.cfg SBU -F middle -n 1
