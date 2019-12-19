SET f="CameraSnapshot.jpg"
echo %f%
darknet_no_gpu.exe detector test itn_fullbox\itn_fullbox.data itn_fullbox\yolov3-itn-fullbox.cfg "itn_fullbox\yolov3-itn-fullbox_last.weights" %f% -save_labels -dont_show -outfile
# python convert_results.py --inname itn_fullbox/test_images/19_11_21_110038_Moment.txt
set /P DUMMY=Hit ENTER to exit..
