#!/usr/bin/python
# author: zhShen
# date: 20190520
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


def xyz2enu(XYZ=[],XYZ_Ref=[]):

    [b,l,h]=xyz2blh(XYZ[0],XYZ[1],XYZ[2])

    r=[XYZ[0]-XYZ_Ref[0], XYZ[1]-XYZ_Ref[1], XYZ[2]-XYZ_Ref[2]]


    sinPhi = sin(b);
    cosPhi = cos(b);
    sinLam = sin(l);
    cosLam = cos(l);

    E = -sinPhi * cosLam * r[0] - sinPhi * sinLam * r[1] + cosPhi * r[2];
    N = -sinLam * r[0] + cosLam * r[1];
    U = +cosPhi * cosLam * r[0] + cosPhi * sinLam * r[1] + sinPhi * r[2];

    return array([E,N,U])



# int xyz2neu(const double* XYZ, const double* XYZ_Ref, double* neu)
#     {
#         double ele[3];
#         xyz2ell(XYZ_Ref, ele, false);

#         ColumnVector r(3);

#         r << XYZ[0] - XYZ_Ref[0] << XYZ[1] - XYZ_Ref[1] << XYZ[2] - XYZ_Ref[2];

#         double sinPhi = sin(ele[0]);
#         double cosPhi = cos(ele[0]);
#         double sinLam = sin(ele[1]);
#         double cosLam = cos(ele[1]);



#         neu[0] = -sinPhi * cosLam * r(1)
#             - sinPhi * sinLam * r(2)
#             + cosPhi * r(3);

#         neu[1] = -sinLam * r(1)
#             + cosLam * r(2);

#         neu[2] = +cosPhi * cosLam * r(1)
#             + cosPhi * sinLam * r(2)
#             + sinPhi * r(3);

#         return 1;
#     }

