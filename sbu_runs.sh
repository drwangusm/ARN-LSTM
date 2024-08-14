#!/bin/bash
# nohup bash sbu_runs.sh > sbu_runs.log 2>&1&  #服务器后台运行，log保存至 sbu_runs.log中

#SBU joint, no lstm, no fusion
python3 src/run_protocol.py joint_rel_ave configs/SBU/no-lstm/joint_rel_ave.cfg SBU -n 5 -v 2
python3 src/run_protocol.py joint_rel_att configs/SBU/no-lstm/joint_rel_att.cfg SBU -n 5 -v 2
python3 src/run_protocol.py joint_no_rel_ave configs/SBU/no-lstm/joint_no_rel_ave.cfg SBU -n 5 -v 2
python3 src/run_protocol.py joint_no_rel_att configs/SBU/no-lstm/joint_no_rel_att.cfg SBU -n 5 -v 2

#SBU temp, no lstm, no fusion
python3 src/run_protocol.py temp_rel_ave configs/SBU/no-lstm/temp_rel_ave.cfg SBU -n 5 -v 2
python3 src/run_protocol.py temp_rel_att configs/SBU/no-lstm/temp_rel_att.cfg SBU -n 5 -v 2
python3 src/run_protocol.py temp_no_rel_ave configs/SBU/no-lstm/temp_no_rel_ave.cfg SBU -n 5 -v 2
python3 src/run_protocol.py temp_no_rel_att configs/SBU/no-lstm/temp_no_rel_att.cfg SBU -n 5 -v 2


#SBU joint, lstm no fusion
python3 src/run_protocol.py joint_rel_ave_lstm configs/SBU/lstm/joint_rel_ave_lstm.cfg SBU -n 5 -t -v 2
python3 src/run_protocol.py joint_rel_att_lstm configs/SBU/lstm/joint_rel_att_lstm.cfg SBU -n 5 -t -v 2
python3 src/run_protocol.py joint_no_rel_ave_lstm configs/SBU/lstm/joint_no_rel_ave_lstm.cfg SBU -n 5 -t -v 2
python3 src/run_protocol.py joint_no_rel_att_lstm configs/SBU/lstm/joint_no_rel_att_lstm.cfg SBU -n 5 -t -v 2

##SBU temp, lstm no fusion
python3 src/run_protocol.py temp_rel_ave_lstm configs/SBU/lstm/temp_rel_ave_lstm.cfg SBU -n 5 -t -v 2
python3 src/run_protocol.py temp_rel_att_lstm configs/SBU/lstm/temp_rel_att_lstm.cfg SBU -n 5 -t -v 2
python3 src/run_protocol.py temp_no_rel_ave_lstm configs/SBU/lstm/temp_no_rel_ave_lstm.cfg SBU -n 5 -t -v 2
python3 src/run_protocol.py temp_no_rel_att_lstm configs/SBU/lstm/temp_no_rel_att_lstm.cfg SBU -n 5 -t -v 2


#SBU no lstm, fusion
python3 src/run_protocol.py ARN_rel_ave_before configs/SBU/lstm-fusion/ARN_rel_ave_before.cfg SBU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_rel_att_before configs/SBU/lstm-fusion/ARN_rel_att_before.cfg SBU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_ave_before configs/SBU/lstm-fusion/ARN_no_rel_ave_before.cfg SBU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_att_before configs/SBU/lstm-fusion/ARN_no_rel_att_before.cfg SBU -F middle -n 5 -v 2

python3 src/run_protocol.py ARN_rel_ave_after configs/SBU/lstm-fusion/ARN_rel_ave_after.cfg SBU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_rel_att_after configs/SBU/lstm-fusion/ARN_rel_att_after.cfg SBU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_ave_after configs/SBU/lstm-fusion/ARN_no_rel_ave_after.cfg SBU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_att_after configs/SBU/lstm-fusion/ARN_no_rel_att_after.cfg SBU -F middle -n 5 -v 2



#SBU lstm fusion -- run error
python3 src/run_protocol.py ARN_rel_ave_before_lstm configs/SBU/lstm-fusion/ARN_rel_ave_before_lstm.cfg SBU -t -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_rel_att_before_lstm configs/SBU/lstm-fusion/ARN_rel_att_before_lstm.cfg SBU -t -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_ave_before_lstm configs/SBU/lstm-fusion/ARN_no_rel_ave_before_lstm.cfg SBU -t -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_att_before_lstm configs/SBU/lstm-fusion/ARN_no_rel_att_before_lstm.cfg SBU -t -F middle -n 5 -v 2

python3 src/run_protocol.py ARN_rel_ave_after_lstm configs/SBU/lstm-fusion/ARN_rel_ave_after_lstm.cfg SBU -t -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_rel_att_after_lstm configs/SBU/lstm-fusion/ARN_rel_att_after_lstm.cfg SBU -t -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_ave_after_lstm configs/SBU/lstm-fusion/ARN_no_rel_ave_after_lstm.cfg SBU -t -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_att_after_lstm configs/SBU/lstm-fusion/ARN_no_rel_att_after_lstm.cfg SBU -t -F middle -n 5 -v 2

# ARN fusion inward+outward
python3 src/run_protocol.py ARN_inward configs/SBU/ARN_inward.cfg SBU -n 5 -v 2
python3 src/run_protocol.py ARN_outward configs/SBU/ARN_outward.cfg SBU -n 5 -v 2
python3 src/run_protocol.py ARN_inward+outward configs/SBU/ARN_inward+outward.cfg SBU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN-fc1_inward+outward configs/SBU/ARN-fc1_inward+outward.cfg SBU -F middle -n 5 -v 2

# ARN two stream fusion 
python3 src/run_protocol.py ARN_joint_stream configs/SBU/ARN_joint_stream.cfg SBU -n 5 -v 2
python3 src/run_protocol.py ARN_temporal_stream configs/SBU/ARN_temporal_stream.cfg SBU -n 5 -v 2
python3 src/run_protocol.py ARN_two_stream configs/SBU/ARN_two_stream.cfg SBU -F middle -n 5 -v 2

# ARN two stream fusion att
python3 src/run_protocol.py ARN_joint_stream_att configs/SBU/ARN_joint_stream_att.cfg SBU -n 5 -v 2 # x
python3 src/run_protocol.py ARN_temporal_stream_att configs/SBU/ARN_temporal_stream_att.cfg SBU -n 5 -v 2 # x
python3 src/run_protocol.py ARN_two_stream_att configs/SBU/ARN_two_stream_att.cfg SBU -F middle -n 5 -v 2 # x
# ARN two stream fusion att_avg
python3 src/run_protocol.py ARN_two_stream_att_avg configs/SBU/ARN_two_stream_att_avg.cfg SBU -F middle -n 5 -v 2 # x 

# ARN two stream fusion att + projection_size2000
python3 src/run_protocol.py ARN_joint_stream_att_proj_2000 configs/SBU/ARN_joint_stream_att_proj_2000.cfg SBU -n 5 -v 2
python3 src/run_protocol.py ARN_temporal_stream_att_proj_2000 configs/SBU/ARN_temporal_stream_att_proj_2000.cfg SBU -n 5 -v 2
python3 src/run_protocol.py ARN_two_stream_att_proj_2000 configs/SBU/ARN_two_stream_att_proj_2000.cfg SBU -F middle -n 5 -v 2

# ARN two stream fusion att + projection_size2000 with no use_relations
python3 src/run_protocol.py ARN_joint_stream_att_no_rel_proj_2000 configs/SBU/ARN_joint_stream_att_no_rel_proj_2000.cfg SBU -n 5 -v 2
python3 src/run_protocol.py ARN_temporal_stream_att_no_rel_proj_2000 configs/SBU/ARN_temporal_stream_att_no_rel_proj_2000.cfg SBU -n 5 -v 2
python3 src/run_protocol.py ARN_two_stream_att_no_rel_proj_2000 configs/SBU/ARN_two_stream_att_no_rel_proj_2000.cfg SBU -F middle -n 5 -v 2

# ARN-LSTM fusion inward+outward
python3 src/run_protocol.py ARN-LSTM_inward configs/SBU/ARN-LSTM_inward.cfg SBU -n 5 -v 2
python3 src/run_protocol.py ARN-LSTM_outward configs/SBU/ARN-LSTM_outward.cfg SBU -n 5 -v 2
python3 src/run_protocol.py ARN-LSTM_inward+outward configs/SBU/ARN-LSTM_inward+outward.cfg SBU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN-LSTM-fc1_inward+outward configs/SBU/ARN-LSTM-fc1_inward+outward.cfg SBU -F middle -n 5 -v 2

# other experiments
python3 src/run_protocol.py ARN_inward_no_aug configs/SBU/ARN_inward-no_aug.cfg SBU -n 5 -v 2
python3 src/run_protocol.py ARN_outward_no_aug configs/SBU/ARN_outward-no_aug.cfg SBU -n 5 -v 2
python3 src/run_protocol.py ARN-Naive_inward+outward configs/SBU/ARN-Naive_inward+outward.cfg SBU -n 5 -v 2

python3 src/run_protocol.py ARN_inward_random configs/SBU/ARN_inward_random.cfg SBU -n 5 -v 2
python3 src/run_protocol.py ARN_outward_random configs/SBU/ARN_outward_random.cfg SBU -n 5 -v 2
python3 src/run_protocol.py ARN_inward+outward_random configs/SBU/ARN_inward+outward_random.cfg SBU -F middle -n 5 -v 2

