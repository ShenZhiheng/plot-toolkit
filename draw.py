#!/usr/local/bin/python3
# author: zhShen
# date: 20190520
import numpy as np
import matplotlib.pyplot as plt

font = {'family' : 'Arial',
		'weight' : 500,
		'size'   : 30,
}

def plot_pos(name,time=[],diff=[]):

	# RMS
	size=len(time)
	beg=time[0]
	hour=(time-beg)/3600
	diff0=np.mean(abs(diff[:,0]))
	diff1=np.mean(abs(diff[:,1]))
	diff2=np.mean(abs(diff[:,2]))
	s='RMS:({0:.3f},{1:.3f},{2:.3f})m'.format(diff0,diff1,diff2)

	fig,ax=plt.subplots(1,1,figsize=(12,6),dpi=100,facecolor='w')
	# fig,ax,ax2,ax3=plt.subplots(3,1,figsize=(10,5),dpi=200,facecolor='w')
	ax.patch.set_alpha(0.5)    
	ax.grid(linestyle='--',linewidth=0.3, color='blue',axis='both')

	# Plot
	ax.scatter(hour,diff[:,0],s=15,color='red',marker='o')
	ax.scatter(hour,diff[:,1],s=15,color='lime',marker='o')
	ax.scatter(hour,diff[:,2],s=15,color='blue',marker='o')
	box = ax.get_position()
	ax.set_position([box.x0, box.y0, box.width , box.height]) 

	# Label
	font1 = {'weight' : 600, 'size' : 15}
	ax.set_xlabel('GPS Time(hour)',font1)
	ax.set_ylabel('Position Error(m)',font1)
	# ax.set_xticks(np.arange(0,hour[size-1]+0.2, 0.2))
	# ax.set_yticks(np.arange(-2,2.1,0.5))
	ax.set_xlim(-0.1,hour[size-1]+0.1)
	ax.set_ylim(-2,2)
	# ax.set_ylim(-10,10)
	ax.tick_params(axis='both',colors='black',direction='out',labelsize=15,width=1,length=1,pad=5)
	# labels = ax.get_xticklabels() + ax.get_yticklabels()
	# [label.set_fontname('Times New Roman') for label in labels]

	# Legend
	font2 = {'weight' : 600, 'size' : 15}
	# frameon=True (边框) edgecolor='red'(边框颜色)  borderpad=0.5(内边距)
	legend=ax.legend(['East','North','Up'],bbox_to_anchor=(1.01,1.12),loc='upper right',prop=font2,
		framealpha=0.5,facecolor='none',ncol=3,numpoints=5, markerscale=2, handlelength=1)

	ax.text(0.01,1.04,s,bbox=dict(facecolor='none', alpha=0.1,pad=6),fontdict=font2,transform = ax.transAxes)
	plt.savefig(name+'.png',bbox_inches = 'tight',dpi=300,transparent='true')



def plot_vel(name,time=[],diff=[]):

	# RMS
	size=len(time)
	beg=time[0]
	hour=(time-beg)/3600
	diff0=np.mean(abs(diff[:,0]))
	diff1=np.mean(abs(diff[:,1]))
	diff2=np.mean(abs(diff[:,2]))
	s='RMS:({0:.3f},{1:.3f},{2:.3f})m/s'.format(diff0,diff1,diff2)

	fig1,ax=plt.subplots(1,1,figsize=(12,6),dpi=100,facecolor='w')
	ax.patch.set_alpha(0.5)    
	ax.grid(linestyle='--',linewidth=0.3, color='blue',axis='both')

	# Plot
	ax.scatter(hour,diff[:,0],s=15,color='red',marker='o')
	ax.scatter(hour,diff[:,1],s=15,color='lime',marker='o')
	ax.scatter(hour,diff[:,2],s=15,color='blue',marker='o')
	box = ax.get_position()
	ax.set_position([box.x0, box.y0, box.width , box.height]) 

	# Label
	font1 = {'weight' : 600, 'size' : 15}
	ax.set_xlabel('GPS Time(hour)',font1)
	ax.set_ylabel('Velocity Error(m/s)',font1)
	# ax.set_xticks(np.arange(0,hour[size-1]+0.2, 0.2))
	# ax.set_yticks(np.arange(-0.1,0.11,0.02))
	ax.set_xlim(-0.1,hour[size-1]+0.1)
	ax.set_ylim(-0.2,0.2)
	# ax.set_ylim(-1,1)
	ax.tick_params(axis='both',colors='black',direction='out',labelsize=15,width=1,length=1,pad=5)

	# Legend
	font2 = {'weight' : 600, 'size' : 15}
	# frameon=True (边框) edgecolor='red'(边框颜色)  borderpad=0.5(内边距)
	legend=ax.legend(['East','North','Up'],bbox_to_anchor=(1.01,1.12),loc='upper right',prop=font2,
		framealpha=0.5,facecolor='none',ncol=3,numpoints=5, markerscale=2, handlelength=1)

	ax.text(0.01,1.04,s,bbox=dict(facecolor='none', alpha=0.1,pad=6),fontdict=font2,transform = ax.transAxes)
	plt.savefig(name+'.png',bbox_inches = 'tight',dpi=300,transparent='true')


def plot_att(name,time=[],diff=[]):

	# RMS
	size=len(time)
	beg=time[0]
	hour=(time-beg)/3600
	diff0=np.mean(abs(diff[:,0]))
	diff1=np.mean(abs(diff[:,1]))
	diff2=np.mean(abs(diff[:,2]))
	s='RMS:({0:.3f},{1:.3f},{2:.3f})deg'.format(diff0,diff1,diff2)

	fig1,ax=plt.subplots(1,1,figsize=(12,6),dpi=100,facecolor='w')
	ax.patch.set_alpha(0.5)    
	ax.grid(linestyle='--',linewidth=0.3, color='blue',axis='both')

	# Plot
	ax.scatter(hour,diff[:,0],s=15,color='red',marker='o')
	ax.scatter(hour,diff[:,1],s=15,color='lime',marker='o')
	ax.scatter(hour,diff[:,2],s=15,color='blue',marker='o')
	box = ax.get_position()
	ax.set_position([box.x0, box.y0, box.width , box.height]) 

	# Label
	font1 = {'weight' : 600, 'size' : 15}
	ax.set_xlabel('GPS Time(hour)',font1)
	ax.set_ylabel('Attitude Error(m/s)',font1)
	# ax.set_xticks(np.arange(0,hour[size-1]+0.2, 0.2))
	# ax.set_yticks(np.arange(-0.5,0.51,0.1))
	ax.set_xlim(-0.1,hour[size-1]+0.1)
	ax.set_ylim(-1,1)
	# ax.set_ylim(-3,3)
	ax.tick_params(axis='both',colors='black',direction='out',labelsize=15,width=1,length=1,pad=5)

	# Legend
	font2 = {'weight' : 600, 'size' : 15}
	# frameon=True (边框) edgecolor='red'(边框颜色)  borderpad=0.5(内边距)
	legend=ax.legend(['Pitch','Roll','Yaw'],bbox_to_anchor=(1,1.12),loc='upper right',prop=font2,
		framealpha=0.5,facecolor='none',ncol=3,numpoints=5, markerscale=2, handlelength=1)

	ax.text(0.01,1.04,s,bbox=dict(facecolor='none', alpha=0.1,pad=6),fontdict=font2,transform = ax.transAxes)
	plt.savefig(name+'.png',bbox_inches = 'tight',dpi=300,transparent='true')


