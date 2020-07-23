#!/usr/local/bin/python3
# author: zhShen
# date: 20200711
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib as mpl
import trans

font = {'family' : 'Arial',
		'weight' : 500,
		'size'   : 30,
}

clr = { 0 : 'red',
		1 : 'green',
}

def plot_pos(name,time=[],diff=[]):

	# RMS
	size=len(time)
	beg=time[0]
	# hour=time
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
	ax.set_ylim(-1,1)
	# ax.set_ylim(-2,2)
	# ax.set_ylim(-5,5)
	# ax.set_ylim(-10,10)
	ax.tick_params(axis='both',colors='black',direction='out',labelsize=15,width=1,length=1,pad=5)
	# labels = ax.get_xticklabels() + ax.get_yticklabels()
	# [label.set_fontname('Times New Roman') for label in labels]

	# Legend
	font2 = {'weight' : 600, 'size' : 15}
	# frameon=True (边框) edgecolor='red'(边框颜色)  borderpad=0.5(内边距)
	legend=ax.legend(['East','North','Up'],bbox_to_anchor=(1.01,1.12),loc='upper right',prop=font2,
		framealpha=0.5,facecolor='none',ncol=3,numpoints=5, markerscale=2, handlelength=1)

	print(s)
	ax.text(0.01,1.04,s,bbox=dict(facecolor='none', alpha=0.1,pad=6),fontdict=font2,transform = ax.transAxes)
	# plt.savefig(name+'.png',bbox_inches = 'tight',dpi=300,transparent='true')


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
	# ax.set_ylim(-0.5,0.5)
	# ax.set_ylim(-1,1)
	# ax.set_ylim(-3,3)
	ax.tick_params(axis='both',colors='black',direction='out',labelsize=15,width=1,length=1,pad=5)

	# Legend
	font2 = {'weight' : 600, 'size' : 15}
	# frameon=True (边框) edgecolor='red'(边框颜色)  borderpad=0.5(内边距)
	legend=ax.legend(['Pitch','Roll','Yaw'],bbox_to_anchor=(1,1.12),loc='upper right',prop=font2,
		framealpha=0.5,facecolor='none',ncol=3,numpoints=5, markerscale=2, handlelength=1)

	ax.text(0.01,1.04,s,bbox=dict(facecolor='none', alpha=0.1,pad=6),fontdict=font2,transform = ax.transAxes)
	# plt.savefig(name+'.png',bbox_inches = 'tight',dpi=300,transparent='true')


def plot_bias(name,time=[],bias=[]):

	# RMS
	size=len(time)
	beg=time[0]
	hour=(time-beg)/3600

	fig,[ax1,ax2]=plt.subplots(2,1,figsize=(12,6),dpi=100,facecolor='w')
	ax1.patch.set_alpha(0.5)    
	ax1.grid(linestyle='--',linewidth=0.3, color='blue',axis='both')

	# Plot
	ax1.scatter(hour,bias[:,0],s=15,color='red',marker='o')
	ax1.scatter(hour,bias[:,1],s=15,color='lime',marker='o')
	ax1.scatter(hour,bias[:,2],s=15,color='blue',marker='o')
	box = ax1.get_position()
	ax1.set_position([box.x0, box.y0, box.width , box.height]) 

	# Label
	font1 = {'weight' : 600, 'size' : 12}
	ax1.set_ylabel('Gyroscope Bias(deg/h)',font1,labelpad=12)
	ax1.set_yticks(np.arange(0,7,1.5))
	# ax1.set_ylim(-3,3)
	ax1.tick_params(axis='both',colors='black',direction='out',labelsize=15,width=1,length=1,pad=5)

	# Legend
	font2 = {'weight' : 600, 'size' : 12}
	legend=ax1.legend(['x','y','z'],bbox_to_anchor=(1,1.2),loc='upper right',prop=font2,
		framealpha=0.5,facecolor='none',ncol=3,numpoints=5, markerscale=2, handlelength=1)


	ax2.patch.set_alpha(0.5)    
	ax2.grid(linestyle='--',linewidth=0.3, color='blue',axis='both')

	# Plot
	ax2.scatter(hour,bias[:,3],s=15,color='red',marker='o')
	ax2.scatter(hour,bias[:,4],s=15,color='lime',marker='o')
	ax2.scatter(hour,bias[:,5],s=15,color='blue',marker='o')
	box = ax2.get_position()
	ax2.set_position([box.x0, box.y0, box.width , box.height]) 

	# Label
	ax2.set_xlabel('GPS Time(hour)',font1)
	ax2.set_ylabel('Accelerator Bias(mg)',font1,labelpad=12)
	# ax2.set_xticks(np.arange(0,hour[size-1]+0.2, 0.2))
	ax2.set_yticks(np.arange(0,1.1,0.2))
	ax2.tick_params(axis='both',colors='black',direction='out',labelsize=15,width=1,length=1,pad=5)
	# plt.savefig(name+'.png',bbox_inches = 'tight',dpi=300,transparent='true')


def plot_trj(name,time=[],pos=[]):

	size=len(time)
	E,N,U=[],[],[]
	[x0,y0,z0]=pos[0,:]
	for i in range(size):
		[e,n,u]=trans.xyz2enu(pos[i,:],[x0,y0,z0])
		E.append(e)
		N.append(n)
		U.append(u)
	# RMS
	fig = plt.figure(figsize=(12,6),dpi=100,facecolor='w')
	ax1 = fig.add_subplot(111, projection='3d')
	ax1.patch.set_alpha(0.5)    
	ax1.grid(linestyle='--',linewidth=0.3, color='blue',axis='both')
	
	# Plot
	ax1.scatter3D(N,E,U,s=15,color='green',marker='o')
	ax1.view_init(20, -60)  # 设定视角
	# ax1.view_init(elev, azim)  # 设定视角

	# Label
	font1 = {'weight' : 600, 'size' : 12}
	ax1.set_zlabel('Up(m)',font1,labelpad=20)
	ax1.set_ylabel('North(m)',font1,labelpad=20)
	ax1.set_xlabel('East(m)',font1,labelpad=20)
	# ax1.set_ylim(-3,3)
	ax1.tick_params(axis='both',colors='black',direction='out',labelsize=15,width=1,length=1,pad=5)

	# Legend
	font2 = {'weight' : 600, 'size' : 12}
	# frameon=True (边框) edgecolor='red'(边框颜色)  borderpad=0.5(内边距)

	# plt.savefig(name+'.png',bbox_inches = 'tight',dpi=300,transparent='true')


def plot_sat_pdop(name,time=[],status=[]):

	# RMS
	size=len(time)
	beg=time[0]
	hour=(time-beg)/3600

	nsat=status[:,0]
	pdop=status[:,1]
	amb=status[:,2]
	# s='RMS:({0:.3f},{1:.3f},{2:.3f})m/s'.format(diff0,diff1,diff2)

	fig,ax=plt.subplots(1,1,figsize=(14,6),dpi=100,facecolor='w')
	ax.patch.set_alpha(0.5)    
	ax.grid(linestyle='--',linewidth=0.3, color='blue',axis='both')
	
	# Plot NSAT
	ax.scatter(hour,nsat,s=15,color='#0804f9',marker='s',zorder=50,label='NSAT')
	box = ax.get_position()
	ax.set_position([box.x0, box.y0, box.width , box.height]) 
	ax.set_xlim(-0.1,hour[size-1]+0.1)
	ax.set_ylim(0,max(nsat)+1)
	font1 = {'weight' : 600, 'size' : 15}
	ax.set_xlabel('GPS Time(hour)',font1)
	ax.set_ylabel('Number of Satellite',font1)
	ax.tick_params(axis='both',colors='black',direction='out',labelsize=15,width=1,length=1,pad=5)

	ax1 = ax.twinx()
	ax1.set_ylabel('PDOP',font1)

	# Plot PDOP
	ax1.scatter(hour,pdop,s=15,color='#cf1b1b',marker='o',zorder=1,label='PDOP')
	ax1.tick_params(axis='both',colors='black',direction='out',labelsize=15,width=1,length=1,pad=5)
	ax.set_ylim(1,)

	# # Plot AMB
	ax2 = ax.twinx()
	[x,y]=[[hour[i] for i in range(size) if amb[i]==1],[0.99 for i in range(size) if amb[i]==1]]
	# ax2.scatter(x,y,s=50,color='lime',marker='|')
	ax2.scatter(x,y,s=100,color='lime',marker='|')
	ax2.scatter([],[],s=20,color='lime',marker='s',label='Fixed')
	ax2.set_yticks(np.arange(0,1.1,0.1))
	ax2.set_yticks([])

	ax3 = ax.twinx()
	[x,y]=[[hour[i] for i in range(size) if amb[i]==0],[0.99 for i in range(size) if amb[i]==0]]
	ax3.scatter(x,y,s=100,color='red',marker='|')
	ax3.scatter([],[],s=20,color='red',marker='s',label='Float')
	ax3.set_yticks(np.arange(0,1.1,0.1))
	ax3.set_yticks([])


	# ax2 = ax.twinx()
	# cmap, norm = mpl.colors.from_levels_and_colors(levels=[0, 1], colors=['red', 'lime'], extend='max')
	# ax2.scatter(hour,[0.99 for i in range(size)],s=50,c=amb,marker='s',cmap=cmap,norm=norm,label='Fixed')
	# ax2.set_yticks(np.arange(0,1.1,0.1))
	# ax2.set_yticks([])

	# Legend
	font2 = {'weight' : 600, 'size' : 15}
	legend=fig.legend(bbox_to_anchor=(0.5,0.98),loc='upper right',prop=font2,
		framealpha=0.5,facecolor='none',ncol=5,numpoints=5, markerscale=2, handlelength=1)

	plt.savefig(name+'.png',bbox_inches = 'tight',dpi=300,transparent='true')

