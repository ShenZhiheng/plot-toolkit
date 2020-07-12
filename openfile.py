#!/usr/bin/python
# author: zhShen
# date: 20190920
import numpy as np
import math

def open_flt_file(fltfile):
	t,x,y,z,vx,vy,vz,nsat,pdop,state=[],[],[],[],[],[],[],[],[],[]
	with open(fltfile,'rt') as f:
		for line in f:
			if line[0] == "#" or line[0] == "%" :
				continue
			value=line.split()
			t.append(float(value[0]))
			x.append(float(value[1]))
			y.append(float(value[2]))
			z.append(float(value[3]))
			vx.append(float(value[4]))
			vy.append(float(value[5]))
			vz.append(float(value[6]))
			nsat.append(float(value[13]))
			pdop.append(float(value[14]))
			state.append(value[16])
	time=np.array(t).T
	pos=np.array([x,y,z]).T
	vel=np.array([vx,vy,vz]).T
	status=np.array([nsat,pdop,state]).T
	return (time,pos,vel,status)



def open_ins_file(insfile):
	t,x,y,z,vx,vy,vz,pitch,roll,yaw=[],[],[],[],[],[],[],[],[],[]
	bgx,bgy,bgz,bax,bay,baz=[],[],[],[],[],[]
	with open(insfile,'rt') as f:
		for line in f:
			if line[0] == "#" or line[0] == "%" :
				continue
			value=line.split()
			t.append(float(value[0]))
			x.append(float(value[1]))
			y.append(float(value[2]))
			z.append(float(value[3]))
			vx.append(float(value[4]))
			vy.append(float(value[5]))
			vz.append(float(value[6]))
			pitch.append(float(value[7]))
			roll.append(float(value[8]))
			yaw.append(float(value[9]))
			bgx.append(float(value[10]))
			bgx.append(float(value[11]))
			bgx.append(float(value[12]))
			bax.append(float(value[13]))
			bay.append(float(value[14]))
			baz.append(float(value[15]))
	time=np.array(t).T
	pos=np.array([x,y,z]).T
	vel=np.array([vx,vy,vz]).T
	att=np.array([pitch,roll,yaw]).T
	bias=np.array([bgx,bgy,bgz,bax,bay,baz]).T
	return (time,pos,vel,att,bias)


def open_IE_file(IE_file):
	t,x,y,z,vx,vy,vz,pitch,roll,yaw,state=[],[],[],[],[],[],[],[],[],[],[]
	with open(IE_file,'rt') as f:
		for line in f:
			if line[0] == "%" or line[0] =="#":
				continue
			value=line.split()
			# if value[24]== 'Float':
				# continue
			t.append(float(value[1]))
			x.append(float(value[2]))
			y.append(float(value[3]))
			z.append(float(value[4]))
			vx.append(float(value[12]))
			vy.append(float(value[13]))
			vz.append(float(value[14]))
			yaw.append(float(value[21]))
			pitch.append(float(value[22]))
			roll.append(float(value[23]))
			state.append(value[24])
	time=np.array(t).T
	pos=np.array([x,y,z]).T
	vel=np.array([vx,vy,vz]).T
	att=np.array([pitch,roll,yaw]).T
	amb=np.array(state).T
	return (time,pos,vel,att,amb)
	
