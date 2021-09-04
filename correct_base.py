#!/usr/bin/python
# author: zhShen
# date: 20200711
import numpy as np

def correct_base(xyz=[],div_ref=[],plus_ref=[]):
    x=xyz[:,0]-div_ref[0]+plus_ref[0]
    y=xyz[:,1]-div_ref[1]+plus_ref[1]
    z=xyz[:,2]-div_ref[2]+plus_ref[2]
    xyz_corrected=np.array([x,y,z]).T
    return xyz_corrected
