#!/usr/bin/python
# author: zhShen
# date: 20190620
import numpy as np
import matplotlib.pyplot as plt
import Bound as bd
import math
import randcolor as rc

t_ie,X_ie,Y_ie,Z_ie=[],[],[],[]
t_m,X_m,Y_m,Z_m=[],[],[],[]
Vx_ie,Vy_ie,Vz_ie,Vx_m,Vy_m,Vz_m=[],[],[],[],[],[]
floated,fixed=0.0,0.0

t,X_err,Y_err,Z_err,VX_err,VY_err,VZ_err,SUMXYZ,SUMVXYZ=[],[],[],[],[],[],[],[],[]
X_sum,Y_sum,Z_sum,VX_sum,VY_sum,VZ_sum=0.0,0.0,0.0,0.0,0.0,0.0
RMS=0.0

state=[]
ratio,pdop=[],[]

t_out,sat_list,vsat_list,nsat=[],[],[],[]
sss,ttt,eledeg=[],[],[]

ele={'G01':[0],
'C06':[0]
}


# color=[1 0 0;0 1 0;0 0 1;0 1 1]
# #;1 0,1;1,1,0;0.5,0.5,1;0.5,1,0.5;1,0.5,0.5;0.5,1,1;1,0.5,1;1,1,0.5;0.8,0.4,0.2;0.8,0.2,0.4;0.2,0.4,0.8]

for sys in ['G','R','E','C']:
	for number in range(1,50,1):
		if number<10:
			ss='0'+str(number)
		else:
			ss=str(number)
		prn = sys + ss
		ele[prn]=[]


path = 'SEPT20190716'
attribute='great'

with open(path+'/GNSS_combined.txt','rt') as f:
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

with open(path+'/xyzfileif.pos','rt') as f:
	for line in f:
		value=line.split()
		if value[0] == "%":
			continue

		if value[5] == "FLOAT":
			floated=floated+1
			state.append(2)
			continue
		else:
			fixed=fixed+1
			state.append(1)

		t_m.append(float(value[1]));
		X_m.append(float(value[2]));
		Y_m.append(float(value[3]));
		Z_m.append(float(value[4]));
		Vx_m.append(float(value[14]));
		Vy_m.append(float(value[15]));
		Vz_m.append(float(value[16]));
		if float(value[11])<100:
			ratio.append(float(value[11]))
		else:
			ratio.append(20)
		if float(value[12])<9:
			pdop.append(float(value[12]))
		else:
			pdop.append(1.3)


with open(path+'/out.txt','rt') as f:
	for line in f:
		value=line.split()
		if float(value[0])<100:
			continue
		t_out.append(float(value[0]))
		nsat=int(value[1])
		if nsat>100:
			continue

		for i in range(nsat):
			info=value[2+i].split(':')
			ele[info[0]].append((value[0])+'  '+(info[1]))

for i in range(len(t_m)):
	index=bd.lower_bound(t_ie,t_m[i]);
	# index=index-1
	# print t_m[i],t_ie[index]
	if abs(t_m[i]-t_ie[index])>1e-1:
		continue;	
	# if (abs(X_m[i]-X_ie[index])>1.0 or abs(Y_m[i]-Y_ie[index])>1.0 or abs(Z_m[i]-Z_ie[index])>1.0):
	# 	continue
	t.append(t_m[i]);
	X_err.append(X_m[i]-X_ie[index])
	Y_err.append(Y_m[i]-Y_ie[index])
	Z_err.append(Z_m[i]-Z_ie[index])
	SUMXYZ.append(math.sqrt((X_m[i]-X_ie[index])*(X_m[i]-X_ie[index])+(Y_m[i]-Y_ie[index])*(Y_m[i]-Y_ie[index])+(Z_m[i]-Z_ie[index])*(Z_m[i]-Z_ie[index])))
	VX_err.append(Vx_m[i]-Vx_ie[index])
	VY_err.append(Vy_m[i]-Vy_ie[index])
	VZ_err.append(Vz_m[i]-Vz_ie[index])
for i in range(len(t_ie)):
	SUMVXYZ.append(math.sqrt((Vx_ie[i])*(Vx_ie[i])+(Vy_ie[i])*(Vy_ie[i])+(Vz_ie[i])*(Vz_ie[i])))


for i in range(len(t)):
	X_sum=X_sum+abs(X_err[i]);
	Y_sum=Y_sum+abs(Y_err[i]);
	Z_sum=Z_sum+abs(Z_err[i]);
	RMS=RMS+abs(SUMXYZ[i])


X_sum=X_sum/len(t);
Y_sum=Y_sum/len(t);
Z_sum=Z_sum/len(t);
RMS=RMS/len(t);

print max(SUMXYZ),min(SUMXYZ),RMS,fixed/(fixed+floated)

plt.figure(figsize=(14, 7))
plt.scatter(t,X_err,color='red',s=30);
plt.hold('on')
plt.scatter(t,Y_err,color='green',s=30);
plt.scatter(t,Z_err,color='blue',s=30);
plt.ylim([-0.6,0.6])
plt.title('Novatel Position error',color='black',fontsize=40)
plt.grid(ls='-')
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel('Seconds of Week/(s)',fontsize=35)
plt.ylabel('Position error/(m)',fontsize=35)
plt.legend(['X','Y','Z'],fontsize=30);
# plt.savefig(path + '/' + attribute +'/ins-Position error.png',dpi=700,bbox_inches = 'tight')

plt.figure(figsize=(14, 7))
plt.scatter(t,VX_err,color='red',s=30);
plt.hold('on')
plt.scatter(t,VY_err,color='green',s=30);
plt.scatter(t,VZ_err,color='blue',s=30);
# plt.ylim([-0.6,0.6])
plt.title('Velocity error',color='black',fontsize=40)
plt.grid(ls='-')
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel('Seconds of Week/(s)',fontsize=35)
plt.ylabel('Position error/(m)',fontsize=35)
plt.legend(['X','Y','Z'],fontsize=30);


fig,ax1 = plt.subplots(figsize=(14, 7))
plt.tick_params(labelsize=30)
ax2 = ax1.twinx()
ax1.plot(t_m, ratio,'o-', c='red',label='ratio')
plt.tick_params(labelsize=30)
ax2.plot(t_m, pdop, 'o-', c='green',label='pdop') 
plt.title('Ratio & PDOP',color='black',fontsize=40)
ax1.set_xlabel('Seconds of Week/(s)',fontsize=35)
ax1.set_ylabel('Ratio',fontsize=35)
ax2.set_ylabel('PDOP',fontsize=35)
plt.legend()
plt.grid(ls='-')
# plt.savefig(path + '/' +'ratiopdop.png',dpi=700,bbox_inches = 'tight')


fig,ax1=plt.subplots(figsize=(18, 9))
plt.grid(ls='-')
# ax2=ax1.twinx()
# ax2.scatter(t_m,state,s=5,label='amb state')
plt.title('Elevation Series',color='black',fontsize=40)
plt.tick_params(labelsize=30)
for sys in ['G','R','E','C']:
	for number in range(1,50,1):
		if number<10:
			ss='0'+str(number)
		else:
			ss=str(number)
		prn = sys + ss
		if len(ele[prn])== 0 :
			continue
		for i in range(len(ele[prn])):
		 	sss=ele[prn][i].split()
		 	ttt.append(float(sss[0]))
		 	eledeg.append(float(sss[1]))
		ax1.plot(ttt,eledeg,linewidth=5,label=prn)
		ax1.set_xlabel('Second of Week/s',fontsize=35)
		plt.xlim([185200,187200])
		plt.legend()
		sss,ttt,eledeg=[],[],[]
plt.savefig(path + '/' +'Elevation.png',dpi=700,bbox_inches = 'tight')


# plt.figure(figsize=(14, 7))
# plt.plot(t_ie,Vx_ie,linewidth=8);
# plt.hold('on')
# plt.plot(t_ie,Vy_ie,linewidth=8);
# plt.plot(t_ie,Vz_ie,linewidth=8);
# plt.title('Velocity',color='black',fontsize=40)
# plt.grid(ls='-')
# plt.xticks(fontsize=30)
# plt.yticks(fontsize=30)
# plt.xlabel('Seconds of Week/(s)',fontsize=35)
# plt.ylabel('Velocity/(m/s)',fontsize=35)
# plt.legend(['Vx','Vy','Vz'],fontsize=30);
# plt.savefig(path + '/velocity.png',dpi=700,bbox_inches = 'tight')

plt.show();

