# -*- coding: utf-8 -*-
from darknet import performDetect

temp = performDetect(imagePath="C:/itn2/images/500091858_20191211_161410_523929.jpg", thresh= 0.5, configPath = "C:/itn/yolov3-itn.cfg", 
                     weightPath = "C:\\Users\\vanbinhd\\Google Drive\yolov3-itn_last.weights", metaPath= "C:/itn/itn.data", showImage= True, makeImageOnly = False, initOnly= False)
