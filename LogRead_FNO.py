# -*- coding: utf-8 -*-
"""
Created on Wed May 10 09:50:02 2017

@author: elindgre
"""

import numpy as np
import matplotlib.pyplot as plt
import DIP_API as dip
import FNO_API as fno
from mpl_toolkits.mplot3d import Axes3D



#rpm = myCont.data['SPDRPM']
#inj = myCont.data['InjCtl_qSetUnBal']
#fuelC = myCont.data['BBE']

#filtrera ut där inj är mer än 5 och fuelC mindre än 600

x = myCont.data['SPDRPM'].value
y = myCont.data['InjCtl_qSetUnBal'].value
z = myCont.data['BBE'].value


fig = plt.figure(-1)
fig.clf()
ax = Axes3D(fig)
ax.plot(x,y,z,'.')
ax.set_xlabel('SPDRPM')
ax.set_ylabel('InjCtl_qSetUnBal')
ax.set_zlabel('BBE')

num_x = 10
num_y = 10
myAxisX = np.linspace(min(x),max(x),num_x)
myAxisY = np.linspace(min(y),max(y),num_y)
myAxes=[myAxisX,myAxisY]
myWeight = 200*np.zeros(num_x*num_y)

mySpline = fno.Bspline('BBE', axes=myAxes, weight=myWeight)

myX=np.meshgrid(myAxisX,myAxisY)
myf=300*np.ones(num_x*num_y)
mySpline.add_constraints(myX,'<',myf)

mySpline.add_smoothness(der=[2], lam=1e-2)



opt = fno.Optimization('myOptimization')
opt.set_signal('SPDRPM', x)
opt.set_signal('InjCtl_qSetUnBal', y)
opt.set_signal('BBE', z)
opt.set_function('est_fuel_consump', ['SPDRPM','InjCtl_qSetUnBal'], mySpline)
opt.set_term('err_abs', 'BBE - est_fuel_consump')
sym_blocks = [['est_fuel_consump']]
opt.optimize_weight('err_abs', sym_blocks)
opt.report('err_abs', save=False)

#myAxes = 
#myWeight = 
#mySpline = fno.Bspline('sine_square', axes=myAxes, weight=myWeight)