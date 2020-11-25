#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:50:49 2020

@author: jentejanssen
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%

CurrentRes=pd.read_csv('landcoverWithClassificationCurrentHH.csv', header=0)
streams =pd.read_csv("Streampoints_Nagpur.csv", header=0)
streams.head()

#%%
streams = streams.drop(['LINKNO',
                        'DSLINKNO', 'USLINKNO1',
              'USLINKNO2',
              'DSNODEID',
              'Order',
              'Length',
              'Magnitude',
              'DS_Cont_Ar',
              'Drop',
              'Slope',
              'Straight_L',
              'US_Cont_Ar',
              'WSNO',
              'DOUT_END',
              'DOUT_START', 
              'DOUT_MID'], axis = 1)
streams.head()

#%%
CurrentRes['New Res ID']=np.zeros(len(CurrentRes))
CurrentRes['Dist[m]']=np.zeros(len(CurrentRes))
for i in range(len(CurrentRes)):
    #Finding closest coordinate for irrigation reservoirs
    DisMat = np.sqrt((CurrentRes['Y'][i] - streams["ycoord"])**2 + (CurrentRes['X'][i] - streams["xcoord"])**2)
    #finding index of min distance
    res_i = DisMat.idxmin()
    #finding coord of min distance
    DistPond=DisMat[res_i]*105000 #degrees to km around lat ~20 degrees north

    CurrentRes['New Res ID'][i]=res_i        
    CurrentRes['Dist[m]'][i]=DistPond      #in km 
    
CurrentRes=CurrentRes.sort_values(by=['Dist[m]'])

CurrentRes.head()

#%%
CurrentRes.to_csv (r'/Users/jentejanssen/Documents/TU Delft/Water Management/Afstuderen/Locations Solidaridad/Hinganghat/Current locations/Current_locations_Landuse_Distance_Wardha_stream.csv', index = False, header=True)
