#!/usr/bin/python
# author: zhShen
# date: 20190920
import numpy as np
import math

sow=[]
data=[]

with open('sbg/Documents.txt','rt') as f:
	for line in f:
		if line[0]=='%':
			continue
		value=line.split()
		end=len(line)
		index=line.find(':')
		hms=line[index-2:index+10].split(':')
		ga=line[index+11:end-1]
		h=int(hms[0])
		m=int(hms[1])
		s=float(hms[2])

		sow.append(86400*2+h*3600+m*60+s)
		data.append(ga)
		# f.append((value[5]));

print sow

with open('sbg.txt','wt') as f:
	for i in range(len(sow)):
		s='{0:.4f}   {1}'\
		.format(sow[i],data[i])
		f.writelines(s+'\n')


