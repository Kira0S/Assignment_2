#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 14:11:47 2018

@author: ciaraosullivan
"""
nx = 10*2**5
ngc = 1
bc = 'ini'
inicond='shock tube'
tmax = 0.2
rho_1 = 8
v_1 = 0
P_1 = 8
rho_2 = 1
v_2 = 0
P_2 = 1 
nw =3
ndim=1
xmin1=-0.5
xmax1=0.5
dx =(xmax1-xmin1)/(nx)
cfl=0.4
gamma=1.4
#dtsave = tamx/Nsnap
#filename_base = trim(iniCond)//'snapshots'
#file_index
#eoc_file='EOC.dat'
#chrono_o_mess ='chrono_0'
#smalldble =1.
#one =1.
#dpi=dacos(-1.)
#cv_analysis = .false.
#nsnap = 30