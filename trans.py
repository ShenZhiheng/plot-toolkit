#!/usr/bin/python
import glv
from math import *
from numpy import *

def blh2xyz(B,L,H):
    sB = sin(B);
    cB = cos(B);
    sL = sin(L);
    cL = cos(L);
    N = glv.a/sqrt(1-glv.e2*sB**2);
    X = (N+H)*cB*cL;
    Y = (N+H)*cB*sL;
    Z = (N*(1-glv.e2)+H)*sB;
    return array([X,Y,Z]);

def xyz2blh(X,Y,Z):
    bell = glv.a*(1.0-1.0/glv.f);                          
    ss = sqrt(X*X+Y*Y);   
    zps   = Z/ss;
    theta = atan( (Z*glv.a) / (ss*glv.b) );
    sin3  = sin(theta) * sin(theta) * sin(theta);
    cos3  = cos(theta) * cos(theta) * cos(theta);
    
    #Closed formula
    B = atan((Z + glv.ep2 * glv.b * sin3) / (ss - glv.e2 * glv.a * cos3));
    L = atan2(Y,X);
    nn = glv.a/sqrt(1.0-glv.e2*sin(B)*sin(L));
    H = ss/cos(B) - nn;

    i=0;
    while i<=100:
        nn = glv.a/sqrt(1.0-glv.e2*sin(B)*sin(B));
        hOld = H;
        phiOld = B;
        H = ss/cos(B)-nn;
        B = atan(zps/(1.0-glv.e2*nn/(nn+H)));
        if abs(phiOld-B) <= 1.0e-11 and abs(hOld-H) <= 1.0e-5:
            # always convert longitude to 0-360
            if L < 0.0 :
                L += 2 * pi;
                break;

        i+=1;


    return array([B,L,H])


