#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import Bound as bd
import math

t_ie,X_ie,Y_ie,Z_ie=[],[],[],[]
t_m,X_m,Y_m,Z_m=[],[],[],[]
a=0;
Vx_ie,Vy_ie,Vz_ie,Vx_m,Vy_m,Vz_m=[],[],[],[],[],[]
Pitch_ie,Roll_ie,Yaw_ie,Pitch_m,Roll_m,Yaw_m=[],[],[],[],[],[]
bgx,bgy,bgz,bax,bay,baz=[],[],[],[],[],[]

t,X_err,Y_err,Z_err,VX_err,VY_err,VZ_err,SUMXYZ=[],[],[],[],[],[],[],[]
Pitch_err,Roll_err,Yaw_err=[],[],[]
X_sum,Y_sum,Z_sum,VX_sum,VY_sum,VZ_sum,Pitch_sum,Roll_sum,Yaw_sum=0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0

with open('FSAS20150722/FSAS20150722.trj','rt') as f:
	for line in f:
		value=line.split()
		t_ie.append(float(value[0]));
		X_ie.append(float(value[1]));
		Y_ie.append(float(value[2]));
		Z_ie.append(float(value[3]));
		Vx_ie.append(float(value[4]));
		Vy_ie.append(float(value[5]));
		Vz_ie.append(float(value[6]));
		Yaw_ie.append(float(value[7]));
		Pitch_ie.append(float(value[8]));
		Roll_ie.append(float(value[9]));


with open('FSAS20150722/TCI/tci.ins','rt') as f:
	for line in f:
		value=line.split()
		t_m.append(float(value[0]));
		X_m.append(float(value[1]));
		Y_m.append(float(value[2]));
		Z_m.append(float(value[3]));
		Vx_m.append(float(value[4]));
		Vy_m.append(float(value[5]));
		Vz_m.append(float(value[6]));
		Pitch_m.append(float(value[7]));
		Roll_m.append(float(value[8]));
		Yaw_m.append(float(value[9]));
		bgx.append(float(value[10]));
		bgy.append(float(value[11]));
		bgz.append(float(value[12]));
		bax.append(float(value[13]));
		bay.append(float(value[14]));
		baz.append(float(value[15]));

for i in range(len(t_m)):
	index=bd.lower_bound(t_ie,t_m[i]);
	index=index-1
	if abs(t_m[i]-t_ie[index]-0.0025)>1e-8:
		continue;
	t.append(t_m[i]);
	X_err.append(X_m[i]-X_ie[index])
	Y_err.append(Y_m[i]-Y_ie[index])
	Z_err.append(Z_m[i]-Z_ie[index])
	SUMXYZ.append(math.sqrt((X_m[i]-X_ie[index])*(X_m[i]-X_ie[index])+(Y_m[i]-Y_ie[index])*(Y_m[i]-Y_ie[index])+(Z_m[i]-Z_ie[index])*(Z_m[i]-Z_ie[index])))
	VX_err.append(Vx_m[i]-Vx_ie[index])
	VY_err.append(Vy_m[i]-Vy_ie[index])
	VZ_err.append(Vz_m[i]-Vz_ie[index])
	Pitch_err.append(Pitch_m[i]-Pitch_ie[index])
	Roll_err.append(Roll_m[i]-Roll_ie[index])
	a=Yaw_m[i]-Yaw_ie[index]
	if abs(Yaw_m[i]-Yaw_ie[index])>20:
		a=0
	if t_m[i]>27200:
		Yaw_err.append(a)
	# print i,X_err[i],Y_err[i],Z_err[i],VX_err[i],VY_err[i],VZ_err[i]

for i in range(len(t)):
	X_sum=X_sum+abs(X_err[i]);
	Y_sum=Y_sum+abs(Y_err[i]);
	Z_sum=Z_sum+abs(Z_err[i]);
	VX_sum=VX_sum+abs(VX_err[i]);
	VY_sum=VY_sum+abs(VY_err[i]);
	VZ_sum=VZ_sum+abs(VZ_err[i]);
	Pitch_sum=Pitch_sum+abs(Pitch_err[i]);
	Roll_sum=Roll_sum+abs(Roll_err[i]);

for i in range(len(Yaw_err)):
	Yaw_sum=Yaw_sum+abs(Yaw_err[i]);


X_sum=X_sum/len(t);
Y_sum=Y_sum/len(t);
Z_sum=Z_sum/len(t);
VX_sum=VX_sum/len(t);
VY_sum=VY_sum/len(t);
VZ_sum=VZ_sum/len(t);
Pitch_sum=Pitch_sum/len(t);
Roll_sum=Roll_sum/len(t);
Yaw_sum=Yaw_sum/len(Yaw_err);

print X_sum,Y_sum,Z_sum,VX_sum,VY_sum,VZ_sum,Pitch_sum,Roll_sum,Yaw_sum


plt.plot(t,SUMXYZ,linewidth=8)
plt.xlabel('Seconds of Week/(s)',fontsize=20)
plt.ylabel('Position error/(m)',fontsize=20)

plt.figure()
plt.plot(t,X_err,linewidth=10);
plt.hold('on')
plt.plot(t,Y_err,linewidth=10);
plt.plot(t,Z_err,linewidth=10);
plt.title('Position error',color='black',fontsize=40)
plt.grid(ls='-')
# plt.ylim(-10,10)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel('Seconds of Week/(s)',fontsize=35)
plt.ylabel('Position error/(m)',fontsize=35)
plt.legend(['X','Y','Z'],fontsize=30);

plt.figure()
plt.plot(t,VX_err,linewidth=8);
plt.hold('on')
plt.plot(t,VY_err,linewidth=8);
plt.plot(t,VZ_err,linewidth=8);
plt.title('Velocity error',color='black',fontsize=40)
# plt.ylim(-0.5,0.5)
plt.grid(ls='-')
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel('Seconds of Week/(s)',fontsize=35)
plt.ylabel('Velocity error/(m/s)',fontsize=35)
plt.legend(['Vx','Vy','Vz'],fontsize=30);

# plt.figure()
# plt.plot(range(len(t)),Pitch_err,linewidth=8);
# plt.title('Attitude error',color='black',fontsize=40)
# plt.plot(range(len(t)),Roll_err,linewidth=8);
# plt.plot(range(len(t)),Yaw_err,linewidth=8);
# plt.grid(ls='-')
# plt.xticks(fontsize=30)
# plt.yticks(fontsize=30)
# plt.xlabel('Seconds of Week/(s)',fontsize=35)
# plt.ylabel('Attitude error/(deg)',fontsize=35)
# plt.legend(['Pitch','Roll','Yaw'],fontsize=30);

plt.figure()
plt.plot(t,Pitch_err,color='red',linewidth=8);
plt.title('Attitude error',color='black',fontsize=40)
plt.plot(t,Roll_err,color='green',linewidth=8);
plt.plot(t,Yaw_err,color='blue',linewidth=8);
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.grid(ls='-')
# plt.ylim(-1,1)
plt.xlabel('Seconds of Week/(s)',fontsize=35)
plt.ylabel('Attitude error/(deg)',fontsize=35)
plt.legend(['Pitch','Roll','Yaw'],fontsize=30);

# plt.figure()
# plt.subplot(3,1,1)
# plt.title('Position',color='black',fontsize=20)
# plt.plot(t_ie,X_ie,color='red',linewidth=3);
# plt.hold('on')
# plt.plot(t_m,X_m,color='green',linewidth=3);
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# plt.legend(['IE','Mine'],fontsize=20);

# plt.subplot(3,1,2)
# plt.plot(t_ie,Y_ie,color='red',linewidth=3);
# plt.hold('on')
# plt.plot(t_m,Y_m,color='green',linewidth=3);
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# plt.legend(['IE','Mine'],fontsize=20);

# plt.subplot(3,1,3)
# plt.plot(t_ie,Z_ie,color='red',linewidth=3);
# plt.hold('on')
# plt.plot(t_m,Z_m,color='green',linewidth=3);
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# plt.xlabel('Seconds of Week/(s)',fontsize=20)
# plt.legend(['IE','Mine'],fontsize=20);


# plt.figure()
# plt.subplot(3,1,1)
# plt.title('Velocity',color='black',fontsize=20)
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


# plt.figure()
# plt.subplot(3,1,1)
# plt.title('Attitude',color='black',fontsize=20)
# plt.plot(t_ie,Pitch_ie,color='red',linewidth=3);
# plt.hold('on')
# plt.plot(t_m,Pitch_m,color='green',linewidth=3);
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# plt.legend(['IE','Mine'],fontsize=20);

# plt.subplot(3,1,2)
# plt.plot(t_ie,Roll_ie,color='red',linewidth=3);
# plt.hold('on')
# plt.plot(t_m,Roll_m,color='green',linewidth=3);
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# plt.legend(['IE','Mine'],fontsize=20);

# plt.subplot(3,1,3)
# plt.plot(t_ie,Yaw_ie,color='red',linewidth=3);
# plt.hold('on')
# plt.plot(t_m,Yaw_m,color='green',linewidth=3);
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# plt.xlabel('Seconds of Week/(s)')
# plt.legend(['IE','Mine'],fontsize=20);

plt.figure()
plt.plot(t_m,bgx,color='red',linewidth=8);
plt.hold('on')
plt.plot(t_m,bgy,color='green',linewidth=8);
plt.hold('on')
plt.plot(t_m,bgz,color='blue',linewidth=8);
plt.title('Gyro Bias',color='black',fontsize=40)
plt.grid(ls='-')
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel('Seconds of Week/(s)',fontsize=35)
plt.ylabel('bias of gyro/(deg/h)',fontsize=35)
plt.legend(['x','y','z'],fontsize=30);


plt.figure()
plt.plot(t_m,bax,color='red',linewidth=8);
plt.hold('on')
plt.plot(t_m,bay,color='green',linewidth=8);
plt.hold('on')
plt.plot(t_m,baz,color='blue',linewidth=8);
plt.title('Accelerate Bias',color='black',fontsize=40)
plt.grid(ls='-')
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel('Seconds of Week/(s)',fontsize=35)
plt.ylabel('bias of acce/(mg)',fontsize=35)
plt.legend(['x','y','z'],fontsize=30);


plt.show();

