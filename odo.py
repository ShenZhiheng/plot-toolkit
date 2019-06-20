#!/usr/bin/python
import trans
import Bound as bd
import numpy as np
import Cne
import glv
import matplotlib.pyplot as plt

count=0
t_o,B_o,L_o,H_o=[],[],[],[]
t_m,B_m,L_m,H_m=[],[],[],[]
b,l,h,x,y,z=0,0,0,0,0,0
ve,vn,vu,vx,vy,vz=0,0,0,0,0,0
Ve_o,Vn_o,Vu_o,Ve_m,Vn_m,Vu_m=[],[],[],[],[],[]
Pitch_o,Roll_o,Yaw_o,Pitch_m,Roll_m,Yaw_m=[],[],[],[],[],[]
t,B_err,L_err,H_err,Ve_err,Vn_err,Vu_err=[],[],[],[],[],[],[]
Pitch_err,Roll_err,Yaw_err=[],[],[]

with open('HOLO20190611/odometry.txt','rt') as f:
	for line in f:
		value=line.split(',')
		t_o.append(float(value[1]))
		l=float(value[2])
		b=float(value[3])
		h=float(value[4])
		B_o.append(b)
		L_o.append(l)
		H_o.append(h)
		Ve_o.append(float(value[8]))
		Vn_o.append(float(value[9]))
		Vu_o.append(float(value[10]))
		Pitch_o.append(float(value[5])/glv.deg)
		Roll_o.append(float(value[6])/glv.deg)
		Yaw_o.append(float(value[7])/glv.deg)

with open('HOLO20190611/HOLO-GRC.odo','rt') as f:
	for line in f:
		if count==0 or count==1:
			count=count+1
			continue
		value=line.split()
		t_m.append(float(value[0]))
		B_m.append(float(value[2]));
		L_m.append(float(value[1]));
		H_m.append(float(value[3]));
		Ve_m.append(float(value[7]));
		Vn_m.append(float(value[8]));
		Vu_m.append(float(value[9]));
		Pitch_m.append(float(value[4]))
		Roll_m.append(float(value[5]))
		Yaw_m.append(float(value[6]))

for i in range(len(t_m)):
	index=bd.lower_bound(t_o,t_m[i]);
	# index=index-1
	print t_m[i],t_o[index]
	if abs(t_m[i]-t_o[index])>0.008:
		continue;
	t.append(t_m[i]);
	B_err.append(B_m[i]-B_o[index])
	L_err.append(L_m[i]-L_o[index])
	H_err.append(H_m[i]-H_o[index])
	Ve_err.append(Ve_m[i]-Ve_o[index])
	Vn_err.append(Vn_m[i]-Vn_o[index])
	Vu_err.append(Vu_m[i]-Vu_o[index])
	Pitch_err.append(Pitch_m[i]-Pitch_o[index])
	Roll_err.append(Roll_m[i]-Roll_o[index])
	a=Yaw_m[i]-Yaw_o[index]
	Yaw_err.append(a)


# plt.title('Position')
# plt.plot(t_o,B_o,color='red',linewidth=5);
# plt.hold('on')
# plt.plot(t_m,B_m,color='green',linewidth=5);
# plt.legend(['odo','Mine']);

# plt.figure()
# plt.plot(t_o,L_o,color='red',linewidth=5);
# plt.hold('on')
# plt.plot(t_m,L_m,color='green',linewidth=5);
# plt.legend(['odo','Mine']);

plt.figure()
plt.plot(t_o,H_o,color='red',linewidth=5);
plt.hold('on')
plt.plot(t_m,H_m,color='green',linewidth=5);
plt.xlabel('t/(s)')
plt.title('Height',color='black',fontsize=30)
plt.legend(['odo','Mine']);


plt.figure()
plt.plot(B_o,L_o,color='green',linewidth=5)
plt.plot(B_m,L_m,color='red',linewidth=5)
plt.title('Trajectory',color='black',fontsize=30)
plt.legend(['odo','Mine']);
plt.grid(ls='-')
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel('Latitude/(rad)',fontsize=35)
plt.ylabel('Longitude/(rad)',fontsize=35)


plt.figure()
plt.title('Ve',color='black',fontsize=30)
plt.plot(t_o,Ve_o,color='red',linewidth=5);
plt.hold('on')
plt.plot(t_m,Ve_m,color='green',linewidth=5);
plt.legend(['odo','Mine']);

plt.figure()
plt.title('Vn',color='black',fontsize=30)
plt.plot(t_o,Vn_o,color='red',linewidth=5);
plt.hold('on')
plt.plot(t_m,Vn_m,color='green',linewidth=5);
plt.legend(['odo','Mine']);

plt.figure()
plt.title('Vu',color='black',fontsize=30)
plt.plot(t_o,Vu_o,color='red',linewidth=5);
plt.hold('on')
plt.plot(t_m,Vu_m,color='green',linewidth=5);
plt.xlabel('t/(s)')
plt.legend(['odo','Mine']);



plt.figure()
plt.subplot(3,1,1)
plt.title('Attitude',color='black',fontsize=20)
plt.plot(t_o,Pitch_o,color='red',linewidth=3);
plt.hold('on')
plt.plot(t_m,Pitch_m,color='green',linewidth=3);
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(['odo','Mine'],fontsize=20);

plt.subplot(3,1,2)
plt.plot(t_o,Roll_o,color='red',linewidth=3);
plt.hold('on')
plt.plot(t_m,Roll_m,color='green',linewidth=3);
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(['odo','Mine'],fontsize=20);

plt.subplot(3,1,3)
plt.plot(t_o,Yaw_o,color='red',linewidth=3);
plt.hold('on')
plt.plot(t_m,Yaw_m,color='green',linewidth=3);
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('Seconds of Week/(s)')
plt.legend(['odo','Mine'],fontsize=20);




plt.figure()
plt.plot(t,B_err,linewidth=5);
plt.hold('on')
plt.plot(t,L_err,linewidth=5);
plt.plot(t,H_err,linewidth=5);
plt.title('Position error',color='black',fontsize=40)
plt.grid(ls='-')
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel('Seconds of Week/(s)',fontsize=35)
plt.ylabel('Position error/(m)',fontsize=35)
plt.legend(['B','L','H'],fontsize=30);

plt.figure()
plt.plot(t,Ve_err,linewidth=5);
plt.hold('on')
plt.plot(t,Vn_err,linewidth=5);
plt.plot(t,Vu_err,linewidth=5);
plt.title('Velocity error',color='black',fontsize=40)
plt.grid(ls='-')
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel('Seconds of Week/(s)',fontsize=35)
plt.ylabel('Velocity error/(m/s)',fontsize=35)
plt.legend(['Ve','Vn','Vu'],fontsize=30);

plt.figure()
plt.plot(t,Pitch_err,color='red',linewidth=5);
plt.title('Attitude error',color='black',fontsize=40)
plt.plot(t,Roll_err,color='green',linewidth=5);
# plt.plot(t,Yaw_err,color='blue',linewidth=5);
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.grid(ls='-')
plt.xlabel('Seconds of Week/(s)',fontsize=35)
plt.ylabel('Attitude error/(deg)',fontsize=35)
plt.legend(['Pitch','Roll','Yaw'],fontsize=30);



plt.show();

