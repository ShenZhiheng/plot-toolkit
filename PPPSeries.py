#!/usr/bin/python
# author: zhShen
# date: 20191120
import numpy as np
import matplotlib.pyplot as plt
import Bound as bd
import trans
import glv

X_sum,Y_sum,Z_sum,VX_sum,VY_sum,VZ_sum=0.0,0.0,0.0,0.0,0.0,0.0
ZTD=[]
sat=[]
t,X,Y,Z=[],[],[],[]
B,L,H=[],[],[]

path = 'ZHD2019'
count=0
with open(path+'/SGG_-GREC3h.flt','rt') as f:
	for line in f:
		value=line.split()
		t.append(count);
		[x,y,z]=[float(value[2]),float(value[3]),float(value[4])]
		# [b,l,h]=trans.xyz2blh(x,y,z)
		X.append(float(value[2]));
		Y.append(float(value[3]));
		Z.append(float(value[4]));
		# B.append(b)
		# L.append(l)
		# H.append(h)
		ZTD.append(float(value[5]));
		sat.append(float(value[13]))
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


plt.figure(figsize=(18, 9))
plt.subplot(3,1,1)
plt.title('Position Series',color='black',fontsize=20)
plt.plot(t,X,color='red',linewidth=5);
plt.ylim(-0.2,0.2)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(['X'],fontsize=30);

plt.subplot(3,1,2)
plt.plot(t,Y,color='green',linewidth=5);
plt.ylim(-0.1,0.1)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(['Y'],fontsize=30);

plt.subplot(3,1,3)
plt.plot(t,Z,color='blue',linewidth=5);
plt.xticks(fontsize=20)
plt.ylim(-0.1,0.1)
plt.yticks(fontsize=20)
plt.xlabel('Epoch/(s)',fontsize=25)
plt.ylabel('Position/(m)',fontsize=25)
plt.legend(['Z'],fontsize=30);
# plt.savefig(path +'/Position1h.png',dpi=700,bbox_inches = 'tight')

plt.figure(figsize=(18, 9))
plt.plot(t,sat,color='red',linewidth=5)
plt.title('Satellite Series',color='black',fontsize=30)
plt.xlabel('Epoch/(s)',fontsize=25)
plt.ylabel('Sat Num/(#)',fontsize=25)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.savefig(path +'/Sat3h.png',dpi=700,bbox_inches = 'tight')


plt.show();

