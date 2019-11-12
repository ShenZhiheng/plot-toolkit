#!/usr/bin/python
# author: zhShen
# date: 20190620
import numpy as np
import matplotlib.pyplot as plt

t,gx,gy,gz,ax,ay,az=[],[],[],[],[],[],[]
t1,gx1,gy1,gz1,ax1,ay1,az1=[],[],[],[],[],[],[]

path = 'FSAS20190917/3'

with open(path+'/imu3.txt','rt') as f:
	for line in f:
		if line[0] == "%":
			continue
		value=line.split()
		t.append(float(value[0]))
		gx.append(float(value[1]))
		gy.append(float(value[2]))
		gz.append(float(value[3]))
		ax.append(float(value[4]))
		ay.append(float(value[5]))
		az.append(float(value[6]))


with open(path+'/sbg.txt','rt') as f:
	for line in f:
		if line[0] == "%":
			continue
		value=line.split()
		t1.append(float(value[0]))
		gx1.append(float(value[1])+60)
		gy1.append(float(value[2])+60)
		gz1.append(float(value[3])+60)
		ax1.append(float(value[4])+30)
		ay1.append(float(value[5])+30)
		az1.append(float(value[6])+30)



plt.plot(t,ay,linewidth=5,color='red')
plt.hold('on')
plt.plot(t1,ay1,linewidth=5,color='green')
# plt.plot(t,gz,linewidth=5,color='blue')
plt.title('Gyro Data',color='black',fontsize=20)
plt.xlabel('t/(s)',fontsize=20)
plt.ylabel('Gyro Data/(deg/s)',fontsize=20)
plt.legend(['X','Y','Z'],fontsize=20);

# plt.figure()
# plt.plot(t,ax,linewidth=5,color='red')
# plt.hold('on')
# plt.plot(t,ay,linewidth=5,color='green')
# # plt.plot(t,az,linewidth=5,color='blue')
# plt.title('Accelerator Data',color='black',fontsize=20)
# plt.xlabel('t/(s)',fontsize=20)
# plt.ylabel('Accelerator Data/(m/s^2)',fontsize=20)
# plt.legend(['X','Y','Z'],fontsize=20);

plt.show()
