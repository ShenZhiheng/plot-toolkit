#!/usr/bin/python
# author: zhShen
# date: 20190920
#coding:utf8
import trans
import glv
import Cne
import numpy as np


t,B,L,H,Ve,Vn,Vu=[],[],[],[],[],[],[]
X,Y,Z,Vx,Vy,Vz=[],[],[],[],[],[]
b,l,h,x,y,z=0,0,0,0,0,0
PDOP,nSat=0,0

with open('HOLO20190618/xyzfileif.pos','rt') as f:
	for line in f:
		value=line.split()

		x=float(value[1])
		y=float(value[2])
		z=float(value[3])
		vx=float(value[13])
		vy=float(value[14])
		vz=float(value[15])
		# nSat=float(value[13])
		# PDOP=float(value[14])

		# if PDOP > 3 or nSat < 6:
		# 	continue
		[b,l,h]=trans.xyz2blh(x,y,z)
		v=np.array([[vx,vy,vz]]).transpose()
		[ve,vn,vu]=(Cne.Cne(b,l)*v)

		t.append(float(value[0]))
		B.append(b/glv.deg)
		L.append(l/glv.deg)
		H.append(h)
		Ve.append(ve[0,0])
		Vn.append(vn[0,0])
		Vu.append(vu[0,0])



with open('HOLO20190618/rtk.odo','wt') as f:
	for i in range(len(t)):
		# s='{0:<10}  {1:<15}  {2:<15}  {3:<15}  {4:>5}  {5:>5}  {6:>5}  {7:>15}  {8:>15}  {9:>15}  '\
		# .format(t[i],B[i],L[i],H[i],0,0,0,Ve[i],Vn[i],Vu[i])
		s='{0:.4f}  {1:.6f}  {2:.6f}  {3:.4f}  {4:.2f}  {5:.2f}  {6:.2f}  {7:.4f}  {8:.4f}  {9:.4f}  '\
		.format(t[i],B[i],L[i],H[i],0,0,0,Ve[i],Vn[i],Vu[i])
		f.writelines(s+'\n')



