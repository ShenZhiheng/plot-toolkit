#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import Bound as bd
import math

t_ie,X_ie,Y_ie,Z_ie=[],[],[],[]
t_m,X_m,Y_m,Z_m=[],[],[],[]
Vx_ie,Vy_ie,Vz_ie,Vx_m,Vy_m,Vz_m=[],[],[],[],[],[]
state=[]
fixed,floated=0.0,0.0
path='FSAS20150722'
t,X_err,Y_err,Z_err,VX_err,VY_err,VZ_err,SUMXYZ,SUMVXYZ=[],[],[],[],[],[],[],[],[]
X_sum,Y_sum,Z_sum,VX_sum,VY_sum,VZ_sum=0.0,0.0,0.0,0.0,0.0,0.0
RMS=0.0
nSat=[]

with open(path + '/FSAS20150722.pos','rt') as f:
	for line in f:
		value=line.split()
		# if value[24] == "FLOAT":
		# 	continue
		t_ie.append(float(value[0]));
		X_ie.append(float(value[1]));
		Y_ie.append(float(value[2]));
		Z_ie.append(float(value[3]));
		# Vx_ie.append(float(value[4]));
		# Vy_ie.append(float(value[5]));
		# Vz_ie.append(float(value[6]));

with open(path + '/xyzfileif.pos','rt') as f:
	for line in f:
		value=line.split()
		if value[0] == "%":
			continue
		if value[5] == "FLOAT":
			# fixed=fixed+1
			continue
		# else:
		# 	floated=floated+1
		# 	continue
		# if value[5] == "2":
		# 	state.append(0.2)
		# else:
		# 	state.append(0.1)
		t_m.append(float(value[1]));
		X_m.append(float(value[2]));
		Y_m.append(float(value[3]));
		Z_m.append(float(value[4]));
		nSat.append(int(value[6]))
		# Vx_m.append(float(value[14]));
		# Vy_m.append(float(value[15]));
		# Vz_m.append(float(value[16]));

for i in range(len(t_m)):
	# SUMVXYZ.append(math.sqrt((Vx_m[i])*(Vx_m[i])+(Vy_m[i])*(Vy_m[i])+(Vz_m[i])*(Vz_m[i])))
	index=bd.lower_bound(t_ie,t_m[i]);
	if abs(t_m[i]-t_ie[index])>1e-8:
		continue;
	t.append(t_m[i]);
	X_err.append(X_m[i]-X_ie[index])
	Y_err.append(Y_m[i]-Y_ie[index])
	Z_err.append(Z_m[i]-Z_ie[index])
	SUMXYZ.append(math.sqrt((X_m[i]-X_ie[index])*(X_m[i]-X_ie[index])+(Y_m[i]-Y_ie[index])*(Y_m[i]-Y_ie[index])+(Z_m[i]-Z_ie[index])*(Z_m[i]-Z_ie[index])))
	# VX_err.append(Vx_m[i]-Vx_ie[index])
	# VY_err.append(Vy_m[i]-Vy_ie[index])
	# VZ_err.append(Vz_m[i]-Vz_ie[index])

# print max(SUMXYZ),min(SUMXYZ),fixed/(fixed+floated)

for i in range(len(t)):
	X_sum=X_sum+abs(X_err[i]);
	Y_sum=Y_sum+abs(Y_err[i]);
	Z_sum=Z_sum+abs(Z_err[i]);
	RMS=RMS+abs(SUMXYZ[i])

X_sum=X_sum/len(t);
Y_sum=Y_sum/len(t);
Z_sum=Z_sum/len(t);
RMS=RMS/len(t);

print X_sum,Y_sum,Z_sum,RMS


plt.figure(figsize=(14,7))
plt.scatter(t_m,nSat,color='red',s=30)
plt.title('Number of Sat',color='black',fontsize=40)
plt.grid(ls='-')
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel('Seconds of Week/(s)',fontsize=35)
plt.ylabel('Number',fontsize=35)
# plt.savefig(path + '/Number of Sat.png',dpi=700,bbox_inches = 'tight')

plt.figure(figsize=(14, 7))
plt.scatter(t,X_err,color='red',s=30);
plt.hold('on')
plt.scatter(t,Y_err,color='green',s=30);
plt.scatter(t,Z_err,color='blue',s=30);
# plt.ylim(-0.5,0.5)
plt.title('Position error',color='black',fontsize=40)
plt.grid(ls='-')
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel('Seconds of Week/(s)',fontsize=35)
plt.ylabel('Position error/(m)',fontsize=35)
plt.legend(['X','Y','Z'],fontsize=30);
# plt.savefig(path + '/RTKlib Position error.png',dpi=700,bbox_inches = 'tight')
# plt.figure()
# plt.plot(t_m,Vx_m,linewidth=8);
# plt.hold('on')
# plt.plot(t_m,Vy_m,linewidth=8);
# plt.plot(t_m,Vz_m,linewidth=8);
# plt.title('Velocity error',color='black',fontsize=40)
# plt.grid(ls='-')
# plt.xticks(fontsize=30)
# plt.yticks(fontsize=30)
# plt.xlabel('Seconds of Week/(s)',fontsize=35)
# plt.ylabel('Velocity error/(m/s)',fontsize=35)
# plt.legend(['Vx','Vy','Vz'],fontsize=30);

plt.show();

