#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import Bound as bd
import trans
import glv

t_ie,X_ie,Y_ie,Z_ie=[],[],[],[]
t_m,X_m,Y_m,Z_m=[],[],[],[]

Vx_ie,Vy_ie,Vz_ie,Vx_m,Vy_m,Vz_m=[],[],[],[],[],[]
Sig_x,Sig_y,Sig_z,Sig_Vx,Sig_Vy,Sig_Vz=[],[],[],[],[],[]
t,X_err,Y_err,Z_err,VX_err,VY_err,VZ_err=[],[],[],[],[],[],[]
X_sum,Y_sum,Z_sum,VX_sum,VY_sum,VZ_sum=0.0,0.0,0.0,0.0,0.0,0.0

with open('FSAS20190113/WLC20190113.trj','rt') as f:
	for line in f:
		value=line.split()
		t_ie.append(float(value[0]));
		[x,y,z]=[float(value[1]),float(value[2]),float(value[3])]
		# [x,y,z]=trans.blh2xyz(float(value[18])*glv.deg,float(value[19])*glv.deg,float(value[20]))
		X_ie.append(x);
		Y_ie.append(y);
		Z_ie.append(z);
		Vx_ie.append(float(value[4]));
		Vy_ie.append(float(value[5]));
		Vz_ie.append(float(value[6]));

with open('FSAS20190113/FSAS-GR-1.flt','rt') as f:
	for line in f:
		value=line.split()
		t_m.append(float(value[0]));
		X_m.append(float(value[1]));
		Y_m.append(float(value[2]));
		Z_m.append(float(value[3]));
		Vx_m.append(float(value[4]));
		Vy_m.append(float(value[5]));
		Vz_m.append(float(value[6]));

for i in range(len(t_m)):
	index=bd.lower_bound(t_ie,t_m[i]);
	if index==len(t_ie)-1:
		break;
	if abs(t_m[i]-t_ie[index])>1e-8:
		continue;
	t.append(t_m[i]);
	X_err.append(X_m[i]-X_ie[index])
	Y_err.append(Y_m[i]-Y_ie[index])
	Z_err.append(Z_m[i]-Z_ie[index])
	VX_err.append(Vx_m[i]-Vx_ie[index])
	VY_err.append(Vy_m[i]-Vy_ie[index])
	VZ_err.append(Vz_m[i]-Vz_ie[index])

for i in range(len(t)):
	X_sum=X_sum+abs(X_err[i]);
	Y_sum=Y_sum+abs(Y_err[i]);
	Z_sum=Z_sum+abs(Z_err[i]);
	VX_sum=VX_sum+abs(VX_err[i]);
	VY_sum=VY_sum+abs(VY_err[i]);
	VZ_sum=VZ_sum+abs(VZ_err[i]);

X_sum=X_sum/len(t);
Y_sum=Y_sum/len(t);
Z_sum=Z_sum/len(t);
VX_sum=VX_sum/len(t);
VY_sum=VY_sum/len(t);
VZ_sum=VZ_sum/len(t);

print X_sum,Y_sum,Z_sum,VX_sum,VY_sum,VZ_sum


plt.plot(t,X_err,linewidth=10,color='red');
plt.hold('on')
plt.plot(t,Y_err,linewidth=10,color='green');
plt.plot(t,Z_err,linewidth=10,color='blue');
plt.title('Position error',color='black',fontsize=40)
plt.grid(ls='-')
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel('Seconds of Week/(s)',fontsize=35)
plt.ylabel('Position error/(m)',fontsize=35)
plt.legend(['X','Y','Z'],fontsize=30);

plt.figure()
plt.plot(t,VX_err,linewidth=10);
plt.hold('on')
plt.plot(t,VY_err,linewidth=10);
plt.plot(t,VZ_err,linewidth=10);
plt.title('Velocity error',color='black',fontsize=40)
plt.grid(ls='-')
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.ylim(-2,2)
plt.xlabel('Seconds of Week/(s)',fontsize=35)
plt.ylabel('Velocity error/(m/s)',fontsize=35)
plt.legend(['Vx','Vy','Vz'],fontsize=30);


plt.figure()
plt.plot(t_m,Vx_m,linewidth=8,color='red');
plt.hold('on')
plt.plot(t_m,Vy_m,linewidth=8,color='green');
plt.plot(t_m,Vz_m,linewidth=8,color='blue');
plt.title('Velocity',color='black',fontsize=40)
plt.grid(ls='-')
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel('Seconds of Week/(s)',fontsize=35)
plt.ylabel('Velocity/(m/s)',fontsize=35)
plt.legend(['Vx','Vy','Vz'],fontsize=30);

# plt.figure()
# plt.subplot(3,1,1)
# plt.title('Velocity',fontsize=20)
# plt.plot(t_ie,Vx_ie,color='red',linewidth=3);
# plt.hold('on')
# plt.plot(t_m,Vx_m,color='green',linewidth=3);
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# plt.legend(['IE','Mine'],fontsize=20);

# plt.subplot(3,1,2)
# plt.plot(t_ie,Vy_ie,color='red',linewidth=3);
# plt.hold('on')
# plt.plot(t_m,Vy_m,color='green',linewidth=3);
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# plt.legend(['IE','Mine'],fontsize=20);

# plt.subplot(3,1,3)
# plt.plot(t_ie,Vz_ie,color='red',linewidth=3);
# plt.hold('on')
# plt.plot(t_m,Vz_m,color='green',linewidth=3);
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# plt.xlabel('Seconds of Week/(s)')
# plt.legend(['IE','Mine'],fontsize=20);




plt.show();

