#!/usr/bin/python
from trans import xyz2blh
import numpy as np
import matplotlib.pyplot as plt

t,X,Y,Z,Vx,Vy,Vz=[],[],[],[],[],[],[]
B,L,H=[],[],[]
Sig_x,Sig_y,Sig_z,Sig_Vx,Sig_Vy,Sig_Vz=[],[],[],[],[],[]
nSat,PDOP=[],[]

with open('FSAS20190113/FSAS-GR.flt','rt') as f:
	for line in f:
		value=line.split()
		t.append(float(value[0]))
		X.append(float(value[1]))
		Y.append(float(value[2]))
		Z.append(float(value[3]))
		[b,l,h]=xyz2blh(float(value[1]),float(value[2]),float(value[3]))
 		# [b,l,h]=[float(value[1]),float(value[2]),float(value[3])]
		B.append(b)
		L.append(l)
		H.append(h)
		Vx.append(value[4])
		Vy.append(value[5])
		Vz.append(value[6])

		Sig_x.append(value[7])
		Sig_y.append(value[8])
		Sig_z.append(value[9])
		Sig_Vx.append(value[10])
		Sig_Vy.append(value[11])
		Sig_Vz.append(value[12])
		nSat.append(value[13])
		PDOP.append(value[14])

plt.scatter(B,L,color='green',s=30)
plt.title('Position',color='black',fontsize=40)
plt.grid(ls='-')
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel('Latitude/(rad)',fontsize=35)
plt.ylabel('Longitude/(rad)',fontsize=35)

# plt.figure()
# plt.title('Number of Sats',color='black',fontsize=40)
# plt.scatter(t,nSat,s=20);
# plt.grid(ls='-')
# plt.xticks(fontsize=30)
# plt.yticks(fontsize=30)
# plt.xlabel('Second of Week/(s)',fontsize=35)
# plt.ylabel('Number of Sats/(#)',fontsize=35)

# plt.figure()
# plt.title('PDOP',color='black',fontsize=40)
# plt.scatter(t,PDOP,s=20,color='orange');
# plt.grid(ls='-')
# plt.xticks(fontsize=30)
# plt.yticks(fontsize=30)
# plt.xlabel('Second of Week/(s)',fontsize=35)
# plt.ylabel('Number of Sats/(#)',fontsize=35)


# plt.figure()
# plt.plot(t,Vx,color='red',linewidth=10)
# plt.hold('on')
# plt.title('Velocity',color='black',fontsize=40)
# plt.plot(t,Vy,color='green',linewidth=10)
# plt.plot(t,Vz,color='blue',linewidth=10)
# plt.grid(ls='-')
# plt.xticks(fontsize=30)
# plt.yticks(fontsize=30)
# plt.xlabel('Second of Week/(s)',fontsize=35)
# plt.ylabel('Velocity/(m/s)',fontsize=35)
# plt.legend(['Vx','Vy','Vz'],fontsize=30)


# plt.figure()
# plt.title('Position Std',fontsize=40)
# plt.plot(t,Sig_x,color='red',linewidth=10)
# plt.hold('on')
# plt.plot(t,Sig_y,color='green',linewidth=10)
# plt.plot(t,Sig_z,color='blue',linewidth=10)
# plt.grid(ls='-')
# plt.xticks(fontsize=30)
# plt.yticks(fontsize=30)
# plt.legend(['Sig_x','Sig_y','Sig_z'],fontsize=30)
# plt.xlabel('Second of Week/(s)',fontsize=35)
# plt.ylabel('Std/(m)',fontsize=35)


# plt.figure()
# plt.title('Velocity Std',fontsize=40)
# plt.plot(t,Sig_Vx,color='red',linewidth=10)
# plt.hold('on')
# plt.plot(t,Sig_Vy,color='green',linewidth=10)
# plt.plot(t,Sig_Vz,color='blue',linewidth=10)
# plt.legend(['Sig_Vx','Sig_Vy','Sig_Vz'],fontsize=30)
# plt.grid(ls='-')
# plt.xticks(fontsize=30)
# plt.yticks(fontsize=30)
# plt.xlabel('Second of Week/(s)',fontsize=35)
# plt.ylabel('Std/(m/s)',fontsize=35)




plt.show()
