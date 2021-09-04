#!/usr/local/bin/python3
# author: zhShen
# date: 20190620
import numpy as np
import matplotlib.pyplot as plt
import glv 

t,gx,gy,gz,ax,ay,az=[],[],[],[],[],[],[]
t1,gx1,gy1,gz1,ax1,ay1,az1=[],[],[],[],[],[],[]

# path = 'simulate'
path = '.'
count=0

with open(path+'/imu_U6FILE28.txt','rt') as f:
	for line in f:
		if line[0] == "#":
			continue
		value=line.split()
		# t.append(count);
		t.append(float(value[0]))
		gx.append(float(value[1]))
		gy.append(float(value[2]))
		gz.append(float(value[3]))
		ax.append(float(value[4]))
		ay.append(float(value[5]))
		az.append(float(value[6]))
		count=count+1


with open(path+'/starneto2.txt','rt') as f:
	for line in f:
		if line[0] == "%":
			continue
		value=line.split()
		t1.append(float(value[0]))
		gx1.append(float(value[1]))
		gy1.append(float(value[2]))
		gz1.append(float(value[3]))
		ax1.append(float(value[4]))
		ay1.append(float(value[5]))
		az1.append(float(value[6]))

# t_diff=[]
# t_count=[]
# for i in range(len(t)-1):
# 	t_count.append(i)
# 	t_diff.append(t[i+1]-t[i])


# print(t_diff,len(t_count),len(t_diff))

# plt.figure(figsize=(14, 7),dpi=100)
# plt.scatter(t_count,t_diff,s=10,color='red')


plt.figure(figsize=(12, 6),dpi=100)
plt.plot(t,gy,linewidth=5,color='red')
plt.plot(t1,gy1,linewidth=5,color='green')
# plt.plot(t,gz,linewidth=5,color='blue')
# plt.xlim(345849,356400)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('t/(s)',fontsize=20)
plt.ylabel('Gyroscope Data/(Rad)',fontsize=20)
plt.legend(['ADIS','Starneto'],fontsize=12,loc=1)
# plt.savefig(path +'/Gyroscope Data.png',dpi=300,bbox_inches = 'tight',transparent='true')


plt.figure(figsize=(12, 6),dpi=100)
plt.plot(t,gx,linewidth=5,color='red')
plt.plot(t1,gx1,linewidth=5,color='green')
# plt.plot(t,gz,linewidth=5,color='blue')
# plt.xlim(345849,356400)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('t/(s)',fontsize=20)
plt.ylabel('Gyroscope Data/(Rad)',fontsize=20)
plt.legend(['ADIS','Starneto'],fontsize=12,loc=1)


plt.figure(figsize=(12, 6),dpi=100)
plt.plot(t,gy,linewidth=5,color='red')
plt.plot(t1,gy1,linewidth=5,color='green')
# plt.plot(t,gz,linewidth=5,color='blue')
# plt.xlim(345849,356400)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('t/(s)',fontsize=20)
plt.ylabel('Gyroscope Data/(Rad)',fontsize=20)
plt.legend(['ADIS','Starneto'],fontsize=12,loc=1)

plt.figure(figsize=(12, 6),dpi=100)
plt.plot(t,gz,linewidth=5,color='red')
plt.plot(t1,gz1,linewidth=5,color='green')
# plt.plot(t,gz,linewidth=5,color='blue')
# plt.xlim(345849,356400)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('t/(s)',fontsize=20)
plt.ylabel('Gyroscope Data/(Rad)',fontsize=20)
plt.legend(['ADIS','Starneto'],fontsize=12,loc=1)

# plt.figure(figsize=(12, 6),dpi=100)
# plt.plot(t,ax,linewidth=5,color='red')
# plt.plot(t,ay,linewidth=5,color='green')
# plt.plot(t,az,linewidth=5,color='blue')
# # plt.xlim(345849,356400)
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# plt.xlabel('t/(s)',fontsize=20)
# plt.ylabel('Accelerometer Data/(m/s)',fontsize=20)
# plt.legend(['X','Y','Z'],fontsize=12,loc=1)
# plt.savefig(path +'/Accelerometer Data.png',dpi=300,bbox_inches = 'tight',transparent='true')

plt.show()
