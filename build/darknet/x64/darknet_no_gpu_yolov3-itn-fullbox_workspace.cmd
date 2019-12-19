echo off
SET input_name="C:\darknet\build\darknet\x64\workspace\capture.jpg"
SET output_name="C:\darknet\build\darknet\x64\workspace\capture.txt"
darknet_no_gpu.exe detector test itn_fullbox\itn_fullbox.data itn_fullbox\yolov3-itn-fullbox.cfg itn_fullbox\yolov3-itn-fullbox_last.weights %input_name% -save_labels -dont_show -outfile
python convert_results.py --inname %output_name%
# set /P DUMMY=Enter to exit...











