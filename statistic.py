#!/usr/bin/python
# author: zhShen
# date: 20190520
import glv
from math import *
import numpy as np

def ratio(threshold1,threshold2,XYZ=[]):
    cnt=0
    for i in range(len(XYZ)):
        x=XYZ[i][0]
        y=XYZ[i][1]
        z=XYZ[i][2] 
        if abs(x)< threshold1 and abs(y)< threshold1 and abs(z)< threshold2:
            cnt=cnt+1
    # size=2314
    size=1084
    print("Ratio of three components < threshold: ", cnt/size)

