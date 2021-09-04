#!/usr/local/bin/python3
# author: zhShen
# date: 20200711
import numpy as np
import openfile as of
import diff
import draw as dw
import matplotlib.pyplot as plt
import glv
import trans

t,t_ref,time=[],[],[]
pos,pos_ref,diff_pos=[],[],[]
vel,vel_ref,diff_vel=[],[],[]
att,att_ref,diff_att=[],[],[]
bias,state_ref=[],[]

path = 'GNSS_INS20201216'
path = 'GNSS_INS_VISION20201029'
ins_file=path+'/SEPT-LCI1.ins'
# ins_file=path+'/SIM/SEPT-TCI-F_Gap30.ins'
# ins_file=path+'/SIM/SEPT-TCI-F_Gap60.ins'
# ins_file=path+'/SIM/SEPT-TCI-F_Gap90.ins'

# ins_file=path+'/SIM/SEPT-TCI-WAR_Gap10.ins'
# ins_file=path+'/SIM/SEPT-TCI-WAR_Gap30.ins'
# ins_file=path+'/SIM/SEPT-TCI-WAR_Gap60.ins'
# ins_file=path+'/SIM/SEPT-TCI-WAR_Gap90.ins'
# ins_file=path+'/INS1/SEPT-TCI-WAR1.ins'

# path = 'GNSS_INS_VISION20201029'
# ref_file=path+'/SEPT-rtk_client.pos' 
# ref_file=path+'/TC_smooth_combined1.txt'

ref_file=path+'/TC_smooth_combined1.txt'
# ref_file=path+'/TC_smooth_combined1.txt'
# ins_file=path+'/great-RTK-LCI-Seraug-2.ins'

[t,pos,vel,att,bias]=of.open_ins_file(ins_file)
[t_ref,pos_ref,vel_ref,att_ref,state_ref]=of.open_IE_file(ref_file)

# for i in range(len(vel_ref)):
#     [X,Y,Z]=pos_ref[i]
#     [B,L,H]=trans.xyz2blh(X,Y,Z)
#     C=trans.Cnb(att_ref[i][0]*glv.deg,att_ref[i][1]*glv.deg,-att_ref[i][2]*glv.deg)
#     C1=trans.Cne(B,L).transpose()
#     vb=((C1*C).transpose())*(np.matrix(vel_ref[i]).transpose())
#     print(t_ref[i],float(vb[0]),float(vb[1]),float(vb[2]))




pos_ref=diff.correct_base(pos_ref,glv.div_ref[path],glv.plus_ref[path])

# print(t)
# print(t_ref)
[time,diff_pos]=diff.diff_enu(t,pos,t_ref,pos_ref)
# print(time)
dw.plot_pos(ins_file,time,diff_pos)
# print(diff.available(0.5,diff_pos))

# [time,diff_vel]=diff.diff_vel(t,vel,t_ref,vel_ref)
# dw.plot_vel(path+'/fig/ppp-tci-vel',t,vel)

[time,diff_att]=diff.diff_att(t,att,t_ref,att_ref)
dw.plot_att(path+'/fig/ppp-tci-vel',time,diff_att)
# print(diff_pos)

# Available

# Plot
dw.plot_bias(path+'/fig/bias',t,bias)
# dw.plot_hrzn_trj(path+'/fig/trj',t,pos)

plt.show()
