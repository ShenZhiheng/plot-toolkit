#!/usr/bin/python
import Cen
import glv
import trans

[x,y,z]=trans.blh2xyz((39+29/60+ 34.88249/3600)*glv.deg,(109+51/60+ 52.01747/3600)*glv.deg,1363.838);
# [b,l,h]=trans.xyz2blh( -323105.2290 ,-5531622.4390  ,3148081.9020 );


print x,y,z



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
