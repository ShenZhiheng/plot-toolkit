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
att,att_ref,diff_att=[],[],[]
bias,state_ref=[],[]

path = 'GNSS_INS20190614'
# path = 'simulate'
# ref_file=path+'/ground-truth.ins'
# ref_file=path+'/TC_combined_smoothed.txt'
ref_file=path+'/TC_smooth_combined1.txt'
ins_file=path+'/great-TCI-6.ins'

[t,pos,vel,att,bias]=of.open_ins_file(ins_file)
[t_ref,pos_ref,vel_ref,att_ref,state_ref]=of.open_IE_file(ref_file)

pos_ref=diff.correct_base(pos_ref,glv.div_ref[path],glv.plus_ref[path])

[time,diff_pos]=diff.diff_enu(t,pos,t_ref,pos_ref)
[time,diff_vel]=diff.diff_vel(t,vel,t_ref,vel_ref)
[time,diff_att]=diff.diff_att(t,att,t_ref,att_ref)
# print(diff_pos)

# Available
print(diff.available(0.5,diff_pos))

# Plot
dw.plot_pos(path+'/fig/ppp-tci-pos',time,diff_pos)
dw.plot_vel(path+'/fig/ppp-tci-vel',time,diff_vel)
dw.plot_att(path+'/fig/ppp-tci-att',time,diff_att)
dw.plot_bias(path+'/fig/bias',t,bias)
# dw.plot_trj(path+'/fig/trj',t,pos)

plt.show()
