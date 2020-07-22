#!/usr/local/bin/python3
# author: zhShen
# date: 20200711
import sys 
sys.path.append("..")
import numpy as np
import Bound as bd
import trans
import glv

def diff_enu(t1=[],xyz=[],t2=[],xyz_ref=[]):
	t,E,N,U=[],[],[],[]
	for i in range(len(t1)):
		index=bd.lower_bound(t2,t1[i])
		if abs(t1[i]-t2[index])>1e-6:
			continue
		t.append(t1[i])
		[e,n,u]=trans.xyz2enu(xyz[i],xyz_ref[index])
		E.append(e)
		N.append(n)
		U.append(u)
	time=np.array(t).T
	diff=np.array([E,N,U]).T
	return(time,diff)

def diff_enu25(t1=[],xyz=[],t2=[],xyz_ref=[]):
	t,E,N,U=[],[],[],[]
	for i in range(len(t1)):
		index=bd.lower_bound(t2,t1[i])
		index=index-1
		if abs(t1[i]-t2[index]-0.0025)>1e-6:
			continue
		t.append(t1[i])
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
		t.append(t1[i])
		[e,n,u]=vel[i]-vel_ref[index]
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
		if x<threshold and y<threshold and z<threshold :
			ava=ava+1
	return ava