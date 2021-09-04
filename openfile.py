#!/usr/bin/python
# author: zhShen
# date: 20200711
import numpy as np
import math
import glv
import trans

def open_flt_file(fltfile,onlyfixed=False):
	t,x,y,z,vx,vy,vz,nsat,pdop,state=[],[],[],[],[],[],[],[],[],[]
	float_num,fixed_num=0,0
	with open(fltfile,'rt') as f:
		for line in f:
			if line[0] == "#" or line[0] == "%" :
				continue
			value=line.split()
			if value[16]=='Fixed':
				# if float(value[17])>3:
				# 	continue
				fixed_num=fixed_num+1
			else:
				float_num=float_num+1
				if onlyfixed:
					continue

			# if float(value[0])<291252.0 or float(value[0])>=291252+200:
				# continue
			# if float(value[0])<289500 or float(value[0])>=290400:
				# continue
			# if float(value[0])<444000 or float(value[0])>449000:
			# if float(value[13])<8:
				# continue
			# print(line)
			t.append(float(value[0]))
			x.append(float(value[1]))
			y.append(float(value[2]))
			z.append(float(value[3]))
			vx.append(float(value[4]))
			vy.append(float(value[5]))
			vz.append(float(value[6]))
			nsat.append(float(value[13]))
			pdop.append(float(value[14]))
			if value[16]== 'Fixed':
				sta=1
			else:
				sta=0
			state.append(sta)
	time=np.array(t).T
	pos=np.array([x,y,z]).T
	vel=np.array([vx,vy,vz]).T
	status=np.array([nsat,pdop,state]).T
	pct=fixed_num/(fixed_num+float_num)
	return (time,pos,vel,status,pct)


def open_pos_file(posfile):
	t,x,y,z,nsat,state=[],[],[],[],[],[],
	with open(posfile,'rt') as f:
		for line in f:
			if line[0] == "#" or line[0] == "%" :
				continue
			value=line.split()
			# print(line)
			t.append(float(value[1]))
			x.append(float(value[2]))
			y.append(float(value[3]))
			z.append(float(value[4]))
			state.append(float(value[5]))
			nsat.append(float(value[6]))

	time=np.array(t).T
	pos=np.array([x,y,z]).T
	status=np.array([nsat,state]).T
	return (time,pos,status)

def open_enu_file(enufile,onlyfixed=False):
	t,x,y,z=[],[],[],[]
	with open(enufile,'rt') as f:
		for line in f:
			if line[0] == "#" or line[0] == "%" or line.find('RMS')>=0:
				continue
			# print(line)
			value=line.split()
			if value[4]=='Float':
				if onlyfixed:
					continue
			t.append(float(value[0]))
			x.append(float(value[1]))
			y.append(float(value[2]))
			z.append(float(value[3]))

	time=np.array(t).T
	pos=np.array([x,y,z]).T
	return (time,pos)

def open_gpgga_file(gpgga):
	t,X,Y,Z,nsat,hdop,state=[],[],[],[],[],[],[]
	count=0
	with open(gpgga,'rt') as f:
		for line in f:
			value=line.split(',')

			if(value[0] != '$GPGGA'):
				continue
			hour=float(value[1][0:2])
			min=float(value[1][2:4])
			sec=float(value[1][4:])
			if(value[2]==''):
				continue
			b_deg=float(value[2][0:2])
			b_min=float(value[2][2:])
			b=(b_deg+b_min/60)*glv.deg

			if(value[3]==''):
				continue
			l_deg=float(value[4][0:3])
			l_min=float(value[4][3:])
			l=(l_deg+l_min/60)*glv.deg
			h=float(value[9])+float(value[11])
			if(float(value[6])!=4):
				count=count+1
				continue

			[x,y,z]=trans.blh2xyz(b,l,h)
			# print(b,l_deg,l_min,h)
			# print(x,y,z)
			# print(hour,min,sec)
			t.append(hour*3600+min*60+sec+18)
			X.append(x)
			Y.append(y)
			Z.append(z)
			state.append(float(value[6]))
			nsat.append(float(value[7]))
			hdop.append(float(value[8]))

	time=np.array(t).T
	pos=np.array([X,Y,Z]).T
	status=np.array([nsat,hdop,state]).T
	print(count)
	return (time,pos,status)

def open_ins_file(insfile,onlyfixed=False):
	t,x,y,z,vx,vy,vz,pitch,roll,yaw=[],[],[],[],[],[],[],[],[],[]
	bgx,bgy,bgz,bax,bay,baz=[],[],[],[],[],[]
	with open(insfile,'rt') as f:
		for line in f:
			if line[0] == "#" or line[0] == "%" :
				continue
			value=line.split()

			# if float(value[0])<289500 or float(value[0])>=290400:
				# continue

			# if float(value[0])<289830 and float(value[0])>=289800:
			# 	continue
			if onlyfixed:
				if value[18]=='Float':
					continue
			# if float(value[16])<6:
			# 	continue
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
			bgy.append(float(value[11]))
			bgz.append(float(value[12]))
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
	float_num,fixed_num=0,0
	with open(IE_file,'rt') as f:
		for line in f:
			if line[0] == "%" or line[0] =="#":
				continue
			value=line.split()
			# print(line)
			if value[24]== 'Float':
				continue
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
			if value[24]== 'Fixed':
				sta=1
				fixed_num=fixed_num+1
			else:
				sta=0
				float_num=float_num+1
			state.append(sta)
	time=np.array(t).T
	pos=np.array([x,y,z]).T
	vel=np.array([vx,vy,vz]).T
	att=np.array([pitch,roll,yaw]).T
	pct=fixed_num/(fixed_num+float_num)
	print(pct)
	amb=np.array(state).T
	return (time,pos,vel,att,amb)
	

def open_ppprtk_file(ppprtk):
	t,x,y,z,nsat,pdop,state=[],[],[],[],[],[],[]
	with open(ppprtk,'rt') as f:
		for line in f:
			if line[0] == "#" or line[0] == "%" :
				continue
			value=line.split()
			t.append(float(value[7]))
			x.append(float(value[8]))
			y.append(float(value[9]))
			z.append(-float(value[10]))
			nsat.append(float(value[12]))
			pdop.append(float(value[11]))
	time=np.array(t).T
	pos=np.array([x,y,z]).T
	status=np.array([nsat,pdop]).T
	return (time,pos,status)



def open_aug_file(aug_file,sat_ref,sat,freq):
	t,aug1,aug2,aug3,aug4=[],[],[],[],[]
	with open(aug_file,'rt') as f:
		for line in f:
			value=line.split()
			gsat=value[5]
			gsat_ref=value[6]
			gfreq=value[7]
			if gsat==sat and gsat_ref==sat_ref and gfreq==freq:
				t.append(float(value[0]))
				aug1.append(float(value[1]))
				aug2.append(float(value[2]))
				aug3.append(float(value[3]))
				aug4.append(float(value[4]))
	time=np.array(t).T
	aug=np.array([aug1,aug2,aug3,aug4]).T
	return (time,aug)