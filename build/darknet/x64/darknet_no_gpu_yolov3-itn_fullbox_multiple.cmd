@echo off
FOR /R "C:\darknet\build\darknet\x64\itn_fullbox\test_images" %%f IN (*.jpg) DO (
	darknet_no_gpu.exe detector test itn_fullbox\itn_fullbox.data itn_fullbox\yolov3-itn-fullbox.cfg "C:\Users\vanbinhd\Google Drive\backup\yolov3-itn-fullbox_4000.weights" %%f -save_labels -dont_show -outfile
	echo %%f
)
set /P DUMMY=Hit ENTER to exit..











