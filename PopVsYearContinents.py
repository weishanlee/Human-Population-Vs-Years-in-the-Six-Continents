# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:05:36 2019

@author: Wei Shan Lee
email: weishan_lee@yahoo.com

Description
---------------------------
opulation data vs time of the six continents.
"""
#print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import pandas as pd
#%% After the PopulationVsContinentsMe.xlsx file is done 
PopVsContinents = pd.read_excel("C:/Users/Wei-shan/.spyder-py3" + \
                                "/IMMC2019Int/PopulationVsContinentsMe.xlsx")
PopVsContinents = PopVsContinents.groupby(["Continent"]).sum().T

#plt.figure("Population vs. Years with Various Continents")
ax = PopVsContinents.plot.line(grid=True) 
ax.set_xlabel("Time (year)",size = 16)
ax.set_ylabel("Population Size",size = 16)
plt.minorticks_on()
minorLocatorX = AutoMinorLocator(5)#number of minor intervals per major inteval
minorLocatorY = AutoMinorLocator(5)
ax.xaxis.set_minor_locator(minorLocatorX) # add minor ticks on x axis
ax.yaxis.set_minor_locator(minorLocatorY) # add minor ticks on y axis
plt.show()
plt.savefig("C:/Users/Wei-shan/.spyder-py3/IMMC2019Int" + \
            "/PopulationVsContinentsMe.png")