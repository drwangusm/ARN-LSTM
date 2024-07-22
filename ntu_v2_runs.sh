#!/bin/bash

#nohup bash ntu_v2_runs.sh > ntu_v2_runs.log 2>&1&

#NTU-V2 joint, lstm no fusion
python3 src/run_protocol.py joint_rel_ave_lstm configs/NTU-V2/lstm/joint_rel_ave_lstm.cfg NTU-V2 -n 5 -t -v 2
python3 src/run_protocol.py joint_rel_att_lstm configs/NTU-V2/lstm/joint_rel_att_lstm.cfg NTU-V2 -n 5 -t -v 2
python3 src/run_protocol.py joint_no_rel_ave_lstm configs/NTU-V2/lstm/joint_no_rel_ave_lstm.cfg NTU-V2 -n 5 -t -v 2
python3 src/run_protocol.py joint_no_rel_att_lstm configs/NTU-V2/lstm/joint_no_rel_att_lstm.cfg NTU-V2 -n 5 -t -v 2

# #NTU-V2 lstm fusion , fusion cross_subject and cross_setup
# python3 src/run_protocol.py ARN_rel_ave_before_lstm configs/NTU-V2/lstm/ARN_rel_ave_before_lstm.cfg NTU-V2 -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_rel_att_before_lstm configs/NTU-V2/lstm/ARN_rel_att_before_lstm.cfg NTU-V2 -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_no_rel_ave_before_lstm configs/NTU-V2/lstm/ARN_no_rel_ave_before_lstm.cfg NTU-V2  -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_no_rel_att_before_lstm configs/NTU-V2/lstm/ARN_no_rel_att_before_lstm.cfg NTU-V2  -t -F middle -n 5 -v 2

# python3 src/run_protocol.py ARN_rel_ave_after_lstm configs/NTU-V2/lstm/ARN_rel_ave_after_lstm.cfg NTU-V2 -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_rel_att_after_lstm configs/NTU-V2/lstm/ARN_rel_att_after_lstm.cfg NTU-V2 -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_no_rel_ave_after_lstm configs/NTU-V2/lstm/ARN_no_rel_ave_after_lstm.cfg NTU-V2 -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_no_rel_att_after_lstm configs/NTU-V2/lstm/ARN_no_rel_att_after_lstm.cfg NTU-V2 -t -F middle -n 5 -v 2