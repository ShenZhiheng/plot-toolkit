#!/usr/bin/python
# author: zhShen
# date: 20191130
import numpy as np
import matplotlib.pyplot as plt
import Bound as bd
import trans
import glv

X_sum,Y_sum,Z_sum,VX_sum,VY_sum,VZ_sum=0.0,0.0,0.0,0.0,0.0,0.0
ZTD=[]
sat=[]
Gsat=[]
Rsat=[]
Esat=[]
Csat=[]
t,X,Y,Z=[],[],[],[]
B,L,H=[],[],[]
floated,fixed=0.0,0.0

path = '.'
count=0
with open(path+'/xyzfileif.pos','rt') as f:
	for line in f:
		if line[0] == "%":
			continue
		value=line.split()
		if value[5] == "FLOAT":
			floated=floated+1
			# continue
		else:
			fixed=fixed+1

		t.append(count);
		[x,y,z]=[float(value[2]),float(value[3]),float(value[4])]
		# [b,l,h]=trans.xyz2blh(x,y,z)
		X.append(float(value[2])-(-2423816.8997));
		Y.append(float(value[3])-(5386057.0931));
		Z.append(float(value[4])-(2399883.3709));
		# B.append(b)
		# L.append(l)
		# H.append(h)
		sat.append(float(value[6]))
		Gsat.append(float(value[7]))
		Rsat.append(float(value[8]))
		Esat.append(float(value[9]))
		Csat.append(float(value[10]))
		count=count+1

for i in range(len(t)):
	X_sum=X_sum+(X[i]);
	Y_sum=Y_sum+(Y[i]);
	Z_sum=Z_sum+(Z[i]);

X_sum=X_sum/len(t);
Y_sum=Y_sum/len(t);
Z_sum=Z_sum/len(t);

for i in range(len(t)):
	X[i]=X[i]-X_sum
	Y[i]=Y[i]-Y_sum
	Z[i]=Z[i]-Z_sum

print floated, fixed, fixed/(fixed+floated)


plt.figure(figsize=(18, 9))
plt.subplot(3,1,1)
plt.title('Position Series',color='black',fontsize=20)
plt.scatter(t,X,color='red',s=10);
# plt.ylim(-0.1,0.1)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(['X'],fontsize=30);

plt.subplot(3,1,2)
plt.scatter(t,Y,color='green',s=10);
# plt.ylim(-0.1,0.1)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(['Y'],fontsize=30);

plt.subplot(3,1,3)
plt.scatter(t,Z,color='blue',s=10);
plt.xticks(fontsize=20)
# plt.ylim(-0.1,0.1)
plt.yticks(fontsize=20)
plt.xlabel('Epoch/(s)',fontsize=25)
plt.ylabel('Position/(m)',fontsize=25)
plt.legend(['Z'],fontsize=30);
# plt.savefig(path +'/RTKPosition.png',dpi=700,bbox_inches = 'tight')

plt.figure(figsize=(18, 9))
plt.scatter(t,sat,color='red',s=8)
plt.scatter(t,Gsat,color='green',s=8)
plt.scatter(t,Rsat,color='blue',s=8)
plt.scatter(t,Esat,color='orange',s=8)
plt.scatter(t,Csat,color='yellow',s=8)
plt.title('Satellite Series',color='black',fontsize=30)
plt.xlabel('Epoch/(s)',fontsize=25)
plt.ylabel('Sat Num/(#)',fontsize=25)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(['Total','GPS','GLO','GAL','BDS'],fontsize=30);
# plt.savefig(path +'/RTKSat.png',dpi=700,bbox_inches = 'tight')


plt.show();

