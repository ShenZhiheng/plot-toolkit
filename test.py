#!/usr/bin/python
# author: zhShen
# date: 20190520
import Cne
import glv
import trans


[x,y,z]=trans.blh2xyz((30+27.0/60.0+41.49673/3600.0)*glv.deg,(114+28.0/60.0+47.91331/3600.0)*glv.deg,37.817)
         
# [x,y,z]=trans.blh2xyz((40.058778)*glv.deg,(116.477409)*glv.deg,26.136309);
# 30 24 31.70819, 114 16 12.18277, 22.754
# 30 27 41.49673, 114 28 47.91331, 37.817
[b,l,h]=trans.xyz2blh( -2280114.342488 ,5007885.038898 , 3214597.404017);


Cne=Cne.Cne(0.532809967326,1.99589996779)

# print Cne

print x,y,z,b/glv.deg,l/glv.deg,h

[p,r,y]=(0.000791/glv.deg,0.022679/glv.deg,0.304539/glv.deg)

print p,r,y



# X,Y,Z=[],[],[]
# B,L,H=[],[],[]

# with open('XYZ.txt','rt') as f:
# 	for line in f:
# 		value=line.split();
# 		[b,l,h]=trans.xyz2blh(float(value[0]) ,float(value[1]),float(value[2]))
# 		X.append(value[0])
# 		B.append(b)
# 		L.append(l)
# 		H.append(h)


# with open('BLH.txt','wt') as f:
# 	for i in range(len(X)):
# 		f.writelines(str(B[i])+'  '+str(L[i])+'  '+str(H[i])+'  '+'\n');
