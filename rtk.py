#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import Bound as bd
import math

t_ie,X_ie,Y_ie,Z_ie=[],[],[],[]
t_m,X_m,Y_m,Z_m=[],[],[],[]
Vx_ie,Vy_ie,Vz_ie,Vx_m,Vy_m,Vz_m=[],[],[],[],[],[]
state=[]
floated,fixed=0.0,0.0

t,X_err,Y_err,Z_err,VX_err,VY_err,VZ_err,SUMXYZ,SUMVXYZ=[],[],[],[],[],[],[],[],[]
X_sum,Y_sum,Z_sum,VX_sum,VY_sum,VZ_sum=0.0,0.0,0.0,0.0,0.0,0.0

with open('SEPT20190716/GNSS_combined.txt','rt') as f:
	for line in f:
		value=line.split()
		if value[0] == "%":
			continue
		if value[24] == "FLOAT":
			continue
		t_ie.append(float(value[1]));
		X_ie.append(float(value[2]));
		Y_ie.append(float(value[3]));
		Z_ie.append(float(value[4]));
		Vx_ie.append(float(value[12]));
		Vy_ie.append(float(value[13]));
		Vz_ie.append(float(value[14]));

with open('SEPT20190716/xyzfileif.pos','rt') as f:
	for line in f:
		value=line.split()
		if value[0] == "%":
			continue

		if value[5] == "FLOAT":
			state.append(2)
			floated=floated+1
			continue
		else:
			state.append(1)
			fixed=fixed+1

		t_m.append(float(value[1]));
		X_m.append(float(value[2]));
		Y_m.append(float(value[3]));
		Z_m.append(float(value[4]));
		# Vx_m.append(float(value[14]));
		# Vy_m.append(float(value[15]));
		# Vz_m.append(float(value[16]));

for i in range(len(t_m)):
	index=bd.lower_bound(t_ie,t_m[i]);
	if abs(t_m[i]-t_ie[index])>1e-8:
		continue;
	t.append(t_m[i]);
	X_err.append(X_m[i]-X_ie[index])
	Y_err.append(Y_m[i]-Y_ie[index])
	Z_err.append(Z_m[i]-Z_ie[index])
# 	SUMXYZ.append(math.sqrt((X_m[i]-X_ie[index])*(X_m[i]-X_ie[index])+(Y_m[i]-Y_ie[index])*(Y_m[i]-Y_ie[index])+(Z_m[i]-Z_ie[index])*(Z_m[i]-Z_ie[index])))
# 	VX_err.append(Vx_m[i]-Vx_ie[index])
# 	VY_err.append(Vy_m[i]-Vy_ie[index])
# 	VZ_err.append(Vz_m[i]-Vz_ie[index])
for i in range(len(t_ie)):
	SUMVXYZ.append(math.sqrt((Vx_ie[i])*(Vx_ie[i])+(Vy_ie[i])*(Vy_ie[i])+(Vz_ie[i])*(Vz_ie[i])))


print fixed/(fixed+floated)

plt.figure()
# plt.plot(t_ie,SUMVXYZ,color='green',linewidth=5);
plt.scatter(range(len(state)),state,color='black',s=30);
# plt.title('Amb State',color='black',fontsize=40)

plt.figure()
plt.scatter(t,X_err,color='red',s=30);
plt.hold('on')
plt.scatter(t,Y_err,color='green',s=30);
plt.scatter(t,Z_err,color='blue',s=30);
plt.ylim(-1,1)
plt.title('Position error',color='black',fontsize=40)
plt.grid(ls='-')
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel('Seconds of Week/(s)',fontsize=35)
plt.ylabel('Position error/(m)',fontsize=35)
plt.legend(['X','Y','Z'],fontsize=30);

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

