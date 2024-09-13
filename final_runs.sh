#!/bin/bash
# nohup bash final_runs.sh > final_runs.log 2>&1&  #服务器后台运行，log保存至 final_runs.log中

### baseline ###
# # SBU
# # RN_joints
# python3 src/run_protocol.py RN_joint configs/SBU/no-lstm/RN_joint.cfg SBU -n 5 -v 2
# # RN_temp
# python3 src/run_protocol.py RN_temp configs/SBU/no-lstm/RN_temp.cfg SBU -n 5 -v 2
# # RN_joint+temp (RN_two_stream)
# python3 src/run_protocol.py RN_joint+temp configs/SBU/no-lstm/RN_joint+temp.cfg SBU -F middle -n 5 -v 2 

# # UT
# # RN_joints
# python3 src/run_protocol.py RN_joint configs/UT/set_1/RN_joint.cfg UT-1 -n 5 -v 2
# python3 src/run_protocol.py RN_joint configs/UT/set_2/RN_joint.cfg UT-2 -n 5 -v 2
# # RN_temp
# python3 src/run_protocol.py RN_temp configs/UT/set_1/RN_temp.cfg UT-1 -n 5 -v 2
# python3 src/run_protocol.py RN_temp configs/UT/set_2/RN_temp.cfg UT-2 -n 5 -v 2
# # RN_joint+temp (RN_two_stream)
# python3 src/run_protocol.py RN_joint+temp configs/UT/set_1/RN_joint+temp.cfg UT-1 -F middle -n 5 -v 2
# python3 src/run_protocol.py RN_joint+temp configs/UT/set_2/RN_joint+temp.cfg UT-2 -F middle -n 5 -v 2

# NTU-V1/V2
# RN_joints
python3 src/run_protocol.py RN_joint configs/NTU-V1/no-lstm/RN_joint.cfg NTU -n 5 -v 2
python3 src/run_protocol.py RN_joint configs/NTU-V2/no-lstm/RN_joint.cfg NTU-V2 -n 1 -v 2
# RN_temp
python3 src/run_protocol.py RN_temp configs/NTU-V1/no-lstm/RN_temp.cfg NTU -n 5 -v 2
python3 src/run_protocol.py RN_temp configs/NTU-V2/no-lstm/RN_temp.cfg NTU-V2 -n 5 -v 2
# RN_joint+temp (RN_two_stream)
python3 src/run_protocol.py RN_joint+temp configs/NTU-V1/no-lstm/RN_joint+temp.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py RN_joint+temp configs/NTU-V2/no-lstm/RN_joint+temp.cfg NTU-V2 -F middle -n 5 -v 2 

## Chapter 4
# # SBU
# # ARN_joint
# python3 src/run_protocol.py ARN_joint configs/SBU/no-lstm/ARN_joint.cfg SBU -n 5 -v 2
# # ARN_temp
# python3 src/run_protocol.py ARN_temp configs/SBU/no-lstm/ARN_temp.cfg SBU -n 5 -v 2
# # ARN_joint+temp
# python3 src/run_protocol.py ARN_joint+temp configs/SBU/no-lstm/ARN_joint+temp.cfg SBU -F middle -n 5 -v 2
# # ARN-fc1_joint+temp
# python3 src/run_protocol.py ARN-fc1_joint+temp configs/SBU/no-lstm/ARN-fc1_joint+temp.cfg SBU -F middle -n 5 -v 2

# # UT
# # ARN_joints
# python3 src/run_protocol.py ARN_joint configs/UT/set_1/ARN_joint.cfg UT-1 -n 5 -v 2
# python3 src/run_protocol.py ARN_joint configs/UT/set_2/ARN_joint.cfg UT-2 -n 5 -v 2
# # ARN_temp
# python3 src/run_protocol.py ARN_temp configs/UT/set_1/ARN_temp.cfg UT-1 -n 5 -v 2
# python3 src/run_protocol.py ARN_temp configs/UT/set_2/ARN_temp.cfg UT-2 -n 5 -v 2
# # ARN_joint+temp (ARN_two_stream)
# python3 src/run_protocol.py ARN_joint+temp configs/UT/set_1/ARN_joint+temp.cfg UT-1 -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_joint+temp configs/UT/set_2/ARN_joint+temp.cfg UT-2 -F middle -n 5 -v 2
# # ARN-fc1_joint+temp
# python3 src/run_protocol.py ARN-fc1_joint+temp configs/UT/set_1/ARN-fc1_joint+temp.cfg UT-1 -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN-fc1_joint+temp configs/UT/set_2/ARN-fc1_joint+temp.cfg UT-2 -F middle -n 5 -v 2

# NTU-V1/V2
# ARN_joint
python3 src/run_protocol.py ARN_joint configs/NTU-V1/no-lstm/ARN_joint.cfg NTU -n 5 -v 2
python3 src/run_protocol.py ARN_joint configs/NTU-V2/no-lstm/ARN_joint.cfg NTU-V2 -n 5 -v 2
# ARN_temp
python3 src/run_protocol.py ARN_temp configs/NTU-V1/no-lstm/ARN_temp.cfg NTU -n 5 -v 2
python3 src/run_protocol.py ARN_temp configs/NTU-V2/no-lstm/ARN_temp.cfg NTU-V2 -n 5 -v 2
# ARN_joint+temp
python3 src/run_protocol.py ARN_joint+temp configs/NTU-V1/no-lstm/ARN_joint+temp.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_joint+temp configs/NTU-V2/no-lstm/ARN_joint+temp.cfg NTU-V2 -F middle -n 5 -v 2
# ARN-fc1_joint+temp
python3 src/run_protocol.py ARN-fc1_joint+temp configs/NTU-V1/no-lstm/ARN-fc1_joint+temp.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN-fc1_joint+temp configs/NTU-V2/no-lstm/ARN-fc1_joint+temp.cfg NTU-V2 -F middle -n 5 -v 2

## Chapter 5
# # SBU
# # ARN_inward compute_distance = false compute_motion = false
# python3 src/run_protocol.py ARN_inward_no_motion configs/SBU/ARN_inward_no_motion.cfg SBU -n 5 -v 2
# # ARN_outward compute_distance = false compute_motion = false
# python3 src/run_protocol.py ARN_outward_no_motion configs/SBU/ARN_outward_no_motion.cfg SBU -n 5 -v 2
# # ARN_inward+outward compute_distance = false compute_motion = false
# python3 src/run_protocol.py ARN_inward+outward_no_motion configs/SBU/ARN_inward+outward_no_motion.cfg SBU -F middle -n 5 -v 2

# # ARN_inward compute_distance = True compute_motion = True
# python3 src/run_protocol.py ARN_inward configs/SBU/ARN_inward.cfg SBU -n 5 -v 2
# # ARN_outward compute_distance = True compute_motion = True
# python3 src/run_protocol.py ARN_outward configs/SBU/ARN_outward.cfg SBU -n 5 -v 2
# # ARN_inward+outward compute_distance = True compute_motion = True
# python3 src/run_protocol.py ARN_inward+outward configs/SBU/ARN_inward+outward.cfg SBU -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN-fc1_inward+outward configs/SBU/ARN-fc1_inward+outward.cfg SBU -F middle -n 5 -v 2

# # UT
# # ARN_inward compute_distance = false compute_motion = false
# python3 src/run_protocol.py ARN_inward_no_motion configs/UT/set_1/ARN_inward_no_motion.cfg UT-1 -n 5 -v 2
# python3 src/run_protocol.py ARN_inward_no_motion configs/UT/set_2/ARN_inward_no_motion.cfg UT-2 -n 5 -v 2
# # ARN_outward compute_distance = false compute_motion = false
# python3 src/run_protocol.py ARN_outward_no_motion configs/UT/set_1/ARN_outward_no_motion.cfg UT-1 -n 5 -v 2
# python3 src/run_protocol.py ARN_outward_no_motion configs/UT/set_2/ARN_outward_no_motion.cfg UT-2 -n 5 -v 2
# # ARN_inward+outward compute_distance = false compute_motion = false
# python3 src/run_protocol.py ARN_inward+outward_no_motion configs/UT/set_1/ARN_inward+outward_no_motion.cfg UT-1 -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_inward+outward_no_motion configs/UT/set_2/ARN_inward+outward_no_motion.cfg UT-2 -F middle -n 5 -v 2

# # ARN_inward compute_distance = True compute_motion = True
# python3 src/run_protocol.py ARN_inward configs/UT/set_1/ARN_inward.cfg UT-1 -n 5 -v 2
# python3 src/run_protocol.py ARN_inward configs/UT/set_2/ARN_inward.cfg UT-2 -n 5 -v 2
# # ARN_outward compute_distance = True compute_motion = True
# python3 src/run_protocol.py ARN_outward configs/UT/set_1/ARN_outward.cfg UT-1 -n 5 -v 2
# python3 src/run_protocol.py ARN_outward configs/UT/set_2/ARN_outward.cfg UT-2 -n 5 -v 2 
# # ARN_inward+outward compute_distance = True compute_motion = True
# python3 src/run_protocol.py ARN_inward+outward configs/UT/set_1/ARN_inward+outward.cfg UT-1 -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN_inward+outward configs/UT/set_2/ARN_inward+outward.cfg UT-2 -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN-fc1_inward+outward configs/UT/set_1/ARN-fc1_inward+outward.cfg UT-1 -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN-fc1_inward+outward configs/UT/set_2/ARN-fc1_inward+outward.cfg UT-2 -F middle -n 5 -v 2

#NTU-V1/V2
# ARN_inward compute_distance = false compute_motion = false
python3 src/run_protocol.py ARN_inward_no_motion configs/NTU-V1/ARN_inward_no_motion.cfg NTU -n 5 -v 2
python3 src/run_protocol.py ARN_inward_no_motion configs/NTU-V2/ARN_inward_no_motion.cfg NTU-V2 -n 5 -v 2
# ARN_outward compute_distance = false compute_motion = false
python3 src/run_protocol.py ARN_outward_no_motion configs/NTU-V1/ARN_outward_no_motion.cfg NTU -n 5 -v 2
python3 src/run_protocol.py ARN_outward_no_motion configs/NTU-V2/ARN_outward_no_motion.cfg NTU-V2 -n 5 -v 2
# ARN_inward+outward compute_distance = false compute_motion = false
python3 src/run_protocol.py ARN_inward+outward_no_motion configs/NTU-V1/ARN_inward+outward_no_motion.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_inward+outward_no_motion configs/NTU-V2/ARN_inward+outward_no_motion.cfg NTU-V2 -F middle -n 5 -v 2

# ARN_inward compute_distance = True compute_motion = True
python3 src/run_protocol.py ARN_inward configs/NTU-V1/ARN_inward.cfg NTU -n 5 -v 2
python3 src/run_protocol.py ARN_inward configs/NTU-V2/ARN_inward.cfg NTU-V2 -n 5 -v 2 # x
# ARN_outward compute_distance = True compute_motion = True
python3 src/run_protocol.py ARN_outward configs/NTU-V1/ARN_outward.cfg NTU -n 5 -v 2
python3 src/run_protocol.py ARN_outward configs/NTU-V2/ARN_outward.cfg NTU-V2 -n 5 -v 2 # x
# ARN_inward+outward compute_distance = True compute_motion = True
python3 src/run_protocol.py ARN_inward+outward configs/NTU-V1/ARN_inward+outward.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN_inward+outward configs/NTU-V2/ARN_inward+outward.cfg NTU-V2 -F middle -n 5 -v 2 # x
python3 src/run_protocol.py ARN-fc1_inward+outward configs/NTU-V1/ARN-fc1_inward+outward.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN-fc1_inward+outward configs/NTU-V2/ARN-fc1_inward+outward.cfg NTU-V2 -F middle -n 5 -v 2 # x

## Chapter 6
# # SBU
# # ARN-LSTM fusion inward+outward
# python3 src/run_protocol.py ARN-LSTM_inward configs/SBU/ARN-LSTM_inward.cfg SBU -n 5 -v 2
# python3 src/run_protocol.py ARN-LSTM_outward configs/SBU/ARN-LSTM_outward.cfg SBU -n 5 -v 2
# python3 src/run_protocol.py ARN-LSTM_inward+outward configs/SBU/ARN-LSTM_inward+outward.cfg SBU -F middle -n 5 -v 2
# python3 src/run_protocol.py ARN-LSTM-fc1_inward+outward configs/SBU/ARN-LSTM-fc1_inward+outward.cfg SBU -F middle -n 5 

# # UT
# # # ARN-LSTM fusion inward+outward
# python3 src/run_protocol.py ARN-LSTM_inward configs/UT/set_1/ARN-LSTM_inward.cfg UT-1 -n 5 -v 2
# python3 src/run_protocol.py ARN-LSTM_outward configs/UT/set_1/ARN-LSTM_outward.cfg UT-1 -n 5 -v 2
# python3 src/run_protocol.py ARN-LSTM_inward+outward configs/UT/set_1/ARN-LSTM_inward+outward.cfg UT-1 -F middle -v 2 -n 5
# python3 src/run_protocol.py ARN-LSTM-fc1_inward+outward configs/UT/set_1/ARN-LSTM-fc1_inward+outward.cfg UT-1 -F middle -v 2 -n 5

# python3 src/run_protocol.py ARN-LSTM_inward configs/UT/set_2/ARN-LSTM_inward.cfg UT-2 -n 5 -v 2
# python3 src/run_protocol.py ARN-LSTM_outward configs/UT/set_2/ARN-LSTM_outward.cfg UT-2 -n 5 -v 2
# python3 src/run_protocol.py ARN-LSTM_inward+outward configs/UT/set_2/ARN-LSTM_inward+outward.cfg UT-2 -F middle -v 2 -n 5
# python3 src/run_protocol.py ARN-LSTM-fc1_inward+outward configs/UT/set_2/ARN-LSTM-fc1_inward+outward.cfg UT-2 -F middle -v 2 -n 5

# NTU-V1
# NTU-V1 ARN-LSTM fusion inward+outward
python3 src/run_protocol.py ARN-LSTM_inward configs/NTU-V1/ARN-LSTM_inward.cfg NTU -n 5 -v 2
python3 src/run_protocol.py ARN-LSTM_outward configs/NTU-V1/ARN-LSTM_outward.cfg NTU -n 5 -v 2
python3 src/run_protocol.py ARN-LSTM_inward+outward configs/NTU-V1/ARN-LSTM_inward+outward.cfg NTU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN-LSTM-fc1_inward+outward configs/NTU-V1/ARN-LSTM-fc1_inward+outward.cfg NTU -F middle -n 5 -v 2

# NTU-V2
# NTU-V2 ARN-LSTM fusion inward+outward
python3 src/run_protocol.py ARN-LSTM_inward configs/NTU-V2/ARN-LSTM_inward.cfg NTU-V2 -n 5 -v 2
python3 src/run_protocol.py ARN-LSTM_outward configs/NTU-V2/ARN-LSTM_outward.cfg NTU-V2 -n 5 -v 2
python3 src/run_protocol.py ARN-LSTM_inward+outward configs/NTU-V2/ARN-LSTM_inward+outward.cfg NTU-V2 -F middle -n 5 -v 2
python3 src/run_protocol.py ARN-LSTM-fc1_inward+outward configs/NTU-V2/ARN-LSTM-fc1_inward+outward.cfg NTU-V2 -F middle -n 5 -v 2



