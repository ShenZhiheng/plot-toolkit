#!/usr/bin/python
# author: zhShen
# date: 20190520
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
path = 'FSAS20190917/4'

with open(path+'/GNSS-combined.txt','rt') as f:
	for line in f:
		if line[0] == "%":
			continue
		value=line.split()
		if value[24] == "FLOAT":
			continue
		t_ie.append(float(value[1]));
		X_ie.append(float(value[2]));
		Y_ie.append(float(value[3]));
		Z_ie.append(float(value[4]));
		Vx_ie.append(float(value[12]));
		Vy_ie.append(float(value[13]));
		Vz_ie.append(float(value[14]));

with open(path+'/NPP6-GREC.flt','rt') as f:
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

plt.figure(figsize=(14, 7))
plt.scatter(t,X_err,s=20,color='red');
plt.hold('on')
plt.scatter(t,Y_err,s=20,color='green');
plt.scatter(t,Z_err,s=20,color='blue');
plt.title('Position error',color='black',fontsize=40)
plt.grid(ls='-')
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel('Seconds of Week/(s)',fontsize=35)
plt.ylabel('Position error/(m)',fontsize=35)
plt.legend(['X','Y','Z'],fontsize=30);
# plt.savefig(path +'/Position error.png',dpi=700,bbox_inches = 'tight')
# plt.figure()
# plt.scatter(t,VX_err,color='red',s=30);
# plt.hold('on')
# plt.scatter(t,VY_err,color='green',s=30);
# plt.scatter(t,VZ_err,color='blue',s=30);
# plt.title('Velocity error',color='black',fontsize=40)
# plt.grid(ls='-')
# plt.xticks(fontsize=30)
# plt.yticks(fontsize=30)
# # plt.ylim(-2,2)
# plt.xlabel('Seconds of Week/(s)',fontsize=35)
# plt.ylabel('Velocity error/(m/s)',fontsize=35)
# plt.legend(['Vx','Vy','Vz'],fontsize=30);


# plt.figure()
# plt.plot(t_m,Vx_m,linewidth=8,color='red');
# plt.hold('on')
# plt.plot(t_m,Vy_m,linewidth=8,color='green');
# plt.plot(t_m,Vz_m,linewidth=8,color='blue');
# plt.title('Velocity',color='black',fontsize=40)
# plt.grid(ls='-')
# plt.xticks(fontsize=30)
# plt.yticks(fontsize=30)
# plt.xlabel('Seconds of Week/(s)',fontsize=35)
# plt.ylabel('Velocity/(m/s)',fontsize=35)
# plt.legend(['Vx','Vy','Vz'],fontsize=30);

plt.show();

