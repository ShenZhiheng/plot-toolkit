#!/usr/bin/python
# author: zhShen
# date: 20190920
#coding:utf8
import numpy as np

def Cne(B,L):
    res=np.mat(np.zeros((3,3)));

    slat = np.sin(B); 
    clat = np.cos(B);
    slon = np.sin(L); 
    clon = np.cos(L);
    res = np.matrix([[ -slon,clon,0 ],
          [ -slat*clon, -slat*slon, clat],
          [  clat*clon,  clat*slon, slat]])
    return res;