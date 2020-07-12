#!/usr/local/bin/python3
# author: zhShen
# date: 20191120
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