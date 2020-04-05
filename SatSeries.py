#!/usr/bin/python
# author: zhShen
# date: 20190920
import numpy as np
import matplotlib.pyplot as plt
import math
import randcolor as rc

t_out,sat_list,vsat_list,nsat=[],[],[],[]
sss,ttt,eledeg=[],[],[]
nnn=[];

ele={'G01':[0],
'C06':[0]
}

for sys in ['G','R','E','C']:
	for number in range(1,50,1):
		if number<10:
			ss='0'+str(number)
		else:
			ss=str(number)
		prn = sys + ss
		ele[prn]=[]


path = '1'
attribute='great'



with open(path+'/out.txt','rt') as f:
	for line in f:
		value=line.split()
		if float(value[0])<361251:
		# if float(value[0])>358935 or float(value[0])<358500:
			continue

		t_out.append(float(value[0]))
		nnn.append(value[1])
		nsat=int(value[1])
		if nsat>100:
			continue

		for i in range(nsat):
			info=value[2+i].split(':')
			ele[info[0]].append((value[0])+'  '+(info[1]))




fig,ax1=plt.subplots(figsize=(20, 10))
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
		ax1.scatter(ttt,eledeg,s=5,label=prn,color=rc.randomcolor())
		ax1.set_xlabel('Seconds of Week/s',fontsize=35)
		plt.ylim([0,90])
		# plt.xlim([358450,359000])
		plt.xlim([361200,362000])
		plt.legend()
		sss,ttt,eledeg=[],[],[]
# plt.savefig(path + '/' +'Elevation1.png',dpi=700,bbox_inches = 'tight')


plt.figure(figsize=(20, 10))
plt.title('Number of Sats',color='black',fontsize=40)
plt.scatter(t_out,nnn,s=20,color='blue');
plt.grid(ls='-')
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel('Second of Week/(s)',fontsize=35)
plt.ylabel('Number of Sats/(#)',fontsize=35)
# plt.savefig(path + '/' +'nsat2.png',dpi=700,bbox_inches = 'tight')

plt.show();


