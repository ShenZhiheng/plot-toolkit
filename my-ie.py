#!/usr/bin/python
from trans import xyz2blh
import numpy as np
import matplotlib.pyplot as plt

t_ie,X_ie,Y_ie,Z_ie=[],[],[],[]
t_m,X_m,Y_m,Z_m=[],[],[],[]

Vx_ie,Vy_ie,Vz_ie,Vx_m,Vy_m,Vz_m=[],[],[],[],[],[]
Sig_x,Sig_y,Sig_z,Sig_Vx,Sig_Vy,Sig_Vz=[],[],[],[],[],[]

with open('087/ie.txt','rt') as f:
	for line in f:
		value=line.split()
		t_ie.append(value[2]);
		X_ie.append(value[3]);
		Y_ie.append(value[4]);
		Z_ie.append(value[5]);
		Vx_ie.append(value[6]);
		Vy_ie.append(value[7]);
		Vz_ie.append(value[8]);
		Sig_x.append(value[12])
		Sig_y.append(value[13])
		Sig_z.append(value[14])
		Sig_Vx.append(value[15])
		Sig_Vy.append(value[16])
		Sig_Vz.append(value[17])

with open('087/HOLO-GR15.flt','rt') as f:
	for line in f:
		value=line.split()
		t_m.append(value[0]);
		X_m.append(value[1]);
		Y_m.append(value[2]);
		Z_m.append(value[3]);
		Vx_m.append(value[4]);
		Vy_m.append(value[5]);
		Vz_m.append(value[6]);

plt.subplot(3,1,1)
plt.title('Position')
plt.scatter(t_ie,X_ie,color='red',s=3);
plt.hold('on')
plt.scatter(t_m,X_m,color='green',s=3);
plt.legend(['IE','Mine']);

plt.subplot(3,1,2)
plt.scatter(t_ie,Y_ie,color='red',s=3);
plt.hold('on')
plt.scatter(t_m,Y_m,color='green',s=3);
plt.legend(['IE','Mine']);

plt.subplot(3,1,3)
plt.scatter(t_ie,Z_ie,color='red',s=3);
plt.hold('on')
plt.scatter(t_m,Z_m,color='green',s=3);
plt.xlabel('t/(s)')
plt.legend(['IE','Mine']);


plt.figure()
plt.subplot(3,1,1)
plt.title('Velocity')
plt.scatter(t_ie,Vx_ie,color='red',s=3);
plt.hold('on')
plt.scatter(t_m,Vx_m,color='green',s=3);
plt.legend(['IE','Mine']);

plt.subplot(3,1,2)
plt.scatter(t_ie,Vy_ie,color='red',s=3);
plt.hold('on')
plt.scatter(t_m,Vy_m,color='green',s=3);
plt.legend(['IE','Mine']);

plt.subplot(3,1,3)
plt.scatter(t_ie,Vz_ie,color='red',s=3);
plt.hold('on')
plt.scatter(t_m,Vz_m,color='green',s=3);
plt.xlabel('t/(s)')
plt.legend(['IE','Mine']);


plt.figure()
plt.title('Position Cov')
plt.scatter(t_ie,Sig_x,color='red',s=3);
plt.hold('on')
plt.scatter(t_ie,Sig_y,color='green',s=3);
plt.scatter(t_ie,Sig_z,color='blue',s=3);
plt.legend(['X','Y','Z'])
plt.xlabel('t/(s)')
plt.ylabel('Pos Cov/(m^2)')
plt.xlim(356930,359279)
plt.ylim(0,100)

plt.figure()
plt.title('Velocity Cov')
plt.scatter(t_ie,Sig_Vx,color='red',s=3);
plt.hold('on')
plt.scatter(t_ie,Sig_Vy,color='green',s=3);
plt.scatter(t_ie,Sig_Vz,color='blue',s=3);
plt.legend(['X','Y','Z'])
plt.xlabel('t/(s)')
plt.ylabel('Vel Cov/(m^2/s^2)')
plt.xlim(356930,359279)
plt.ylim(0,49)


plt.show();

