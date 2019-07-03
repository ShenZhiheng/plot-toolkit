#!/usr/bin/python
import Cen
import glv
import trans
import math
from numpy import *
import matplotlib.pyplot as plt


t_m,B,L,H=[],[],[],[]
Ve,Vn,Vu=[],[],[]
Pitch,Roll,Yaw=[],[],[]
count=0


t,Pax,Pay,Paz,Pve,Pvn,Pvu,Pb,Pl,Ph,Pebx,Peby,Pebz,Pdbx,Pdby,Pdbz=\
[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]

with open('HOLO20190625/kfpk.txt','rt') as f:
	for line in f:
		value=line.split();
		t.append(value[0]);
		Pax.append(math.sqrt(float(value[1])))
		Pay.append(math.sqrt(float(value[2])))
		Paz.append(math.sqrt(float(value[3])))
		Pve.append(math.sqrt(float(value[4])))
		Pvn.append(math.sqrt(float(value[5])))
		Pvu.append(math.sqrt(float(value[6])))
		Pb.append(math.sqrt(float(value[7])))
		Pl.append(math.sqrt(float(value[8])))
		Ph.append(math.sqrt(float(value[9])))
	

with open('HOLO20190625/lci.ins','rt') as f:
	for line in f:
		if count==0 or count==1:
			count=count+1
			continue
		value=line.split()
		t_m.append(float(value[0]))
		B.append(float(value[1]));
		L.append(float(value[2]));
		H.append(float(value[3]));
		Ve.append(float(value[7]));
		Vn.append(float(value[8]));
		Vu.append(float(value[9]));
		Pitch.append(float(value[4]))
		Roll.append(float(value[5]))
		Yaw.append(-float(value[6]))


for i in range(len(t)):

	sb = math.sin(B[i])
	sq = 1 - glv.e2*sb*sb
	sq2 = math.sqrt(sq)
	RM = glv.a*(1 - glv.e2) / sq / sq2
	RN = glv.a / sq2

	Pb[i]=float(Pb[i]*RM)
	Pl[i]=float(Pl[i]*RN)
	Pax[i]=float(Pax[i]/glv.deg)
	Pay[i]=float(Pay[i]/glv.deg)
	Paz[i]=float(Paz[i]/glv.deg)


with open('HOLO20190625/odo.ins','wt') as f:
	s='gps_week,gps_sec,latitude,longitude,altitude,roll,pitch,yaw,Ve,Vn,Vu,x_std,y_std,z_std,roll_std,pitch_std,yaw_std,Ve_std,Vn_std,Vu_std'
	f.writelines(s+'\n')
	for i in range(len(t)):

		s='{0:.4f},{1:.6f},{2:.6f},{3:.4f},{4:.3f},{5:.3f},{6:.3f},{7:.3f},{8:.3f},{9:.3f} '\
		.format(float(t[i]),float(B[i]),float(L[i]),float(H[i]),float(Roll[i]),float(Pitch[i]),float(Yaw[i]),float(Ve[i]),float(Vn[i]),float(Vu[i]))

		s='2059,'+s

		f.writelines(s)

		s='{0:.6f},{1:.6f},{2:.4f},{3:.4f},{4:.4f},{5:.4f},{6:.4f},{7:.4f},{8:.4f}  '\
		.format(float(Pb[i]),float(Pl[i]),float(Ph[i]),float(Pay[i]),float(Pax[i]),float(Paz[i]),float(Pve[i]),float(Pvn[i]),float(Pvu[i]))

		f.writelines(s+'\n')





