#!/usr/local/bin/python3
# author: zhShen
# date: 20200711
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib as mpl
import trans
import diff as df

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
	# beg=366960
	hour=time
	hour=(time-beg)/60
	diff0=np.mean(df.rms(diff[:,0]))
	diff1=np.mean(df.rms(diff[:,1]))
	diff2=np.mean(df.rms(diff[:,2]))
	# diff0=np.mean(abs(diff[:,0]))
	# diff1=np.mean(abs(diff[:,1]))
	# diff2=np.mean(abs(diff[:,2]))
	s='RMS:({0:.3f},{1:.3f},{2:.3f})m'.format(diff0,diff1,diff2)

	fig,ax=plt.subplots(1,1,figsize=(6,3),dpi=100,facecolor='w')
	# fig,ax,ax2,ax3=plt.subplots(3,1,figsize=(10,5),dpi=200,facecolor='w')
	ax.patch.set_alpha(0.5)    
	# ax.grid(linestyle=' ',linewidth=0.3, color='blue',axis='y')
	ax.grid(linestyle='--',linewidth=0.3, color='blue',axis='both')


	# ax.bar(30,-1,width=1/6,fc='lightblue',alpha=0.6)
	# ax.bar(30,1,width=1/6,fc='lightblue',alpha=0.6)
	
	# ax.bar(30.16,-1,width=3/6,fc='lightblue',alpha=0.6)
	# ax.bar(30.16,1,width=3/6,fc='lightblue',alpha=0.6)

	# ax.bar(30.4,-1,width=1,fc='lightblue',alpha=0.6)
	# ax.bar(30.4,1,width=1,fc='lightblue',alpha=0.6)

	# ax.bar(30.66,-1,width=1.5,fc='lightblue',alpha=0.6)
	# ax.bar(30.66,1,width=1.5,fc='lightblue',alpha=0.6)
	# Plo)
	ax.scatter(hour,diff[:,0],s=2,color='red',marker='o')
	ax.scatter(hour,diff[:,1],s=2,color='lime',marker='o')
	ax.scatter(hour,diff[:,2],s=2,color='blue',marker='o')
	box = ax.get_position()
	ax.set_position([box.x0, box.y0, box.width , box.height]) 

	# Label
	font1 = {'weight' : 600, 'size' : 15}
	ax.set_xlabel('Time(min)',font1)
	ax.set_ylabel('Bias(m)',font1)
	# ax.set_xticks(np.arange(0,hour[size-1]+0.2, 0.2))
	# ax.set_yticks(np.arange(-2,2.1,0.5))
	# ax.set_xticks([25,30,35,40])
	ax.set_xlim(0,68)
	# ax.set_xlim(-0.01,hour[size-1]+0.1)
	# ax.set_xlim(-0,0.25)
	# ax.set_yticks([-1.0,-0.5,0,0.5,1.0])
	# ax.set_xticklabels(['0.3','0.5','1.0'])
	# ax.set_yticklabels([-1.0,-0.5,0,0.5,1.0])
	ax.set_ylim(-2,2)
	# ax.set_ylim(-2,2)
	# ax.set_ylim(-5,5)
	# ax.set_ylim(-10,10)
	ax.tick_params(axis='y',colors='black',direction='out',labelsize=15,width=1,length=2,pad=5)
	ax.tick_params(axis='x',colors='black',direction='out',labelsize=15,width=1,length=2,pad=5)
	# labels = ax.get_xticklabels() + ax.get_yticklabels()
	# [label.set_fontname('Times New Roman') for label in labels]

	# Legend
	font2 = {'size' : 9}
	# frameon=True (边框) edgecolor='red'(边框颜色)  borderpad=0.5(内边距)bbox_to_anchor=(0.96,1.22),
	ax.legend(['East','North','Up'],loc='best',prop=font2,
		framealpha=1,facecolor='w',ncol=3,numpoints=5, markerscale=2)

	# print(s)
	# ax.text(0.01,1.04,s,bbox=dict(facecolor='none', alpha=0.1,pad=6),fontdict=font2,transform = ax.transAxes)
	# plt.savefig(name+'legend1.svg',bbox_inches = 'tight',dpi=300)

	# [xlim1,xlim2]=[25,40]
	# y=[0.3,0.3]
	# ax.plot([xlim1,xlim2],y,'--',color='blueviolet')
	# y=[0.5,0.5]
	# ax.plot([xlim1,xlim2],y,'--',color='blueviolet')
	# y=[-0.3,-0.3]
	# ax.plot([xlim1,xlim2],y,'--',color='blueviolet')
	# y=[-0.5,-0.5]
	# ax.plot([xlim1,xlim2],y,'--',color='blueviolet')


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
	# ax.grid(linestyle='--',linewidth=0.3, color='blue',axis='both')

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
	# plt.savefig(name+'.png',bbox_inches = 'tight',dpi=300,transparent='true')


def plot_att(name,time=[],diff=[]):

	# RMS
	size=len(time)
	beg=time[0]
	# beg=366960
	hour=time
	hour=(time-beg)/60
	diff0=np.mean(abs(diff[:,0]))
	diff1=np.mean(abs(diff[:,1]))
	diff2=np.mean(abs(diff[:,2]))
	s='RMS:({0:.3f},{1:.3f},{2:.3f})deg'.format(diff0,diff1,diff2)

	fig1,ax=plt.subplots(1,1,figsize=(12,6),dpi=100,facecolor='w')
	ax.patch.set_alpha(0.5)    
	# ax.grid(linestyle='--',linewidth=0.3, color='blue',axis='both')

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
	# beg=366960
	hour=time
	hour=(time-beg)/60

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

def plot_hrzn_trj(name,time=[],pos=[]):

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
	ax1 = fig.add_subplot(111)
	ax1.patch.set_alpha(0.5)    
	ax1.grid(linestyle='--',linewidth=0.3, color='blue',axis='both')
	
	# Plot
	ax1.scatter(E,N,s=15,color='green',marker='o')
	# ax1.view_init(20, -60)  # 设定视角
	# ax1.view_init(elev, azim)  # 设定视角

	# Label
	font1 = {'weight' : 600, 'size' : 12}
	ax1.set_xlabel('East(m)',font1)
	ax1.set_ylabel('North(m)',font1)
	# ax1.set_ylim(-3,3)
	ax1.tick_params(axis='both',colors='black',direction='out',labelsize=15,width=1,length=1,pad=5)

	# Legend
	font2 = {'weight' : 600, 'size' : 12}
	# frameon=True (边框) edgecolor='red'(边框颜色)  borderpad=0.5(内边距)

	# plt.savefig(name+'.png',bbox_inches = 'tight',dpi=300,transparent='true')

# def plot_hrzn_trj(pos=[],pos1=[]):

	# size=len(pos)
	# E,N,U=[],[],[]
	# [x0,y0,z0]=pos[0,:]
	# for i in range(size):
	# 	[e,n,u]=trans.xyz2enu(pos[i,:],[x0,y0,z0])
	# 	E.append(e)
	# 	N.append(n)
	# 	U.append(u)
	# # RMS
	# fig = plt.figure(figsize=(12,6),dpi=100,facecolor='w')
	# ax1 = fig.add_subplot(111)
	# ax1.patch.set_alpha(0.5)    
	# ax1.grid(linestyle='--',linewidth=0.3, color='blue',axis='both')
	# # Plot
	# ax1.scatter(N,E,s=15,color='green',marker='o')
	
	# # Label
	# font1 = {'weight' : 600, 'size' : 12}
	# ax1.set_xlabel('East(m)',font1)
	# ax1.set_ylabel('North(m)',font1)
	# # ax1.set_ylim(-3,3)
	# ax1.tick_params(axis='both',colors='black',direction='out',labelsize=15,width=1,length=1,pad=5)
	
	# size=len(pos1)
	# E,N,U=[],[],[]
	# for i in range(size):
	# 	[e,n,u]=trans.xyz2enu(pos1[i,:],[x0,y0,z0])
	# 	E.append(e)
	# 	N.append(n)
	# 	U.append(u)
	# ax1.scatter(N,E,s=15,color='red',marker='o')

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
	# beg=288005
	hour=time
	hour=(time-beg)/60
	# hour=(time-beg)/3600

	nsat=status[:,0]
	pdop=status[:,1]
	amb=status[:,2]
	# s='RMS:({0:.3f},{1:.3f},{2:.3f})m/s'.format(diff0,diff1,diff2)

	fig,ax=plt.subplots(1,1,figsize=(64.5/25.4,40/25.4),dpi=100,facecolor='w')
	ax.patch.set_alpha(0.5)    
	#ax.grid(linestyle='--',linewidth=0.3, color='blue',axis='both')
	
	# Plot NSAT
	ax.scatter(hour,nsat,s=1,marker='s',color='#0804f9',zorder=50)
	box = ax.get_position()
	ax.scatter([],[],s=1,color='#0804f9',marker='s',label='NSAT')
	ax.set_position([box.x0, box.y0, box.width , box.height]) 
	ax.set_xlim(-1,20)
	# ax.set_xlim(-0.01,hour[size-1]+0.01)
	ax.set_ylim(3,max(nsat)+1)
	font1 = {'size' : 8}
	# ax.set_xlabel('Time(min)',font1)
	# ax.set_ylabel('NSAT',font1)
	ax.tick_params(axis='both',colors='black',direction='out',labelsize=8,width=1,length=1,pad=0.5)
	ax.set_yticks([0,10,20,30])
	# ax.set_yticks([0,5,10,15,20,25,30])
	# ax.set_xticks([0,5,10,15,20])
	# ax.set_xticklabels(['0','5','10','15','20'])
	# ax.set_xticklabels(['0.3','0.5','1.0'])
	# ax.set_yticklabels([-1.0,-0.5,0,0.5,1.0])


	ax1 = ax.twinx()
	# ax1.set_ylabel('PDOP',font1)

	# Plot PDOP
	ax1.scatter(hour,pdop,s=1,color='red',marker='o',zorder=1)
	ax1.scatter([],[],s=1,color='red',marker='s',label='PDOP')
	ax1.tick_params(axis='both',colors='black',direction='out',labelsize=8,width=1,length=1,pad=0.5)
	ax1.set_ylim(0.5,6)
	ax1.set_yticks([0,2,4,6])
	# ax1.set_yticks([0,1,2,3,4,5,6])

	# # Plot AMB


	# ax3 = ax.twinx()
	# [x,y]=[[hour[i] for i in range(size) if amb[i]==0],[0.99 for i in range(size) if amb[i]==0]]
	# ax3.scatter(x,y,s=50,color='red',marker='|')
	# ax3.scatter([],[],s=20,color='red',marker='s',label='Float')
	# ax3.set_yticks(np.arange(0,1.1,0.1))
	# ax3.set_yticks([])

	# ax2 = ax.twinx()
	# [x,y]=[[hour[i] for i in range(size) if amb[i]==1],[0.99 for i in range(size) if amb[i]==1]]
	# ax2.scatter(x,y,s=50,color='lime',marker='|')
	# ax2.scatter([],[],s=20,color='lime',marker='s',label='Fixed')
	# ax2.set_yticks(np.arange(0,1.1,0.1))
	# ax2.set_yticks([])

	# ax2 = ax.twinx()
	# cmap, norm = mpl.colors.from_levels_and_colors(levels=[0, 1], colors=['red', 'lime'], extend='max')
	# ax2.scatter(hour,[0.99 for i in range(size)],s=50,c=amb,marker='s',cmap=cmap,norm=norm,label='Fixed')
	# ax2.set_yticks(np.arange(0,1.1,0.1))
	# ax2.set_yticks([])

	# Legend
	font2 = {'size' : 8}
	legend=fig.legend(bbox_to_anchor=(0.65,1.08),loc='upper right',prop=font2,
		framealpha=1,facecolor='white',ncol=5,numpoints=5, markerscale=2, handlelength=1)
# 
	plt.tight_layout(pad=0.2)
	plt.savefig(name+'2.svg',dpi=300)


def plot_f_ar_war_enu(t_f=[],enu_f=[],t_war=[],enu_war=[]):

	# s_f='RMS:({0:.3f},{1:.3f},{2:.3f})m'.format(np.mean(abs(enu_f[:,0])),np.mean(abs(enu_f[:,1])),np.mean(abs(enu_f[:,2])))
	# s_war='RMS:({0:.3f},{1:.3f},{2:.3f})m'.format(np.mean(abs(enu_war[:,0])),np.mean(abs(enu_war[:,1])),np.mean(abs(enu_war[:,2])))
	# print(s_f)
	# print(s_war)

	size=len(t_f)
	beg=t_f[0]
	hour_f=t_f
	hour_war=t_war
	hour_f=(t_f-beg)/60
	hour_war=(t_war-beg)/60

	fig1,[ax1,ax2,ax3]=plt.subplots(3,1,figsize=(84/25.4,50/25.4),dpi=100,facecolor='w')
	ax1.patch.set_alpha(0.5)    
	# ax.grid(linestyle='--',linewidth=0.3, color='blue',axis='both')


	ax1.scatter(hour_f,enu_f[:,0],color='r',s=1,zorder=50)
	ax1.scatter(hour_war,enu_war[:,0],color='g',s=1,zorder=50)
	
	ax2.scatter(hour_f,enu_f[:,1],color='r',s=1,zorder=50)
	ax2.scatter(hour_war,enu_war[:,1],color='g',s=1,zorder=50)

	ax3.scatter(hour_f,enu_f[:,2],color='r',s=1,zorder=50)
	ax3.scatter(hour_war,enu_war[:,2],color='g',s=1,zorder=50)

	# ax1.bar(0.337*60,-2,width=0.6,fc='lightblue',alpha=0.6)
	# ax1.bar(0.337*60, 2,width=0.6,fc='lightblue',alpha=0.6)
	# ax2.bar(0.337*60,-2,width=0.6,fc='lightblue',alpha=0.6)
	# ax2.bar(0.337*60, 2,width=0.6,fc='lightblue',alpha=0.6)
	# ax3.bar(0.337*60,-2,width=0.6,fc='lightblue',alpha=0.6)
	# ax3.bar(0.337*60, 2,width=0.6,fc='lightblue',alpha=0.6)

	# ax1.bar(0.405*60,-2,width=0.6,fc='lightblue',alpha=0.6)
	# ax1.bar(0.405*60, 2,width=0.6,fc='lightblue',alpha=0.6)
	# ax2.bar(0.405*60,-2,width=0.6,fc='lightblue',alpha=0.6)
	# ax2.bar(0.405*60, 2,width=0.6,fc='lightblue',alpha=0.6)
	# ax3.bar(0.405*60,-2,width=0.6,fc='lightblue',alpha=0.6)
	# ax3.bar(0.405*60, 2,width=0.6,fc='lightblue',alpha=0.6)

	# ax1.bar(0.465*60,-2,width=0.6,fc='lightblue',alpha=0.6)
	# ax1.bar(0.465*60, 2,width=0.6,fc='lightblue',alpha=0.6)
	# ax2.bar(0.465*60,-2,width=0.6,fc='lightblue',alpha=0.6)
	# ax2.bar(0.465*60, 2,width=0.6,fc='lightblue',alpha=0.6)
	# ax3.bar(0.465*60,-2,width=0.6,fc='lightblue',alpha=0.6)
	# ax3.bar(0.465*60, 2,width=0.6,fc='lightblue',alpha=0.6)

	font1 = {'size' : 9}
	[xlim1,xlim2]=[-1,20]
	# [xlim1,xlim2]=[0,hour_f[size-1]+0.5]
	[lim1,lim2]=[-2,2]
	# ax3.set_xlim(-0,hour_f[size-1]+0.01)
	ax1.tick_params(axis='y',colors='black',direction='out',labelsize=9,pad=0.5,length=1)
	ax2.tick_params(axis='y',colors='black',direction='out',labelsize=9,pad=0.5,length=1)
	ax3.tick_params(axis='both',colors='black',direction='out',labelsize=9,pad=0.5,length=1)
	ax1.set_xticks([])
	ax1.set_xlim(xlim1,xlim2)
	# ax1.set_xlim(-0,hour_f[size-1]+0.01)
	ax1.set_ylim(lim1,lim2)
	# ax1.set_ylabel('East(m)',font1)
	ax2.set_xticks([])
	ax2.set_xlim(xlim1,xlim2)
	# ax2.set_xlim(-0,hour_f[size-1]+0.01)
	ax2.set_ylim(lim1,lim2)
	# ax2.set_ylabel('North(m)',font1)
	ax3.set_xlim(xlim1,xlim2)
	# ax3.set_xlim(-0,hour_f[size-1]+0.01)
	ax3.set_ylim(lim1,lim2)
	# ax3.set_ylabel('Up(m)',font1)
	# ax3.set_xlabel('Time(min)',font1)

	ax3.set_xticks([0,5,10,15,20])


	legend=ax1.legend(['WLAF PPP','WLAF PPP/INS'],bbox_to_anchor=(1.01,1.53),loc='upper right',prop=font1,
		framealpha=1,facecolor='w',ncol=3,numpoints=5, markerscale=2, handlelength=1)
	# ax1.plot([xlim1,xlim2],y,'--',color='chartreuse')
	# ax1.plot([xlim1,xlim2],y,'--',color='lightgreen')
	# ax1.plot([xlim1,xlim2],y,'--',color='blueviolet')

	[xlim1,xlim2]=[-1,20]
	y=[0.3,0.3]
	# y=[0.5,0.5]
	ax1.plot([xlim1,xlim2],y,'--',color='blueviolet',linewidth='0.5')
	ax2.plot([xlim1,xlim2],y,'--',color='blueviolet',linewidth='0.5')
	# y=[1,1]
	y=[0.5,0.5]
	ax3.plot([xlim1,xlim2],y,'--',color='blueviolet',linewidth='0.5')
	y=[-0.3,-0.3]
	# y=[-0.5,-0.5]
	ax1.plot([xlim1,xlim2],y,'--',color='blueviolet',linewidth='0.5')
	ax2.plot([xlim1,xlim2],y,'--',color='blueviolet',linewidth='0.5')
	y=[-0.5,-0.5]
	# y=[-1,-1]
	ax3.plot([xlim1,xlim2],y,'--',color='blueviolet',linewidth='0.5')
	# ax1.text(0.01,1.1,s_f,bbox=dict(facecolor='none', alpha=0.1,pad=6),fontdict=font2,transform = ax1.transAxes)
	plt.tight_layout(pad=0.03)
	plt.savefig('GNSS_INS20201216/'+'WLAF-INS2.svg',dpi=400)





def plot_value(time=[],value=[],time1=[],value1=[]):

	# size=len(time)
	beg=time[0]
	hour=time
	# hour=(time-beg)/60
	hour1=time1
	# hour1=(time1-beg)/60
	fig,ax=plt.subplots(1,1,figsize=(2,2),dpi=100,facecolor='w')
	ax.patch.set_alpha(0.5)    
	# Plot
	ax.scatter(hour,value,color='r',marker='o',s=3)
	ax.scatter(hour1,value1,color='b',marker='o',s=3)
	box = ax.get_position()
	ax.set_position([box.x0, box.y0, box.width , box.height]) 

	ax.set_ylim(-1,1)
	# ax.set_xticks([])
	# ax.set_yticks([])
	# Label
	# font1 = {'weight' : 500, 'size' : 13}
	# ax.set_xlabel('Time(min)',font1)
	# ax.set_ylabel('East(m)',font1)
	ax.tick_params(axis='both',colors='black',direction='out',labelsize=10,width=1,length=1,pad=5)

	# Legend
	# plt.savefig('GNSS_INS20201216/'+'U.svg',bbox_inches = 'tight',dpi=300,transparent='true')


def plot_barh(float_ratio=[],war_ratio=[]):
	# namelist=['PPP-Float','PPP-WAR']
	# war_ratio=[0.975115984816533,0.897089835512442,0.6992830029523408]
	font1 = { 'name' : 'Arial', 'weight' : 600, 'size' : 15}
	fig,ax=plt.subplots(1,1,figsize=(10,5),dpi=100,facecolor='w')
	x=[0,0.15]
	y=[float_ratio[0],war_ratio[0]]
	ax.barh(x,y,hatch=' ',height=0.1,fc='r')
	y=[float_ratio[1],war_ratio[1]]
	ax.barh(x,y,hatch=' ',height=0.1,fc='b')
	y=[float_ratio[2],war_ratio[2]]
	ax.barh(x,y,hatch=' ',height=0.1,fc='g')
	# ax.barh(x,y,hatch=' ',height=0.1,fc='g',align='center',tick_label=namelist)
	ax.set_xticks([0,0.25,0.5,0.75,1])
	ax.set_yticks([])
	ax.set_xticklabels(['0','25%','50%','75%','100%'])

	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	# ax.set_ylabel(font1)
	plt.savefig('GNSS_INS20201216/'+'plot_barh.svg',bbox_inches = 'tight',dpi=300,transparent='true')

	
def plot_bar(float_ratio=[],war_ratio=[],ins_ratio=[]):
	

	# dw.plot_barh([0.9874186550976138,0.9566160520607375,0.8611713665943601],[0.90715835140997840,0.7206073752711497,0.547939262472885])

	# flt_ratio1=[0.9036,0.7178,0.5458]
	# war_ratio1=[0.9814,0.9525,0.8578]

	# flt_ratio2=[-0.7454,-0.4391,-0.1347]
	# war_ratio2=[-0.7721,-0.5378,-0.2758]

	# flt_ratio1=[0.9036,0.7178,0.5458]
	# war_ratio1=[0.9814,0.9525,0.8578]
	# ins_ratio1=[0.9914,0.9831,0.9455]

	flt_ratio2=[0.7454,0.4391,0.1347]
	war_ratio2=[0.7721,0.5378,0.2758]
	ins_ratio2=[0.9179,0.8921,0.7177]

	font1 = {'size' : 8}
	bar_width=0.23
	fig,ax=plt.subplots(1,1,figsize=(84/25.4,60/25.4),dpi=100,facecolor='w')
	ax.grid(linestyle='--',linewidth=0.3, color='blue',axis='y')
	x=np.arange(3)
	# x=np.array([0,1.5,3])

	# hth='&'
	# ax.bar(x-bar_width,flt_ratio1,width=bar_width,fc='r',label="Float PPP",hatch='/')
	# ax.bar(x,war_ratio1,width=bar_width,fc='b',label="WLAF PPP",hatch='/')
	# ax.bar(x+bar_width,ins_ratio1,width=bar_width,fc='g',label="WLAF PPP/INS",hatch='/')
	
	
	hth='-'
	ax.bar(x-bar_width,flt_ratio2,width=bar_width,fc='r',hatch='\\')
	ax.bar(x,war_ratio2,width=bar_width,fc='b',hatch='\\')
	ax.bar(x+bar_width,ins_ratio2,width=bar_width,fc='g',hatch='\\')


	ax.set_yticks([0,0.25,0.5,0.75,1])
	# ax.set_yticks([-1,-0.75,-0.5,-0.25,0,0.25,0.5,0.75,1])
	# ax.set_yticklabels(['100%','75%','50%','25%','0','25%','50%','75%','100%'])
	ax.set_yticklabels(['0','25%','50%','75%','100%'])
	ax.set_xticks([])
	# ax.set_xticklabels(['0.3','0.5','1.0'])
	# ax.set_xlabel('Boundary')
	ax.spines['bottom'].set_position(('data',0))
	# ax.spines['bottom'].set_linewidth(2)
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	# ax.spines['bottom'].set_visible(False)
	# ax.set_ylabel(font1) ,loc='best'
	ax.tick_params(axis='both',colors='black',direction='out',labelsize=8,width=1,length=1,pad=0.5)
	# ax.legend(bbox_to_anchor=(0.1,1.01),prop=font1,framealpha=1,facecolor='none',ncol=3,numpoints=5, markerscale=2, handlelength=0.5)
	font2 = {'size' : 8}
	ax.text(0.09,-0.08,'Level 1',bbox=dict(facecolor='none', alpha=0,pad=6),fontdict=font2,transform = ax.transAxes)
	ax.text(0.42,-0.08,'Level 2',bbox=dict(facecolor='none', alpha=0,pad=6),fontdict=font2,transform = ax.transAxes)
	ax.text(0.80,-0.08,'Level 3',bbox=dict(facecolor='none', alpha=0,pad=6),fontdict=font2,transform = ax.transAxes)
	plt.tight_layout(pad=0.03)
	plt.savefig('GNSS_INS20201216/'+'plot_bar21.svg',bbox_inches = 'tight',dpi=300,transparent='true')
	# plt.legend()