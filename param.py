#!/usr/local/bin/python3
# author: zhShen
# date: 20200613
import numpy as np
import matplotlib.pyplot as plt
import randcolor as rc

t=[]

par={'AMB_L1':[0],
'CRD_X':[0],
'CRD_Y':[0],
'CRD_Z':[0],
'CLK':[0],
'TRP':[0],
'P1P2E_REC':[0],
'P1P2G_REC':[0],
'GAL_ISB':[0]

}

for sys in ['G','R','E','C']:
	for number in range(1,50,1):
		if number<10:
			ss='0'+str(number)
		else:
			ss=str(number)
		prn = sys + ss
		ion = 'SION_'+prn
		amb1 = 'AMB_L1_'+prn
		amb2 = 'AMB_L2_'+prn
		par[ion]=[]
		par[amb1]=[]
		par[amb2]=[]


with open('debug.log','rt') as f:
	for line in f:
		if line[0] == "%" or line[0] == "#":
			continue
		value=line.split()
		t.append(float(value[0]))
		npar = int(value[1])

		for i in range(npar):
			tt = value[0]
			_type = value[2+3*i]
			_val = float(value[2+3*i+1])
			_cov = float(value[2+3*i+2])
			par[_type].append(str(tt)+'  '+str(_val)+'  '+str(_cov))

fig,ax1=plt.subplots(figsize=(20, 7),dpi=100)
# print(par['SION_G01'])

time,val,cov=[],[],[]

for sys in ['G','R','E','C']:
	for number in range(1,50,1):
		if number<10:
			ss='0'+str(number)
		else:
			ss=str(number)
		prn = sys + ss
		ion = 'SION_'+prn
		amb1 = 'AMB_L1_'+prn
		amb2 = 'AMB_L2_'+prn	
		#ion=amb1	
		if len(par[ion])== 0 :
			continue
		for i in range(len(par[ion])):
		 	sss=par[ion][i].split()
		 	time.append(float(sss[0]))
		 	val.append(float(sss[1]))
		 	# print(float(sss[2]))
		 	cov.append(float(sss[2]))

		ax1.scatter(time,val,s=5,label=ion,color=rc.randomcolor())
		ax1.set_xlabel('Seconds of Week/s',fontsize=15)
		ax1.set_ylabel('Value',fontsize=15)
		# plt.ylim([0,30])
		plt.grid(ls='-')
		plt.legend(fontsize=5,loc=1)
		time,val,cov=[],[],[]


plt.show();

