#!/usr/local/bin/python3
# author: zhShen
# date: 20200711
import numpy as np
import openfile as of
import diff
import draw as dw
import matplotlib.pyplot as plt
import glv

t,t_ref,time=[],[],[]
pos,pos_ref,diff_pos=[],[],[]
vel,vel_ref,diff_vel=[],[],[]
bias,status,state_ref=[],[],[]

path = 'GNSS_INS20190716'
ref_file=path+'/GNSS_combined.txt'
flt_file=path+'/SEPT-GC-RTK.flt'

[t,pos,vel,status,pct]=of.open_flt_file(flt_file)
[t_ref,pos_ref,vel_ref,att_ref,state_ref]=of.open_IE_file(ref_file)

dw.plot_sat_pdop(path+'/fig/pdop',t,status)

# pct='{0:.3f}%'.format(pct*100)
# print('fixed percent: ',pct)

# pos_ref=diff.correct_base(pos_ref,glv.div_ref[path],glv.plus_ref[path])

# [time,diff_pos]=diff.diff_enu(t,pos,t_ref,pos_ref)
# [time,diff_vel]=diff.diff_vel(t,vel,t_ref,vel_ref)
# print(diff.available(0.1,diff_pos))

# dw.plot_pos(path+'/fig/rtk_pos',time,diff_pos)
# # dw.plot_vel(path+'/fig/ppp_vel',time,diff_vel)

plt.show()
