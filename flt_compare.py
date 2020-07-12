#!/usr/local/bin/python3
# author: zhShen
# date: 20190420
import numpy as np
import openfile as of
import diff
import draw as dw
import correct_base as cb
import matplotlib.pyplot as plt
import glv

t,t_ref,time=[],[],[]
pos,pos_ref,diff_pos=[],[],[]
vel,vel_ref,diff_vel=[],[],[]
bias,status,state_ref=[],[],[]


path = 'GNSS_INS20190614'
ref_file=path+'/GNSS_combined.txt'
flt_file=path+'/SEPT-GREC.flt'

[t,pos,vel,status]=of.open_flt_file(flt_file)
[t_ref,pos_ref,vel_ref,att_ref,state_ref]=of.open_IE_file(ref_file)

pos_ref=cb.correct_base(pos_ref,glv.div_ref[path],glv.plus_ref[path])

[time,diff_pos]=diff.diff_enu(t,pos,t_ref,pos_ref)
# [time,diff_vel]=diff.diff_vel(t,vel,t_ref,vel_ref)

dw.plot_pos(path+'/fig/pvt_pos',time,diff_pos)
# dw.plot_vel(time,diff_vel)

plt.show()
