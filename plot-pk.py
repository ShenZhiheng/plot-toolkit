#!/usr/bin/python
import Cen
import glv
import trans
from numpy import *
import matplotlib.pyplot as plt

t,Pax,Pay,Paz,Pve,Pvn,Pvu,Pb,Pl,Ph,Pebx,Peby,Pebz,Pdbx,Pdby,Pdbz=\
[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]

with open('FSAS20190113/tci_kfp.txt','rt') as f:
	for line in f:
		value=line.split();
		t.append(value[0]);
		Pax.append(value[1]);
		Pay.append(value[2]);
		Paz.append(value[3]);
		Pve.append(value[4]);
		Pvn.append(value[5]);
		Pvu.append(value[6]);
		Pb.append(value[7]);
		Pl.append(value[8]);
		Ph.append(value[9]);
		Pebx.append(value[10]);
		Peby.append(value[11]);
		Pebz.append(value[12]);
		Pdbx.append(value[13]);
		Pdby.append(value[14]);
		Pdbz.append(value[15]);		

#attitude
plt.subplot(3,1,1);
plt.ylabel('PhiX/(arcmin)')
plt.xlabel('t/(s)');
plt.plot(t,Pax);

plt.subplot(3,1,2);
plt.ylabel('PhiY/(arcmin)')
plt.xlabel('t/(s)');
plt.plot(t,Pay);

plt.subplot(3,1,3);
plt.ylabel('PhiZ/(arcmin)')
plt.xlabel('t/(s)');
plt.plot(t,Paz);


#velocity
plt.figure();
plt.subplot(3,1,1);
plt.ylabel('Xve/(m/s)')
plt.xlabel('t/(s)');
plt.plot(t,Pve);

plt.subplot(3,1,2);
plt.ylabel('Xvn/(m/s)')
plt.xlabel('t/(s)');
plt.plot(t,Pvn);

plt.subplot(3,1,3);
plt.ylabel('Xnu/(m/s)')
plt.xlabel('t/(s)');
plt.plot(t,Pvu);


#position
plt.figure();
plt.subplot(3,1,1);
plt.ylabel('Pb/(arcsec)')
plt.xlabel('t/(s)');
plt.plot(t,Pb);

plt.subplot(3,1,2);
plt.ylabel('Pl/(arcsec)')
plt.xlabel('t/(s)');
plt.plot(t,Pl);

plt.subplot(3,1,3);
plt.ylabel('Ph/(m)')
plt.xlabel('t/(s)');
plt.plot(t,Ph);


#eb
plt.figure();
plt.subplot(3,1,1);
plt.ylabel('Pebx/(deg/h)')
plt.xlabel('t/(s)');
plt.plot(t,Pebx);

plt.subplot(3,1,2);
plt.ylabel('Peby/(deg/h)')
plt.xlabel('t/(s)');
plt.plot(t,Peby);

plt.subplot(3,1,3);
plt.ylabel('Pebz/(deg/h)')
plt.xlabel('t/(s)');
plt.plot(t,Pebz);


#Pb
plt.figure();
plt.subplot(3,1,1);
plt.ylabel('dPbx/(ug)')
plt.xlabel('t/(s)');
plt.plot(t,Pdbx);

plt.subplot(3,1,2);
plt.ylabel('dPby/(ug)')
plt.xlabel('t/(s)');
plt.plot(t,Pdby);

plt.subplot(3,1,3);
plt.ylabel('dPbz/(ug)')
plt.xlabel('t/(s)');
plt.plot(t,Pdbz);



plt.show();