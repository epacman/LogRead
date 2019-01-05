# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 10:08:07 2017

@author: elindgre
"""


import csv
import matplotlib.pyplot as plt
import numpy as np
import pylab
from mpl_toolkits.mplot3d import Axes3D

#Config
filename = 'langt_stora_holm_fixed.csv' 

#Vilken column är vad
rpmcol = 5
timingcol = 4
loadcol = 7
vspdcol = 99
boostcol = 11
thrcol = 6

#Sample rate
sample_rate = 0.01

#_____________________________________________________________________





#skapa tomma
rownum = 0
rpm = []
timing = []
rpm_temp = 0
timing_temp = 0
vspd = []
vspd_temp = 0
load = []
load_temp = 0
boost = []
boost_temp = 0
thr = []
thr_temp = 0

rpm_short = []
timing_short = []
load_short = []
boost_short = []
thr_short = []



ifile = open(filename, 'rb')
reader = csv.reader(ifile)


#main loop, en csv-rad i taget
for row in reader:
	#om första raden, plocka ut text
    if rownum == 0:
        header=row
    else:
        colnum = 0
        for col in row:
        	#om RPM-kolumn
            if colnum == rpmcol:
                if col == '-':
                    rpm_temp = 0
                else:
                    rpm_temp = float(col)
                #lägg till i RPM-vektor
                rpm.append(rpm_temp)
            if colnum == vspdcol:
                vspd_temp = float(col)
                vspd.append(vspd_temp)
            if colnum == boostcol:
                boost_temp = float(col)
                boost.append(boost_temp)
            #om timing-kolumn
            if colnum == timingcol:
                timing_temp = float(col)
                timing.append(timing_temp)    
            if colnum == loadcol:
                if col == '-':
                    load_temp = 0
                else:
                    load_temp = float(col)
                    load.append(load_temp) 
            if colnum == thrcol:
                thr_temp = float(col)
                thr.append(thr_temp)  
                
            colnum += 1
    rownum +=1
    
ifile.close()

#Skapa tidsvektor
time = np.zeros(rownum-1)
for tick in range(len(time)):
    time[tick] = tick * sample_rate
    
    
upper_load = 500
lower_load = 30 


for rad in range(len(time)):
    
    #conditions
    cnd1 = load[rad] < upper_load
    cnd2 = load[rad]  > lower_load
    cnd4 = timing[rad] > 5
    cnd3 = abs(boost[rad] - boost[rad-2]) < 10000
    cnd5 = rpm[rad] > 1500
    
    if cnd1 & cnd2 & cnd3 & cnd4 & cnd5:
        rpm_short.append(rpm[rad])
        load_short.append(load[rad])
        timing_short.append(timing[rad])
        boost_short.append(boost[rad])
        thr_short.append(thr[rad])
        
print len(rpm)
print len(rpm_short)
        
    
    


    


#Välj segment
start = 0
stop = 1000000
start = max(start,0)
stop = min(stop, len(time))


fig =pylab.figure()
ax1 = Axes3D(fig)

cmhot = plt.cm.get_cmap("hot")
ax1.set_xlabel(header[loadcol], fontsize = 10)
ax1.set_ylabel(header[rpmcol], fontsize = 10)
ax1.set_zlabel(header[timingcol], fontsize = 10)
ax1.scatter(load_short[start:stop],rpm_short[start:stop],timing_short[start:stop], c=boost_short[start:stop])


plt.figure()
plt.scatter(boost,load,c=thr)
plt.colorbar()

plt.legend()
        