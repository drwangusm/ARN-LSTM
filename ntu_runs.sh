#!/bin/bash
#NTU-V1 joint, no lstm, no fusion
python3 src/run_protocol.py joint_rel_ave configs/NTU-V1/no-lstm/joint_rel_ave.cfg NTU -n 5 -v 2
python3 src/run_protocol.py joint_rel_att configs/NTU-V1/no-lstm/joint_rel_att.cfg NTU -n 5 -v 2
python3 src/run_protocol.py joint_no_rel_ave configs/NTU-V1/no-lstm/joint_no_rel_ave.cfg NTU -n 5 -v 2
python3 src/run_protocol.py joint_no_rel_att configs/NTU-V1/no-lstm/joint_no_rel_att.cfg NTU -n 5 -v 2

##NTU-V1 temp, no lstm, no fusion
python3 src/run_protocol.py temp_rel_ave configs/NTU-V1/no-lstm/temp_rel_ave.cfg NTU -n 5 -v 2
python3 src/run_protocol.py temp_rel_att configs/NTU-V1/no-lstm/temp_rel_att.cfg NTU -n 5 -v 2
python3 src/run_protocol.py temp_no_rel_ave configs/NTU-V1/no-lstm/temp_no_rel_ave.cfg NTU -n 5 -v 2
python3 src/run_protocol.py temp_no_rel_att configs/NTU-V1/no-lstm/temp_no_rel_att.cfg NTU -n 5 -v 2

#NTU-V1 no lstm, fusion
python3 src/run_protocol.py ARN_rel_ave_before configs/NTU-V1/no-lstm/ARN_rel_ave_before.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_rel_att_before configs/NTU-V1/no-lstm/ARN_rel_att_before.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_ave_before configs/NTU-V1/no-lstm/ARN_no_rel_ave_before.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_att_before configs/NTU-V1/no-lstm/ARN_no_rel_att_before.cfg NTU -F middle -n 5 -v 2

python3 src/run_protocol.py ARN_rel_ave_after configs/NTU-V1/no-lstm/ARN_rel_ave_after.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_rel_att_after configs/NTU-V1/no-lstm/ARN_rel_att_after.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_ave_after configs/NTU-V1/no-lstm/ARN_no_rel_ave_after.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_att_after configs/NTU-V1/no-lstm/ARN_no_rel_att_after.cfg NTU -F middle -n 5 -v 2

#NTU-V1 temp, lstm no fusion
python3 src/run_protocol.py temp_rel_ave_lstm configs/NTU-V1/lstm/temp_rel_ave_lstm.cfg NTU -n 5 -t -v 2
python3 src/run_protocol.py temp_rel_att_lstm configs/NTU-V1/lstm/temp_rel_att_lstm.cfg NTU -n 5 -t -v 2
python3 src/run_protocol.py temp_no_rel_ave_lstm configs/NTU-V1/lstm/temp_no_rel_ave_lstm.cfg NTU -n 5 -t -v 2
python3 src/run_protocol.py temp_no_rel_att_lstm configs/NTU-V1/lstm/temp_no_rel_att_lstm.cfg NTU -n 5 -t -v 2

#NTU-V1 joint, lstm no fusion
python3 src/run_protocol.py joint_rel_ave_lstm configs/NTU-V1/lstm/joint_rel_ave_lstm.cfg NTU -n 5 -t -v 2
python3 src/run_protocol.py joint_rel_att_lstm configs/NTU-V1/lstm/joint_rel_att_lstm.cfg NTU -n 5 -t -v 2
python3 src/run_protocol.py joint_no_rel_ave_lstm configs/NTU-V1/lstm/joint_no_rel_ave_lstm.cfg NTU -n 5 -t -v 2
python3 src/run_protocol.py joint_no_rel_att_lstm configs/NTU-V1/lstm/joint_no_rel_att_lstm.cfg NTU -n 5 -t -v 2

# # NTU-V1 lstm fusion --run error
# python3 src/run_protocol.py ARN_rel_ave_before_lstm configs/NTU-V1/lstm/ARN_rel_ave_before_lstm.cfg NTU -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_rel_att_before_lstm configs/NTU-V1/lstm/ARN_rel_att_before_lstm.cfg NTU -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_no_rel_ave_before_lstm configs/NTU-V1/lstm/ARN_no_rel_ave_before_lstm.cfg NTU -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_no_rel_att_before_lstm configs/NTU-V1/lstm/ARN_no_rel_att_before_lstm.cfg NTU -t -F middle -n 5 -v 2

# python3 src/run_protocol.py ARN_rel_ave_after_lstm configs/NTU-V1/lstm/ARN_rel_ave_after_lstm.cfg NTU -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_rel_att_after_lstm configs/NTU-V1/lstm/ARN_rel_att_after_lstm.cfg NTU -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_no_rel_ave_after_lstm configs/NTU-V1/lstm/ARN_no_rel_ave_after_lstm.cfg NTU -t -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_no_rel_att_after_lstm configs/NTU-V1/lstm/ARN_no_rel_att_after_lstm.cfg NTU -t -F middle -n 5 -v 2


##NTU-v2 cs joint, temp, no lstm no two_stream
python3 src/run_protocol.py joint_rel_ave configs/NTU-V2/no-lstm/joint_rel_ave.cfg NTU-V2 -n 5 -v 2
python3 src/run_protocol.py joint_rel_att configs/NTU-V2/no-lstm/joint_rel_att.cfg NTU-V2 -n 5 -v 2
python3 src/run_protocol.py joint_no_rel_ave configs/NTU-V2/no-lstm/joint_no_rel_ave.cfg NTU-V2 -n 5 -v 2
python3 src/run_protocol.py joint_no_rel_att configs/NTU-V2/no-lstm/joint_no_rel_att.cfg NTU-V2 -n 5 -v 2

python3 src/run_protocol.py temp_rel_ave configs/NTU-V2/no-lstm/temp_rel_ave.cfg NTU-V2 -n 5 -v 2
python3 src/run_protocol.py temp_rel_att configs/NTU-V2/no-lstm/temp_rel_att.cfg NTU-V2 -n 5 -v 2
python3 src/run_protocol.py temp_no_rel_ave configs/NTU-V2/no-lstm/temp_no_rel_ave.cfg NTU-V2 -n 5 -v 2
python3 src/run_protocol.py temp_no_rel_att configs/NTU-V2/no-lstm/temp_no_rel_att.cfg NTU-V2 -n 5 -v 2


# NTU-V2 no lstm, fusion cross_subject and cross_setup
python3 src/run_protocol.py ARN_rel_ave_before configs/NTU-V2/no-lstm/ARN_rel_ave_before.cfg NTU-V2 -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_rel_att_before configs/NTU-V2/no-lstm/ARN_rel_att_before.cfg NTU-V2 -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_ave_before configs/NTU-V2/no-lstm/ARN_no_rel_ave_before.cfg NTU-V2 -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_att_before configs/NTU-V2/no-lstm/ARN_no_rel_att_before.cfg NTU-V2 -F middle -n 5 -v 2

python3 src/run_protocol.py ARN_rel_ave_after configs/NTU-V2/no-lstm/ARN_rel_ave_after.cfg NTU-V2 -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_rel_att_after configs/NTU-V2/no-lstm/ARN_rel_att_after.cfg NTU-V2 -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_ave_after configs/NTU-V2/no-lstm/ARN_no_rel_ave_after.cfg NTU-V2 -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_att_after configs/NTU-V2/no-lstm/ARN_no_rel_att_after.cfg NTU-V2 -F middle -n 5 -v 2

#NTU-V2 temp, lstm no fusion
python3 src/run_protocol.py temp_rel_ave_lstm configs/NTU-V2/lstm/temp_rel_ave_lstm.cfg NTU-V2 -n 5 -t -v 2

python3 src/run_protocol.py temp_rel_att_lstm configs/NTU-V2/lstm/temp_rel_att_lstm.cfg NTU-V2 -n 5 -t -v 2  #没跑完

python3 src/run_protocol.py temp_no_rel_ave_lstm configs/NTU-V2/lstm/temp_no_rel_ave_lstm.cfg NTU-V2 -n 5 -t -v 2
python3 src/run_protocol.py temp_no_rel_att_lstm configs/NTU-V2/lstm/temp_no_rel_att_lstm.cfg NTU -n 5 -t -v 2

#NTU-V2 joint, lstm no fusion
python3 src/run_protocol.py joint_rel_ave_lstm configs/NTU-V2/lstm/joint_rel_ave_lstm.cfg NTU-V2 -n 5 -t -v 2
python3 src/run_protocol.py joint_rel_att_lstm configs/NTU-V2/lstm/joint_rel_att_lstm.cfg NTU-V2 -n 5 -t -v 2
python3 src/run_protocol.py joint_no_rel_ave_lstm configs/NTU-V2/lstm/joint_no_rel_ave_lstm.cfg NTU-V2 -n 5 -t -v 2
python3 src/run_protocol.py joint_no_rel_att_lstm configs/NTU-V2/lstm/joint_no_rel_att_lstm.cfg NTU-V2 -n 5 -t -v 2

#NTU-V2 lstm fusion , fusion cross_subject and cross_setup
python3 src/run_protocol.py ARN_rel_ave_before_lstm configs/NTU-V2/lstm/ARN_rel_ave_before_lstm.cfg NTU-V2 -t -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_rel_att_before_lstm configs/NTU-V2/lstm/ARN_rel_att_before_lstm.cfg NTU-V2 -t -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_ave_before_lstm configs/NTU-V2/lstm/ARN_no_rel_ave_before_lstm.cfg NTU-V2  -t -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_att_before_lstm configs/NTU-V2/lstm/ARN_no_rel_att_before_lstm.cfg NTU-V2  -t -F middle -n 5 -v 2

python3 src/run_protocol.py ARN_rel_ave_after_lstm configs/NTU-V2/lstm/ARN_rel_ave_after_lstm.cfg NTU-V2 -t -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_rel_att_after_lstm configs/NTU-V2/lstm/ARN_rel_att_after_lstm.cfg NTU-V2 -t -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_ave_after_lstm configs/NTU-V2/lstm/ARN_no_rel_ave_after_lstm.cfg NTU-V2 -t -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_no_rel_att_after_lstm configs/NTU-V2/lstm/ARN_no_rel_att_after_lstm.cfg NTU-V2 -t -F middle -n 5 -v 2
