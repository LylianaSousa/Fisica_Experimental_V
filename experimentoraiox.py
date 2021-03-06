import numpy as np
import scipy as sp
import scipy.interpolate
import matplotlib.pyplot as plt
import pandas as pd

# Reading data
atenenergy = np.array([[85.76,10000],[28.54,15000],[13.08,19998],[80.55,19999],[80.54,20000],[28.1,30000],[12.94,40000],[7.037,50000]])
atenuação = atenenergy[:,0]
energy = atenenergy[:,1]

# Interpolate the data using a cubic spline to energy from the experiment
new_energy = np.array([[10573],[10661],[10750],[10840],[10933],[11026],[11122],[11219],[11318],[11419],[11521],[11625],[11732],[11840],[11951],[12063],[12178],[12295],[12414],[12536],[12660],[12786],[12915],[13047],[13182],[13319],[13460],[13603],[13750],[13899],[14053],[14209],[14369],[14533],[14701],[14873],[15048],[15228],[15413],[15602],[15796],[15994],[16198],[16407],[16622],[16842],[17068],[17301],[17540],[17786],[18038],[18298],[18566],[18842],[19126],[19419],[19721],[20033],[20355],[20687],[21031],[21386],[21753],[22134],[22528],[22936],[23359],[23799],[24255],[24730],[25223],[25736],[26271],[26829],[27411],[28019],[28654],[29319],[30016],[30747],[31514],[32321],[33170],[34065],[35010],[36009],[37067],[38189],[39381],[40650],[42004],[43451],[45002],[46667],[48461],[50398]])
new_atenuação = sp.interpolate.interp1d(energy, atenuação, kind='cubic')
df = pd.DataFrame(columns=['A'])
for i in range(len(new_energy)):
    print(float(new_energy[i]),';',round(float(new_atenuação(new_energy[i])),1))
