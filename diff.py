#!/usr/local/bin/python3
# author: zhShen
# date: 20200711
import sys 
sys.path.append("..")
import numpy as np
import Bound as bd
import math
import trans
import glv

def diff_enu(t1=[],xyz=[],t2=[],xyz_ref=[]):
	t,E,N,U=[],[],[],[]
	cnt=0
	for i in range(len(t1)):
		index=bd.lower_bound(t2,t1[i])
		# print(t1[i],t2[index])
		# print(xyz[i],xyz_ref[index])
		if abs(t1[i]-t2[index])>1e-2:
			continue
		[e,n,u]=trans.xyz2enu(xyz[i],xyz_ref[index])
		# if t1[i]>=289890 and abs(e)< 0.3 and abs(n)<0.3 and abs(u)<0.5:
		# 	cnt=cnt+1
		# else:
		# 	cnt=0
		# print(t1[i],e,n,u)
		# if(cnt>=30):
		# 	tgt=t1[i]-30
		# 	print(tgt,(tgt-289890))
		# if t1[i]>289797 and t1[i]<289797+200:
		# print(t1[i],e,n,u)
		# [e,n,u]=(xyz[i]-xyz_ref[index])
		t.append(t1[i])
		E.append(e)
		N.append(n)
		U.append(u)
	time=np.array(t).T
	diff=np.array([E,N,U]).T
	return(time,diff)
	
# def diff_enu(xyz_ref,t1=[],xyz=[]):
# 	t,E,N,U=[],[],[],[]
# 	for i in range(len(t1)):
# 		t.append(t1[i])
# 		[e,n,u]=trans.xyz2enu(xyz[i],xyz_ref)
# 		E.append(e)
# 		N.append(n)
# 		U.append(u)
# 	time=np.array(t).T
# 	diff=np.array([E,N,U]).T
# 	return(time,diff)

def diff_enu25(t1=[],xyz=[],t2=[],xyz_ref=[]):
	t,E,N,U=[],[],[],[]
	for i in range(len(t1)):
		index=bd.lower_bound(t2,t1[i])
		index=index-1
		# print(t1[i],t2[index])
		if abs(t1[i]-t2[index]-0.0025)>1e-6:
			continue
		t.append(t1[i])
		# print(t1[i],t2[index])
		[e,n,u]=trans.xyz2enu(xyz[i],xyz_ref[index])
		E.append(e)
		N.append(n)
		U.append(u)
	time=np.array(t).T
	diff=np.array([E,N,U]).T
	return(time,diff)

def diff_vel(t1=[],vel=[],t2=[],vel_ref=[]):
	t,E,N,U=[],[],[],[]
	for i in range(len(t1)):
		index=bd.lower_bound(t2,t1[i])
		if abs(t1[i]-t2[index])>1e-6:
			continue
		# print(vel[i],vel_ref[index])
		[e,n,u]=vel[i]-vel_ref[index]
		# if abs(e)> 0.03 or abs(n)>0.03 or abs(u)>0.03:
			# continue
		t.append(t1[i])
		E.append(e)
		N.append(n)
		U.append(u)
	time=np.array(t).T
	diff=np.array([E,N,U]).T
	return(time,diff)


def diff_att(t1=[],att=[],t2=[],att_ref=[]):
	t,p,r,y=[],[],[],[]
	for i in range(len(t1)):
		index=bd.lower_bound(t2,t1[i])
		if abs(t1[i]-t2[index])>1e-6:
			continue
		t.append(t1[i])
		[pp,rr,yy]=att[i]-att_ref[index]
		if abs(yy) > 100:
			yy=0
		p.append(pp)
		r.append(rr)
		y.append(yy)
	time=np.array(t).T
	diff=np.array([p,r,y]).T
	return(time,diff)


def correct_base(xyz=[],div_ref=[],plus_ref=[]):
    x=xyz[:,0]-div_ref[0]+plus_ref[0]
    y=xyz[:,1]-div_ref[1]+plus_ref[1]
    z=xyz[:,2]-div_ref[2]+plus_ref[2]
    xyz_corrected=np.array([x,y,z]).T
    return xyz_corrected


def available(threshold,diff=[]):
	size=len(diff)
	ava=0
	for i in range(size):
		x=abs(diff[i,0])
		y=abs(diff[i,1])
		z=abs(diff[i,2])
		if x<threshold and y<threshold and z<0.5 :
			ava=ava+1
	return ava

def rms3(diff=[]):
	r1=rms(diff[:,0])
	r2=rms(diff[:,1])
	r3=rms(diff[:,2])
	s='RMS:({0:.3f},{1:.3f},{2:.3f})m'.format(r1,r2,r3)
	print(s)


def rms(diff=[]):
	size=len(diff)
	sum=0
	for i in range(size):
		sum=sum+diff[i]*diff[i]
	return math.sqrt(sum/size)
