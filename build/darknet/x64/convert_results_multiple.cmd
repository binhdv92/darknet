FOR /R "C:\darknet\build\darknet\x64\itn_fullbox\test_images" %%f IN (*.txt) DO (
	echo %%f
	python convert_results.py --inname %%f
)
set /P DUMMY=Hit ENTER to exit..