#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

t,gx,gy,gz,ax,ay,az=[],[],[],[],[],[],[]


with open('FSAS20180503/imu.txt','rt') as f:
	for line in f:
		value=line.split()
		t.append(float(value[0]))
		gx.append(float(value[1]))
		gy.append(float(value[2]))
		gz.append(float(value[3]))
		ax.append(float(value[1]))
		ay.append(float(value[2]))
		az.append(float(value[3]))


plt.plot(t,gx,linewidth=5,color='red')
plt.hold('on')
plt.plot(t,gy,linewidth=5,color='green')
plt.plot(t,gz,linewidth=5,color='blue')
plt.title('Gyro Data',color='black',fontsize=20)
plt.xlabel('t/(s)',fontsize=20)
plt.ylabel('Gyro Data/(deg/s)',fontsize=20)
plt.legend(['X','Y','Z'],fontsize=20);

plt.figure()
plt.plot(t,ax,linewidth=5,color='red')
plt.hold('on')
plt.plot(t,ay,linewidth=5,color='green')
plt.plot(t,az,linewidth=5,color='blue')
plt.title('Accelerator Data',color='black',fontsize=20)
plt.xlabel('t/(s)',fontsize=20)
plt.ylabel('Accelerator Data/(m/s^2)',fontsize=20)
plt.legend(['X','Y','Z'],fontsize=20);

plt.show()
