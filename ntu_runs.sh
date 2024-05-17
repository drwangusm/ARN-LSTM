#!/bin/bash
#NTU-V1 joint, no lstm, no fusion
python3 src/run_protocol.py joint_rel_ave_v1 configs/NTU-V1/no-lstm/joint_rel_ave.cfg NTU -n 5 -v 2
python3 src/run_protocol.py joint_rel_att_v1 configs/NTU-V1/no-lstm/joint_rel_att.cfg NTU -n 5 -v 2
python3 src/run_protocol.py joint_no_rel_ave_v1 configs/NTU-V1/no-lstm/joint_no_rel_ave.cfg NTU -n 5 -v 2
python3 src/run_protocol.py joint_no_rel_att_v1 configs/NTU-V1/no-lstm/joint_no_rel_att.cfg NTU -n 5 -v 2

##NTU-V1 temp, no lstm, no fusion
python3 src/run_protocol.py temp_rel_ave_v1 configs/NTU-V1/no-lstm/temp_rel_ave.cfg NTU -n 5 -v 2
python3 src/run_protocol.py temp_rel_att_v1 configs/NTU-V1/no-lstm/temp_rel_att.cfg NTU -n 5 -v 2
python3 src/run_protocol.py temp_no_rel_ave_v1 configs/NTU-V1/no-lstm/temp_no_rel_ave.cfg NTU -n 5 -v 2
python3 src/run_protocol.py temp_no_rel_att_v1 configs/NTU-V1/no-lstm/temp_no_rel_att.cfg NTU -n 5 -v 2

#NTU-V1 no lstm, fusion
python3 src/run_protocol.py ARN_rel_ave_before_v1 configs/NTU-V1/no-lstm/ARN_rel_ave_before.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_rel_att_before_v1 configs/NTU-V1/no-lstm/ARN_rel_att_before.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_ave_before_v1 configs/NTU-V1/no-lstm/ARN_no_rel_ave_before.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_att_before_v1 configs/NTU-V1/no-lstm/ARN_no_rel_att_before.cfg NTU -F middle -n 5 -v 2

python3 src/run_protocol.py ARN_rel_ave_after_v1 configs/NTU-V1/no-lstm/ARN_rel_ave_after.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_rel_att_after_v1 configs/NTU-V1/no-lstm/ARN_rel_att_after.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_ave_after_v1 configs/NTU-V1/no-lstm/ARN_no_rel_ave_after.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_att_after_v1 configs/NTU-V1/no-lstm/ARN_no_rel_att_after.cfg NTU -F middle -n 5 -v 2

#NTU-V1 temp, lstm no fusion
python3 src/run_protocol.py temp_rel_ave_lstm_v1 configs/NTU-V1/lstm/temp_rel_ave_lstm.cfg NTU -n 5 -t -v 2
python3 src/run_protocol.py temp_rel_att_lstm_v1 configs/NTU-V1/lstm/temp_rel_att_lstm.cfg NTU -n 5 -t -v 2
python3 src/run_protocol.py temp_no_rel_ave_lstm_v1 configs/NTU-V1/lstm/temp_no_rel_ave_lstm.cfg NTU -n 5 -t -v 2
python3 src/run_protocol.py temp_no_rel_att_lstm_v1 configs/NTU-V1/lstm/temp_no_rel_att_lstm.cfg NTU -n 5 -t -v 2

#NTU-V1 joint, lstm no fusion
python3 src/run_protocol.py joint_rel_ave_lstm_v1 configs/NTU-V1/lstm/joint_rel_ave_lstm.cfg NTU -n 5 -t -v 2
python3 src/run_protocol.py joint_rel_att_lstm_v1 configs/NTU-V1/lstm/joint_rel_att_lstm.cfg NTU -n 5 -t -v 2
python3 src/run_protocol.py joint_no_rel_ave_lstm_v1 configs/NTU-V1/lstm/joint_no_rel_ave_lstm.cfg NTU -n 5 -t -v 2
python3 src/run_protocol.py joint_no_rel_att_lstm_v1 configs/NTU-V1/lstm/joint_no_rel_att_lstm.cfg NTU -n 5 -t -v 2

# NTU-V1 lstm fusion --run error
python3 src/run_protocol.py ARN_rel_ave_before_lstm_v1 configs/NTU-V1/lstm/ARN_rel_ave_before_lstm.cfg NTU -t -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_rel_att_before_lstm_v1 configs/NTU-V1/lstm/ARN_rel_att_before_lstm.cfg NTU -t -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_ave_before_lstm_v1 configs/NTU-V1/lstm/ARN_no_rel_ave_before_lstm.cfg NTU -t -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_att_before_lstm_v1 configs/NTU-V1/lstm/ARN_no_rel_att_before_lstm.cfg NTU -t -F middle -n 5 -v 2

python3 src/run_protocol.py ARN_rel_ave_after_lstm_v1 configs/NTU-V1/lstm/ARN_rel_ave_after_lstm.cfg NTU -t -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_rel_att_after_lstm_v1 configs/NTU-V1/lstm/ARN_rel_att_after_lstm.cfg NTU -t -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_ave_after_lstm_v1 configs/NTU-V1/lstm/ARN_no_rel_ave_after_lstm.cfg NTU -t -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_att_after_lstm_v1 configs/NTU-V1/lstm/ARN_no_rel_att_after_lstm.cfg NTU -t -F middle -n 5 -v 2


##NTU-v2 cs joint, temp, no lstm no two_stream
# python3 src/run_protocol.py joint_rel_ave_cs configs/NTU-V2/no-lstm/joint_rel_ave.cfg NTU-V2 -n 5 -f cross_subject
# python3 src/run_protocol.py joint_rel_ave_cv configs/NTU-V2/no-lstm/joint_rel_ave.cfg NTU-V2 -n 5 -f cross_setup #cross_view
# python3 src/run_protocol.py joint_rel_att_cs configs/NTU-V2/no-lstm/joint_rel_att.cfg NTU-V2 -n 5 -f cross_subject
# python3 src/run_protocol.py joint_rel_att_cv configs/NTU-V2/no-lstm/joint_rel_att.cfg NTU-V2 -n 5 -f cross_setup
# python3 src/run_protocol.py joint_no_rel_ave_cs configs/NTU-V2/no-lstm/joint_no_rel_ave.cfg NTU-V2 -n 5 -f cross_subject
# python3 src/run_protocol.py joint_no_rel_ave_cv configs/NTU-V2/no-lstm/joint_no_rel_ave.cfg NTU-V2 -n 5 -f cross_setup
# python3 src/run_protocol.py joint_no_rel_att_cs configs/NTU-V2/no-lstm/joint_no_rel_att.cfg NTU-V2 -n 5 -f cross_subject
# python3 src/run_protocol.py joint_no_rel_att_cv configs/NTU-V2/no-lstm/joint_no_rel_att.cfg NTU-V2 -n 5 -f cross_setup

# python3 src/run_protocol.py temp_rel_ave_cs configs/NTU-V2/no-lstm/temp_rel_ave.cfg NTU-V2 -n 5 -f cross_subject
# python3 src/run_protocol.py temp_rel_ave_cv configs/NTU-V2/no-lstm/temp_rel_ave.cfg NTU-V2 -n 5 -f cross_setup
# python3 src/run_protocol.py temp_rel_att_cs configs/NTU-V2/no-lstm/temp_rel_att.cfg NTU-V2 -n 5 -f cross_subject
# python3 src/run_protocol.py temp_rel_att_cv configs/NTU-V2/no-lstm/temp_rel_att.cfg NTU-V2 -n 5 -f cross_setup
# python3 src/run_protocol.py temp_no_rel_ave_cs configs/NTU-V2/no-lstm/temp_no_rel_ave.cfg NTU-V2 -n 5 -f cross_subject
# python3 src/run_protocol.py temp_no_rel_ave_cv configs/NTU-V2/no-lstm/temp_no_rel_ave.cfg NTU-V2 -n 5 -f cross_setup
# python3 src/run_protocol.py temp_no_rel_att_cs configs/NTU-V2/no-lstm/temp_no_rel_att.cfg NTU-V2 -n 5 -f cross_subject
# python3 src/run_protocol.py temp_no_rel_att_cv configs/NTU-V2/no-lstm/temp_no_rel_att.cfg NTU-V2 -n 5 -f cross_setup

#NTU-V2 no lstm, fusion  --run error
python3 src/run_protocol.py ARN_rel_ave_before_v1 configs/NTU-V2/no-lstm/ARN_rel_ave_before.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_rel_att_before_v1 configs/NTU-V2/no-lstm/ARN_rel_att_before.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_ave_before_v1 configs/NTU-V2/no-lstm/ARN_no_rel_ave_before.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_att_before_v1 configs/NTU-V2/no-lstm/ARN_no_rel_att_before.cfg NTU -F middle -n 5 -v 2

python3 src/run_protocol.py ARN_rel_ave_after_v1 configs/NTU-V2/no-lstm/ARN_rel_ave_after.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_rel_att_after_v1 configs/NTU-V2/no-lstm/ARN_rel_att_after.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_ave_after_v1 configs/NTU-V2/no-lstm/ARN_no_rel_ave_after.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_att_after_v1 configs/NTU-V2/no-lstm/ARN_no_rel_att_after.cfg NTU -F middle -n 5 -v 2

#NTU-V2 lstm fusion --run error
python3 src/run_protocol.py ARN_rel_ave_before_lstm_v1 configs/NTU-V2/lstm/ARN_rel_ave_before_lstm.cfg NTU -t -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_rel_att_before_lstm_v1 configs/NTU-V2/lstm/ARN_rel_att_before_lstm.cfg NTU -t -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_ave_before_lstm_v1 configs/NTU-V2/lstm/ARN_no_rel_ave_before_lstm.cfg NTU -t -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_att_before_lstm_v1 configs/NTU-V2/lstm/ARN_no_rel_att_before_lstm.cfg NTU -t -F middle -n 5 -v 2

python3 src/run_protocol.py ARN_rel_ave_after_lstm_v1 configs/NTU-V2/lstm/ARN_rel_ave_after_lstm.cfg NTU -t -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_rel_att_after_lstm_v1 configs/NTU-V2/lstm/ARN_rel_att_after_lstm.cfg NTU -t -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_ave_after_lstm_v1 configs/NTU-V2/lstm/ARN_no_rel_ave_after_lstm.cfg NTU -t -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_att_after_lstm_v1 configs/NTU-V2/lstm/ARN_no_rel_att_after_lstm.cfg NTU -t -F middle -n 5 -v 2
