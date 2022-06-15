# -*- coding: utf-8 -*-
"""
Created on Fri May 20 07:38:37 2022

@author: ffaraj
"""


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


Ms = pd.Series([400, 400,20,20,0.5,0.5]) #mass in kg

d = pd.Series([25.4,2.54,2.54,0.64,0.64,0.075]) #nominal size in cm

Lm = 4.19
Lg = 2.5
pct_cu = 0.5
aL = (pct_cu/100)/0.345 #Pct cu to chalcopyrite
f = 0.5
g = 0.25
l = 0.05


c = ((1-aL)/aL) * ((1-aL)*Lm+aL*Lg) 

Sfe2 = (c) * f * g * l * d**3 / (Ms*1000)

Sfe = np.sqrt(Sfe2)

S_Fe_1 = (1/(1000*Ms[2]) - 1/(1000*Ms[1])) * (c) * f * g * l * (d[2]**3)

S_Fe_2 = (1/(1000*Ms[4]) - 1/(1000*Ms[3])) * (c) * f * g * l * d[4]**3


S_FE = S_Fe_1+S_Fe_2
print(np.sqrt(S_FE))
#%%


plt.rcParams["font.family"] = "arial"
S=16
lw = 1
plt.rcParams["font.size"] = S
plt.close()
fig, ax = plt.subplots()
fign='Response_Trend'



VARYMASS = np.linspace(0.001,1000000)
Sfe2_1 = (c) * f * g *l * d[1]**3 / (VARYMASS*1000)
Sfe2_2 = (c) * f * g * l * d[3]**3 / (VARYMASS*1000)
Sfe2_4 = (c) * f * g * l * d[5]**3 / (VARYMASS*1000)
Sfe2_6 = (c) * f * g * l * d[0]**3 / (VARYMASS*1000)

plt.plot(VARYMASS,Sfe2_1,linewidth=1,color='k')
plt.plot(VARYMASS,Sfe2_2,linewidth=1,color='k')
plt.plot(VARYMASS,Sfe2_4,linewidth=1,color='k')
plt.plot(VARYMASS,Sfe2_6,linewidth=1,color='k')


plt.plot(Ms,Sfe2,marker='o',mec='k',mfc='w',linewidth=3,ms=11,color='k')


plt.ylabel('Relative variance, $\mathregular{\sigma_{FE}^2}$')
plt.xlabel('Mass [kg]')
plt.xscale('log')
plt.yscale('log')


plt.ylim(2*10**-7,5*10**-1)

plt.xlim(0.01,1000)
plt.xticks([0.01,0.1,1,10,100,1000])
ax.set_xticklabels(['0.01','0.1','1','10','100','1000'])
ax.set_axisbelow(True)
ax.tick_params(axis="both",direction="in",bottom=True, top=True, left=True, right=True,width=lw)
ax.tick_params(which='minor',axis="both",direction="in",bottom=True, top=True, left=True, right=True,width=lw)



ax.grid(axis='both',which='major',alpha=0.75,zorder=0)
ax.grid(which='minor',alpha=0.5,ls='--')

ax.spines['right'].set_linewidth(lw)
ax.spines['top'].set_linewidth(lw)
ax.spines['bottom'].set_linewidth(lw)
ax.spines['left'].set_linewidth(lw)
plt.show()

plt.savefig(fign, bbox_inches='tight', dpi=300,transparent=True)
