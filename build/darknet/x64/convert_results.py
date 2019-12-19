# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import argparse

# argument
parser=argparse.ArgumentParser(description='''convert_results.py --inname --sep it will convert the result of Yolov3 to tray ID base on boxs of bounding''')
parser.add_argument('-i','--inname',default='itn_fullbox/media/Capture.txt')
parser.add_argument('-s','--sep',default=',')

args=parser.parse_args()
print(args.__dict__)

outname1=f'{args.inname}.out1'
outname2=f'{args.inname}.out2'
print(f'outname1: {outname1}')
print(f'outname2: {outname2}')

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
    
    csvout1=[]
    csvout2=[]
    for i in range(len(df1)):
        box_xmin,box_xmax,box_ymin,box_ymax=center_to_bound(df1['x'][i],df1['y'][i],df1['w'][i],df1['h'][i])
        dftemp=df2[np.asarray(df2['x']>box_xmin)*np.asarray(df2['x']<box_xmax)*np.asarray(df2['y']>box_ymin)*np.asarray(df2['y']<box_ymax)]
        dftemp.sort_values(by=['x'],inplace=True)    
        result=list(dftemp['class'])
    
        resultstr=''
        for j in result:
            resultstr=resultstr+str(j)
        csvout1.append([resultstr,df1['x'][i],df1['y'][i],df1['w'][i],df1['h'][i],box_xmin,box_xmax,box_ymin,box_ymax])
        csvout2.append(resultstr)
    
    
    dfout1=pd.DataFrame(csvout1,columns=['trayid','x','y','w','h','box_xmin','box_xmax','box_ymin','box_ymax'])

    
    dfout2=pd.DataFrame(csvout2,columns=['trayid'])

    
    print(dfout1)                                               
    
    return(dfout1,dfout2)

df = pd.read_csv(args.inname,sep=' ',header=None, names = ['class','x','y','w','h']) 
dfout1,dfout2=convert(df)

dfout2.to_csv(outname2,sep=args.sep,index=False)
dfout1.to_csv(outname1,sep=args.sep,index=False)



    
        


