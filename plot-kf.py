#!/usr/bin/python
# author: zhShen
# date: 20190520
import Cen
import glv
import trans
from numpy import *
import matplotlib.pyplot as plt

t,dax,day,daz,dve,dvn,dvu,db,dl,dh,debx,deby,debz,ddbx,ddby,ddbz=\
[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]

with open('Plane/kfx.txt','rt') as f:
	for line in f:
		value=line.split();
		if value[0]=='275000.0025':
			break;

		t.append(value[0]);
		dax.append(value[1]);
		day.append(value[2]);
		daz.append(value[3]);
		dve.append(value[4]);
		dvn.append(value[5]);
		dvu.append(value[6]);
		db.append(value[7]);
		dl.append(value[8]);
		dh.append(value[9]);
		debx.append(value[10]);
		deby.append(value[11]);
		debz.append(value[12]);
		ddbx.append(value[13]);
		ddby.append(value[14]);
		ddbz.append(value[15]);		

#attitude
plt.subplot(3,1,1);
plt.ylabel('PhiX/(arcmin)')
plt.xlabel('t/(s)');
plt.plot(t,dax);

plt.subplot(3,1,2);
plt.ylabel('PhiY/(arcmin)')
plt.xlabel('t/(s)');
plt.plot(t,day);

plt.subplot(3,1,3);
plt.ylabel('PhiZ/(arcmin)')
plt.xlabel('t/(s)');
plt.plot(t,daz);


#velocity
plt.figure();
plt.subplot(3,1,1);
plt.ylabel('Xve/(m/s)')
plt.xlabel('t/(s)');
plt.plot(t,dve);

plt.subplot(3,1,2);
plt.ylabel('Xvn/(m/s)')
plt.xlabel('t/(s)');
plt.plot(t,dvn);

plt.subplot(3,1,3);
plt.ylabel('Xnu/(m/s)')
plt.xlabel('t/(s)');
plt.plot(t,dvu);


#position
plt.figure();
plt.subplot(3,1,1);
plt.ylabel('db/(arcsec)')
plt.xlabel('t/(s)');
plt.plot(t,db);

plt.subplot(3,1,2);
plt.ylabel('dl/(arcsec)')
plt.xlabel('t/(s)');
plt.plot(t,dl);

plt.subplot(3,1,3);
plt.ylabel('dh/(m)')
plt.xlabel('t/(s)');
plt.plot(t,dh);


#eb
plt.figure();
plt.subplot(3,1,1);
plt.ylabel('debx/(deg/h)')
plt.xlabel('t/(s)');
plt.plot(t,debx);

plt.subplot(3,1,2);
plt.ylabel('deby/(deg/h)')
plt.xlabel('t/(s)');
plt.plot(t,deby);

plt.subplot(3,1,3);
plt.ylabel('debz/(deg/h)')
plt.xlabel('t/(s)');
plt.plot(t,debz);


#db
plt.figure();
plt.subplot(3,1,1);
plt.ylabel('ddbx/(ug)')
plt.xlabel('t/(s)');
plt.plot(t,ddbx);

plt.subplot(3,1,2);
plt.ylabel('ddby/(ug)')
plt.xlabel('t/(s)');
plt.plot(t,ddby);

plt.subplot(3,1,3);
plt.ylabel('ddbz/(ug)')
plt.xlabel('t/(s)');
plt.plot(t,ddbz);



plt.show();