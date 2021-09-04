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
status1=[]

path = 'GNSS_INS20201216'
# path = 'GNSS_INS_VISION20200918'
path = 'GNSS_INS_VISION20201029'
# flt_file=path+'/PVT/SEPT-urtk_c1216(1).pos'
flt_file=path+'/SEPT-GREC-PTK-Seraug-2.flt'
# flt_file=path+'/SIM/SEPT-GEC-WAR_Gap90.flt'
# flt_file=path+'/PVT/SEPT-urtk_c1216-C2.pos'
# ref_file=path+'/PVT/SEPT-GEC-RTK-RT.flt'
ref_file=path+'/TC_Combined_Smoothed_toGNSS01.txt'
# ref_file=path+'/GNSS_combined.txt'
# gpgga=path+'/True_sbg_output-2020-07-31-GGA.txt'

# Open File
[t,pos,vel,status,pct]=of.open_flt_file(flt_file,True)
# [t,pos,status]=of.open_ppprtk_file(flt_file)
# [t_ref,pos_ref,status1] = of.open_pos_file(posfile)
# [t,pos,status] = of.open_enu_file(flt_file)
# [t_ref,pos_ref,vel_ref,status_ref,pct_ref]=of.open_flt_file(ref_file,True)
# [t,pos,vel,att,bias]=of.open_ins_file(flt_file)
# [t_ref,pos_ref,status1] = of.open_gpgga_file(gpgga)
[t_ref,pos_ref,vel_ref,att_ref,state_ref]=of.open_IE_file(ref_file)
# dw.plot_sat_pdop(flt_file,t,status)
# print(t)
# print(t_ref)

# pct='{0:.3f}%'.format(pct*100)
# print('fixed percent: ',pct)

pos_ref=diff.correct_base(pos_ref,glv.div_ref[path],glv.plus_ref[path])
# pos_ref=diff.correct_base(pos_ref,glv.plus_ref['beijing'],glv.div_ref['beijing'])


# Diff
[time,diff_pos]=diff.diff_enu(t,pos,t_ref,pos_ref)
# [time,diff_vel]=diff.diff_vel(t,vel,t_ref,vel_ref)
# print(diff.available(0.5,diff_pos))


# Plot
dw.plot_pos(flt_file,time,diff_pos)
# dw.plot_vel(path+'/fig/ppp_vel',t_ref,vel_ref)
# dw.plot_trj(path+'/fig/trj',t,pos)
# dw.plot_hrzn_trj(path+'/fig/trj',t,pos)
# dw.plot_hrzn_trj(pos_ref,pos)

plt.show()
