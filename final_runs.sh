#!/bin/bash
# nohup bash final_runs.sh > final_runs.log 2>&1&  #服务器后台运行，log保存至 final_runs.log中

# SBU
# ARN-LSTM fusion inward+outward
python3 src/run_protocol.py ARN-LSTM_inward configs/SBU/ARN-LSTM_inward.cfg SBU -n 5 -v 2
python3 src/run_protocol.py ARN-LSTM_outward configs/SBU/ARN-LSTM_outward.cfg SBU -n 5 -v 2
python3 src/run_protocol.py ARN-LSTM_inward+outward configs/SBU/ARN-LSTM_inward+outward.cfg SBU -F middle -n 5 -v 2
python3 src/run_protocol.py ARN-LSTM-fc1_inward+outward configs/SBU/ARN-LSTM-fc1_inward+outward.cfg SBU -F middle -n 5 

# UT
# # ARN-LSTM fusion inward+outward
python3 src/run_protocol.py ARN-LSTM_inward configs/UT/set_1/ARN-LSTM_inward.cfg UT-1 -n 5 -v 2
python3 src/run_protocol.py ARN-LSTM_outward configs/UT/set_1/ARN-LSTM_outward.cfg UT-1 -n 5 -v 2
python3 src/run_protocol.py ARN-LSTM_inward+outward configs/UT/set_1/ARN-LSTM_inward+outward.cfg UT-1 -F middle -v 2 -n 5 # x
python3 src/run_protocol.py ARN-LSTM-fc1_inward+outward configs/UT/set_1/ARN-LSTM-fc1_inward+outward.cfg UT-1 -F middle -v 2 -n 5

python3 src/run_protocol.py ARN-LSTM_inward configs/UT/set_2/ARN-LSTM_inward.cfg UT-2 -n 5 -v 2
python3 src/run_protocol.py ARN-LSTM_outward configs/UT/set_2/ARN-LSTM_outward.cfg UT-2 -n 5 -v 2
python3 src/run_protocol.py ARN-LSTM_inward+outward configs/UT/set_2/ARN-LSTM_inward+outward.cfg UT-2 -F middle -v 2 -n 5
python3 src/run_protocol.py ARN-LSTM-fc1_inward+outward configs/UT/set_2/ARN-LSTM-fc1_inward+outward.cfg UT-2 -F middle -v 2 -n 5

# NTU-V1
# NTU-V1 ARN-LSTM fusion inward+outward
python3 src/run_protocol.py ARN-LSTM_inward configs/NTU-V1/ARN-LSTM_inward.cfg NTU -n 1 -v 2
python3 src/run_protocol.py ARN-LSTM_outward configs/NTU-V1/ARN-LSTM_outward.cfg NTU -n 1 -v 2
python3 src/run_protocol.py ARN-LSTM_inward+outward configs/NTU-V1/ARN-LSTM_inward+outward.cfg NTU -F middle -n 1 -v 2
python3 src/run_protocol.py ARN-LSTM-fc1_inward+outward configs/NTU-V1/ARN-LSTM-fc1_inward+outward.cfg NTU -F middle -n 1 -v 2

# NTU-V2
# NTU-V2 ARN-LSTM fusion inward+outward
python3 src/run_protocol.py ARN-LSTM_inward configs/NTU-V2/ARN-LSTM_inward.cfg NTU-V2 -n 1 -v 2
python3 src/run_protocol.py ARN-LSTM_outward configs/NTU-V2/ARN-LSTM_outward.cfg NTU-V2 -n 1 -v 2
python3 src/run_protocol.py ARN-LSTM_inward+outward configs/NTU-V2/ARN-LSTM_inward+outward.cfg NTU-V2 -F middle -n 1 -v 2
python3 src/run_protocol.py ARN-LSTM-fc1_inward+outward configs/NTU-V2/ARN-LSTM-fc1_inward+outward.cfg NTU-V2 -F middle -n 1 -v 2



