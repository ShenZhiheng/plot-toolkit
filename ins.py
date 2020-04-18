#!/usr/local/bin/python3
# author: zhShen
# date: 20190420
import numpy as np
import matplotlib.pyplot as plt
import Bound as bd
import math

t_ie,X_ie,Y_ie,Z_ie=[],[],[],[]
t_m,X_m,Y_m,Z_m=[],[],[],[]
a,count=0,0
RMS=0.0
Vx_ie,Vy_ie,Vz_ie,Vx_m,Vy_m,Vz_m=[],[],[],[],[],[]
Pitch_ie,Roll_ie,Yaw_ie,Pitch_m,Roll_m,Yaw_m=[],[],[],[],[],[]
bgx,bgy,bgz,bax,bay,baz=[],[],[],[],[],[]

t,X_err,Y_err,Z_err,VX_err,VY_err,VZ_err,SUMXYZ=[],[],[],[],[],[],[],[]
Pitch_err,Roll_err,Yaw_err=[],[],[]
X_sum,Y_sum,Z_sum,VX_sum,VY_sum,VZ_sum,Pitch_sum,Roll_sum,Yaw_sum=0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0

path = 'FSAS20190614'

with open(path+'/TC_smooth_combined.txt','rt') as f:
	for line in f:
		if line[0] == "%":
			continue
		value=line.split()
		if value[24] == "FLOAT":
			continue
		t_ie.append(float(value[1]));
		X_ie.append(float(value[2])-(-2280124.80746)+(-2280126.217));
		Y_ie.append(float(value[3])-(5007874.71896)+(5007876.931));
		Z_ie.append(float(value[4])-(3214600.77599)+(3214601.416));
		Vx_ie.append(float(value[12]));
		Vy_ie.append(float(value[13]));
		Vz_ie.append(float(value[14]));
		Yaw_ie.append(float(value[21]));
		Pitch_ie.append(float(value[22]));
		Roll_ie.append(float(value[23]));
# -2280126.217     5007876.931     3214601.416
# -2280124.80746 5007874.71896 3214600.77599
with open(path+'/tci.ins','rt') as f:
	for line in f:
		if line[0] == "%":
			continue
		value=line.split()
		# if value[16] == "2":
		# 	continue
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
	Yaw_err.append(a)

for i in range(len(t)):
	X_sum=X_sum+abs(X_err[i]);
	Y_sum=Y_sum+abs(Y_err[i]);
	Z_sum=Z_sum+abs(Z_err[i]);
	VX_sum=VX_sum+abs(VX_err[i]);
	VY_sum=VY_sum+abs(VY_err[i]);
	VZ_sum=VZ_sum+abs(VZ_err[i]);
	Pitch_sum=Pitch_sum+abs(Pitch_err[i]);
	Roll_sum=Roll_sum+abs(Roll_err[i]);
	RMS=RMS+abs(SUMXYZ[i])

RMS=RMS/len(t);



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

print(max(SUMXYZ),min(SUMXYZ),RMS)

print(X_sum,Y_sum,Z_sum,VX_sum,VY_sum,VZ_sum,Pitch_sum,Roll_sum,Yaw_sum)


plt.figure(figsize=(14, 7),dpi=100)
plt.plot(t,X_err,color='red',linewidth=5);
plt.plot(t,Y_err,color='green',linewidth=5);
plt.plot(t,Z_err,color='blue',linewidth=5);
plt.title('Position error',color='black',fontsize=25)
plt.grid(ls='-')
# plt.ylim(-0.6,0.6)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('Seconds of Week/(s)',fontsize=20)
plt.ylabel('Position error/(m)',fontsize=20)
plt.legend(['X','Y','Z'],fontsize=30,loc=1);
# plt.savefig(path +'/Position error.png',bbox_inches = 'tight')

plt.figure(figsize=(14, 7),dpi=100)
plt.scatter(t,VX_err,color='red',s=20);
plt.scatter(t,VY_err,color='green',s=20);
plt.scatter(t,VZ_err,color='blue',s=20);
plt.title('TCI Velocity error',color='black',fontsize=20)
# plt.ylim(-0.1,0.1)
plt.grid(ls='-')
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('Seconds of Week/(s)',fontsize=20)
plt.ylabel('Velocity error/(m/s)',fontsize=20)
plt.legend(['Vx','Vy','Vz'],fontsize=30,loc=1);
# # plt.savefig(path +'/Vecocity error.png',bbox_inches = 'tight')


plt.figure(figsize=(14, 7),dpi=100)
plt.scatter(t,Pitch_err,color='red',s=8);
plt.title('TCI Attitude error',color='black',fontsize=25)
plt.scatter(t,Roll_err,color='green',s=8);
plt.scatter(t,Yaw_err,color='blue',s=8);
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('Seconds of Week/(s)',fontsize=20)
plt.grid(ls='-')
plt.ylim(-5,5)
plt.ylabel('Attitude error/(deg)',fontsize=20)
plt.legend(['Pitch','Roll','Yaw'],fontsize=30,loc=1);
# plt.savefig(path +'/Attitude error.png',bbox_inches = 'tight')


# plt.figure()
# plt.subplot(3,1,1)
# plt.title('Attitude',color='black',fontsize=20)
# plt.plot(t_ie,Pitch_ie,color='red',linewidth=3);
# plt.plot(t_m,Pitch_m,color='green',linewidth=3);
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# plt.legend(['IE','Mine'],fontsize=20,loc=1);

# plt.subplot(3,1,2)
# plt.plot(t_ie,Roll_ie,color='red',linewidth=3);
# plt.plot(t_m,Roll_m,color='green',linewidth=3);
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# plt.legend(['IE','Mine'],fontsize=20),loc=1;

# plt.subplot(3,1,3)
# plt.plot(t_ie,Yaw_ie,color='red',linewidth=3);
# plt.plot(t_m,Yaw_m,color='green',linewidth=3);
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# plt.xlabel('Seconds of Week/(s)')
# plt.legend(['IE','Mine'],fontsize=20,loc=1);

plt.figure(figsize=(14, 7),dpi=100)
plt.plot(t_m,bgx,color='red',linewidth=5);
plt.plot(t_m,bgy,color='green',linewidth=5);
plt.plot(t_m,bgz,color='blue',linewidth=5);
plt.title('Gyro Bias',color='black',fontsize=25)
plt.grid(ls='-')
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('Seconds of Week/(s)',fontsize=20)
plt.ylabel('bias of gyro/(deg/h)',fontsize=20)
plt.legend(['x','y','z'],fontsize=30,loc=1);


plt.figure(figsize=(14, 7),dpi=100)
plt.plot(t_m,bax,color='red',linewidth=5);
plt.plot(t_m,bay,color='green',linewidth=5);
plt.plot(t_m,baz,color='blue',linewidth=5);
plt.title('Accelerate Bias',color='black',fontsize=25)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('Seconds of Week/(s)',fontsize=20)
plt.ylabel('bias of acce/(mg)',fontsize=20)
plt.legend(['x','y','z'],fontsize=30,loc=1);


plt.show();

