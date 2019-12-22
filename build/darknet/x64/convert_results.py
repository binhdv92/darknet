# -*- coding: utf-8 -*-
from pandas import DataFrame, read_csv
from numpy import asarray
import argparse

# argument
parser=argparse.ArgumentParser(description='''convert_results.py --inname --sep it will convert the result of Yolov3 to tray ID base on boxs of bounding''')
parser.add_argument('-i','--inname',default='CameraSnapshot.txt')
parser.add_argument('-so','--sep_out',default=',')

args=parser.parse_args()
# print(args.__dict__)

outname ="Detection_out.txt"


# 
def center_to_bound(x,y,w,h):
    xmax=x+w/2
    xmin=x-w/2
    ymax=y+h/2
    ymin=y-h/2
    return(xmin,xmax,ymin,ymax)
    

def convert(df):
    df1=df[df['class']==10]
    df1.sort_values(by='y',inplace=True)
    df1.reset_index(inplace=True)
    
    df2=df[df['class']!=10]
    df2.reset_index()
    
    csvout=[]
    # csvout1=[]

    for i in range(len(df1)):
        box_xmin,box_xmax,box_ymin,box_ymax=center_to_bound(df1['x'][i],df1['y'][i],df1['w'][i],df1['h'][i])
        dftemp=df2[asarray(df2['x']>box_xmin)*asarray(df2['x']<box_xmax)*asarray(df2['y']>box_ymin)*asarray(df2['y']<box_ymax)]
        dftemp.sort_values(by=['x'],inplace=True)    
        result=list(dftemp['class'])
    
        resultstr=''
        for j in result:
            resultstr=resultstr+str(j)
        
        csvout.append(resultstr)
		
    dfout = DataFrame(csvout,columns=['trayid'])
                                          
    return(dfout)


df = read_csv(args.inname,sep=' ',header=None, names = ['class','x','y','w','h'])
dfout=convert(df)

dfout.to_csv(outname,sep=args.sep_out,index=False,header=None)