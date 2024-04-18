#!/bin/bash
#NTU-V1 joint, no lstm, no fusion
python3 src/run_protocol.py final_joint_rel_ave_v1 configs/NTU-V1/final/final_joint_rel_ave.cfg NTU -n 5 -v 2
python3 src/run_protocol.py final_joint_rel_att_v1 configs/NTU-V1/final/final_joint_rel_att.cfg NTU -n 5 -v 2

#NTU-V1 temp, lstm no fusion
python3 src/run_protocol.py final_temp_rel_ave_lstm_v1 configs/NTU-V1/final/lstm/final_temp_rel_ave_lstm.cfg NTU -n 5 -t -v 2
python3 src/run_protocol.py final_temp_rel_att_lstm_v1 configs/NTU-V1/final/lstm/final_temp_rel_att_lstm.cfg NTU -n 5 -t -v 2

#NTU-V1 lstm fusion
python3 src/run_protocol.py IRN_final_rel_ave_before_lstm_v1 configs/NTU-V1/final/lstm/IRN_final_rel_ave_before_lstm.cfg NTU -t -F middle -n 5 -v 2
python3 src/run_protocol.py IRN_final_rel_att_before_lstm_v1 configs/NTU-V1/final/lstm/IRN_final_rel_att_before_lstm.cfg NTU -t -F middle -n 5 -v 2
python3 src/run_protocol.py IRN_final_no_rel_ave_before_lstm_v1 configs/NTU-V1/final/lstm/IRN_final_no_rel_ave_before_lstm.cfg NTU -t -F middle -n 5 -v 2
python3 src/run_protocol.py IRN_final_no_rel_att_before_lstm_v1 configs/NTU-V1/final/lstm/IRN_final_no_rel_att_before_lstm.cfg NTU -t -F middle -n 5 -v 2

python3 src/run_protocol.py IRN_final_rel_ave_after_lstm_v1 configs/NTU-V1/final/lstm/IRN_final_rel_ave_after_lstm.cfg NTU -t -F middle -n 5 -v 2
python3 src/run_protocol.py IRN_final_rel_att_after_lstm_v1 configs/NTU-V1/final/lstm/IRN_final_rel_att_after_lstm.cfg NTU -t -F middle -n 5 -v 2
python3 src/run_protocol.py IRN_final_no_rel_ave_after_lstm_v1 configs/NTU-V1/final/lstm/IRN_final_no_rel_ave_after_lstm.cfg NTU -t -F middle -n 5 -v 2
python3 src/run_protocol.py IRN_final_no_rel_att_after_lstm_v1 configs/NTU-V1/final/lstm/IRN_final_no_rel_att_after_lstm.cfg NTU -t -F middle -n 5 -v 2


#NTU-v2 cs joint, temp, no lstm no two_stream
python3 src/run_protocol.py final_joint_rel_ave_cs configs/NTU-V2/final/final_joint_rel_ave.cfg NTU-V2 -n 5 -f cross_subject
python3 src/run_protocol.py final_joint_rel_ave_cv configs/NTU-V2/final/final_joint_rel_ave.cfg NTU-V2 -n 5 -f cross_view
python3 src/run_protocol.py final_joint_rel_att_cs configs/NTU-V2/final/final_joint_rel_att.cfg NTU-V2 -n 5 -f cross_subject
python3 src/run_protocol.py final_joint_rel_att_cv configs/NTU-V2/final/final_joint_rel_att.cfg NTU-V2 -n 5 -f cross_view
python3 src/run_protocol.py final_joint_no_rel_ave_cs configs/NTU-V2/final/final_joint_no_rel_ave.cfg NTU-V2 -n 5 -f cross_subject
python3 src/run_protocol.py final_joint_no_rel_ave_cv configs/NTU-V2/final/final_joint_no_rel_ave.cfg NTU-V2 -n 5 -f cross_view
python3 src/run_protocol.py final_joint_no_rel_att_cs configs/NTU-V2/final/final_joint_no_rel_att.cfg NTU-V2 -n 5 -f cross_subject
python3 src/run_protocol.py final_joint_no_rel_att_cv configs/NTU-V2/final/final_joint_no_rel_att.cfg NTU-V2 -n 5 -f cross_view

python3 src/run_protocol.py final_temp_rel_ave_cs configs/NTU-V2/final/final_temp_rel_ave.cfg NTU-V2 -n 5 -f cross_subject
python3 src/run_protocol.py final_temp_rel_ave_cv configs/NTU-V2/final/final_temp_rel_ave.cfg NTU-V2 -n 5 -f cross_view
python3 src/run_protocol.py final_temp_rel_att_cs configs/NTU-V2/final/final_temp_rel_att.cfg NTU-V2 -n 5 -f cross_subject
python3 src/run_protocol.py final_temp_rel_att_cv configs/NTU-V2/final/final_temp_rel_att.cfg NTU-V2 -n 5 -f cross_view
python3 src/run_protocol.py final_temp_no_rel_ave_cs configs/NTU-V2/final/final_temp_no_rel_ave.cfg NTU-V2 -n 5 -f cross_subject
python3 src/run_protocol.py final_temp_no_rel_ave_cv configs/NTU-V2/final/final_temp_no_rel_ave.cfg NTU-V2 -n 5 -f cross_view
python3 src/run_protocol.py final_temp_no_rel_att_cs configs/NTU-V2/final/final_temp_no_rel_att.cfg NTU-V2 -n 5 -f cross_subject
python3 src/run_protocol.py final_temp_no_rel_att_cv configs/NTU-V2/final/final_temp_no_rel_att.cfg NTU-V2 -n 5 -f cross_view
