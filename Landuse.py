#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:05:00 2020

@author: jentejanssen
"""

import pandas as pd
import matplotlib.pyplot as plt
import itertools
import numpy as np
import seaborn as sns
#import geopandas as gp
#%%

df = pd.read_csv("landcoverWithClassificationNewGhatanji2Okt.csv", header = 0)
df['.geo'] = df['.geo'].map(lambda x: x.lstrip('{"type":"Point","coordinates":[').rstrip(']}'))
df[['X', 'Y']]= df['.geo'].str.split(",", expand=True).astype(float)
#df['averga'] = flow_in.mean()
#df = df.set_index('Index')

landuse = df.drop([#'INLET', 
#                   'PTSOURCE',
#                   'RES', 
                   'system:index', 
                   'bare-coverfraction-stddev','grass-coverfraction-stddev', 'forest_type', 
                   'crops-coverfraction-stddev', 'data-density-indicator','discrete_classification',
                   'discrete_classification-proba','moss-coverfraction', 'moss-coverfraction-stddev', 
                   'shrub-coverfraction-stddev', 'snow-coverfraction', 'tree-coverfraction-stddev', '.geo'], axis = 1)

#%%
def check(landuse):
    if (landuse['urban-coverfraction']>25):
        return 'Not Suitable (urban fraction too large)'
    elif (landuse['crops-coverfraction']<30):
        return 'Not suitable (cropfraction too little)'
    elif (landuse['crops-coverfraction']>30):
        return 'Suitable'
    
landuse['Suitability'] = landuse.apply(check, axis = 1)

#%%

groups = landuse.groupby("Suitability")
#%%
group.sort_values(['crops-coverfraction'], inplace = True, ascending = False)
#%%
colors = itertools.cycle(["r", "b", "g"])
plt.figure(figsize=(10,7))
for name, group in groups:
    plt.plot(group["X"], group["Y"], marker="o", markersize = 3, linestyle="", color=next(colors),  label=name)
plt.legend(loc='upper left', fontsize = 10)
plt.title('Suitability reservoir locations based on land cover constructed locations', fontsize = 16)
plt.xlabel('Longitude', fontsize = 12)
plt.ylabel('Latitude', fontsize = 12)
#plt.savefig("potential locations GG suitability.png")

#%%
landuse.sort_values(['crops-coverfraction'], inplace = True, ascending = False)
landuse[['crops-coverfraction', 'bare-coverfraction', 
          'grass-coverfraction','shrub-coverfraction', 
          'tree-coverfraction', 'urban-coverfraction']].plot(kind='bar', stacked = True, figsize=(15, 8))
plt.ylabel('Cover fraction', fontsize = 20)
plt.title('Coverfraction potential reservoirs Ghatanji block', fontsize = 32)
plt.xlabel('Reservoir number', fontsize = 20)
plt.legend(loc = 'lower left', fontsize = 16)
#plt.savefig('Cover_fraction_potential_GG.png')
#%%
dfs = np.array_split(group, 8) 
dfs_0 = dfs[0]
dfs_1 = dfs[1]
dfs_2 = dfs[2]
dfs_3 = dfs[3]
dfs_4 = dfs[4]
dfs_5 = dfs[5]
dfs_6 = dfs[6]
dfs_7 = dfs[7]

#%%
#fig, axs = plt.subplots(3,1 )
plt.figure()
dfs_0[['crops-coverfraction', 'bare-coverfraction', 
          'grass-coverfraction','shrub-coverfraction', 
          'tree-coverfraction', 'urban-coverfraction']].plot(kind='bar', stacked = True, figsize=(15, 8))
plt.ylabel('Cover fraction', fontsize = 20)
plt.title('Coverfraction potential reservoirs Ghatanji block', fontsize = 32)
plt.xlabel('Reservoir number', fontsize = 20)
plt.legend(loc = 'lower left', fontsize = 16)
plt.savefig('Cover_fraction_GG_suitable_0.png')

dfs_1[['crops-coverfraction', 'bare-coverfraction', 
          'grass-coverfraction','shrub-coverfraction', 
          'tree-coverfraction', 'urban-coverfraction']].plot(kind='bar', stacked = True, figsize=(15, 8))
plt.ylabel('Cover fraction', fontsize = 20)
plt.title('Coverfraction potential reservoirs Ghatanji block', fontsize = 32)
plt.xlabel('Reservoir number', fontsize = 20)
plt.legend(loc = 'lower left', fontsize = 16)
plt.savefig('Cover_fraction_GG_suitable_1.png')

dfs_2[['crops-coverfraction', 'bare-coverfraction', 
          'grass-coverfraction','shrub-coverfraction', 
          'tree-coverfraction', 'urban-coverfraction']].plot(kind='bar', stacked = True, figsize=(15, 8))
plt.ylabel('Cover fraction', fontsize = 20)
plt.title('Coverfraction potential reservoirs Ghatanji block', fontsize = 32)
plt.xlabel('Reservoir number', fontsize = 20)
plt.legend(loc = 'lower left', fontsize = 16)
plt.savefig('Cover_fraction_GG_suitable_2.png')

dfs_3[['crops-coverfraction', 'bare-coverfraction', 
          'grass-coverfraction','shrub-coverfraction', 
          'tree-coverfraction', 'urban-coverfraction']].plot(kind='bar', stacked = True, figsize=(15, 8))
plt.ylabel('Cover fraction', fontsize = 20)
plt.title('Coverfraction potential reservoirs Ghatanji block', fontsize = 32)
plt.xlabel('Reservoir number', fontsize = 20)
plt.legend(loc = 'lower left', fontsize = 16)
plt.savefig('Cover_fraction_GG_suitable_3.png')

dfs_4[['crops-coverfraction', 'bare-coverfraction', 
          'grass-coverfraction','shrub-coverfraction', 
          'tree-coverfraction', 'urban-coverfraction']].plot(kind='bar', stacked = True, figsize=(15, 8))
plt.ylabel('Cover fraction', fontsize = 20)
plt.title('Coverfraction potential reservoirs Ghatanji block', fontsize = 32)
plt.xlabel('Reservoir number', fontsize = 20)
plt.legend(loc = 'lower left', fontsize = 16)
plt.savefig('Cover_fraction_GG_suitable_4.png')

dfs_5[['crops-coverfraction', 'bare-coverfraction', 
          'grass-coverfraction','shrub-coverfraction', 
          'tree-coverfraction', 'urban-coverfraction']].plot(kind='bar', stacked = True, figsize=(15, 8))
plt.ylabel('Cover fraction', fontsize = 20)
plt.title('Coverfraction potential reservoirs Ghatanji block', fontsize = 32)
plt.xlabel('Reservoir number', fontsize = 20)
plt.legend(loc = 'lower left', fontsize = 16)
plt.savefig('Cover_fraction_GG_suitable_5.png')

dfs_6[['crops-coverfraction', 'bare-coverfraction', 
          'grass-coverfraction','shrub-coverfraction', 
          'tree-coverfraction', 'urban-coverfraction']].plot(kind='bar', stacked = True, figsize=(15, 8))
plt.ylabel('Cover fraction', fontsize = 20)
plt.title('Coverfraction potential reservoirs Ghatanji block', fontsize = 32)
plt.xlabel('Reservoir number', fontsize = 20)
plt.legend(loc = 'lower left', fontsize = 16)
plt.savefig('Cover_fraction_GG_suitable_6.png')

dfs_7[['crops-coverfraction', 'bare-coverfraction', 
          'grass-coverfraction','shrub-coverfraction', 
          'tree-coverfraction', 'urban-coverfraction']].plot(kind='bar', stacked = True, figsize=(15, 8))
plt.ylabel('Cover fraction', fontsize = 20)
plt.title('Coverfraction potential reservoirs Ghatanji block', fontsize = 32)
plt.xlabel('Reservoir number', fontsize = 20)
plt.legend(loc = 'lower left', fontsize = 16)
plt.savefig('Cover_fraction_GG_suitable_7.png')

#%%
fig = plt.figure(figsize = (20,10))

ax = dfs_7[['Yield Benefit [kg/y]', 'Benefit [INR/y]']].plot(kind ='bar', secondary_y= 'Benefit [INR/y]', figsize =(11,6))
ax2 = ax.twinx()
ax2.plot(ax.get_xticks(),
         dfs_7[['crops-coverfraction']].values,
         linestyle='-',
         marker='o', markersize = 3, linewidth=2.0, color = 'red', label ='Crop coverfraction [%]')
ax2.legend(loc = 'upper right')
#ax.right_ax.set_ylim(0,6700)
ax2.axes.get_yaxis().set_visible(False)
ax.set_xlabel('Reservoir number', fontsize = 12)
ax.set_ylabel('Yield benefit [kg/y] & Crop coverfraction [%]', color = '#1f77b4', fontsize= 12)
ax.right_ax.set_ylabel('Benefit [INR/y]', color = 'C1', fontsize = 12)
plt.title('Benefit, yield and crop coverfraction per reservoir location in Ghatanji', fontsize = 16)
ax2.set_ylim(0,330)
#plt.savefig('B_Y_CC_GG_7.png')

#%%
small_Y = group.loc[group['Yield Benefit [kg/y]']<100]
med_Y = group.loc[(group['Yield Benefit [kg/y]']>100) & (group['Yield Benefit [kg/y]']<250)]
high_Y = group.loc[group['Yield Benefit [kg/y]']>250]

small_Y.sort_values(['Yield Benefit [kg/y]'], inplace = True)
med_Y.sort_values(['Yield Benefit [kg/y]'], inplace = True)
high_Y.sort_values(['Yield Benefit [kg/y]'], inplace = True)

#%%
#
ax = small_Y[['Yield Benefit [kg/y]', 'Benefit [INR/y]']].plot(kind ='bar', secondary_y= 'Benefit [INR/y]', figsize =(20,10))
ax2 = ax.twinx()
ax2.scatter(ax.get_xticks(),
         small_Y[['crops-coverfraction']].values, marker = "+", color = 'red', label ='Crop coverfraction [%]')
ax.grid()
ax2.legend(loc = 'upper left')
#ax.right_ax.set_ylim(0,1600)
ax2.axes.get_yaxis().set_visible(False)
ax2.set_ylim(0, 100)
ax.set_xlabel('Reservoir number', fontsize = 20)
ax.set_ylabel('Yield benefit [kg/y] & Crop coverfraction [%]', color = '#1f77b4', fontsize= 20)
ax.right_ax.set_ylabel('Benefit [INR/y]', color = 'C1', fontsize = 20)
plt.title('Small increase of yield of potential reservoir locations in Ghatanji', fontsize = 26)
#ax.set_ylim(0,100)

#ax = small_Y[['Yield Benefit [kg/y]', 'Benefit [INR/y]']].plot(kind ='bar', secondary_y= 'Benefit [INR/y]', figsize =(20,10))
#ax2 = ax.twinx()
#ax2.scatter(ax.get_xticks(),
#         small_Y[['averga']].values, marker = "+", color = 'red', label ='Crop coverfraction [%]')
#ax.grid()
#ax2.legend(loc = 'upper left')
ax.right_ax.set_ylim(0,4000)
#ax2.axes.get_yaxis().set_visible(False)
ax2.set_ylim(0, 110)
#ax.set_xlabel('Reservoir number', fontsize = 20)
#ax.set_ylabel('Yield benefit [kg/y] & Crop coverfraction [%]', color = '#1f77b4', fontsize= 20)
#ax.right_ax.set_ylabel('Benefit [INR/y]', color = 'C1', fontsize = 20)
#plt.title('Small increase of yield of potential reservoir locations in Ghatanji', fontsize = 26)
ax.set_ylim(0,110)
plt.savefig('B_Y_CC_GG_small_yield.png')

#%%
ax = med_Y[['Yield Benefit [kg/y]', 'Benefit [INR/y]']].plot(kind ='bar', secondary_y= 'Benefit [INR/y]', figsize =(20,10))
ax2 = ax.twinx()
ax2.scatter(ax.get_xticks(),
         med_Y[['crops-coverfraction']].values, marker = "+", color = 'red', label ='Crop coverfraction [%]')
ax.grid()
ax2.legend(loc = 'upper right')
#ax.right_ax.set_ylim(0,4000)
ax2.axes.get_yaxis().set_visible(False)
ax2.set_ylim(0, 260)
ax.set_xlabel('Reservoir number', fontsize = 20)
ax.set_ylabel('Yield benefit [kg/y] & Crop coverfraction [%]', color = '#1f77b4', fontsize= 20)
ax.right_ax.set_ylabel('Benefit [INR/y]', color = 'C1', fontsize = 20)
plt.title('Medium increase of yield of potential reservoir locations in Ghatanji', fontsize = 26)
ax.set_ylim(0,260)
plt.savefig('B_Y_CC_GG_med_yield.png')

#%%
ax = high_Y[['Yield Benefit [kg/y]', 'Benefit [INR/y]']].plot(kind ='bar', secondary_y= 'Benefit [INR/y]', figsize =(20,10))
ax2 = ax.twinx()
ax2.scatter(ax.get_xticks(),
         high_Y[['crops-coverfraction']].values, marker = "+", color = 'red', label ='Crop coverfraction [%]')
ax.grid()
ax2.legend(loc = 'upper left')
#ax.right_ax.set_ylim(0,8000)
ax2.axes.get_yaxis().set_visible(False)
ax2.set_ylim(0, 500)
ax.set_xlabel('Reservoir number', fontsize = 20)
ax.set_ylabel('Yield benefit [kg/y] & Crop coverfraction [%]', color = '#1f77b4', fontsize= 20)
ax.right_ax.set_ylabel('Benefit [INR/y]', color = 'C1', fontsize = 20)
plt.title('High increase of yield of potential reservoir locations in Ghatanji', fontsize = 26)
ax.set_ylim(0,500)
plt.savefig('B_Y_CC_GG_high_yield.png')

#%%



#%%
group[['crops-coverfraction', 'bare-coverfraction', 
          'grass-coverfraction','shrub-coverfraction', 
          'tree-coverfraction']].plot(kind='bar', stacked = True, 
          figsize = (22,10))
plt.title('Land cover fraction per constructed reservoir', fontsize = 16)
plt.ylabel('Cover fraction', fontsize = 13)
plt.xlabel('Reservoir number', fontsize = 13)
plt.xticks(rotation=90, fontsize = 7)
#%%
landuse.to_csv (r'/Users/jentejanssen/Documents/TU Delft/Water Management/Afstuderen/Locations Solidaridad/Hinganghat/Current locations/Newlocations_GG_landuse_Benefit.csv', index = False, header=True)

#%%
NS_crops = landuse.loc[landuse['Suitability'] == 'Not suitable (cropfraction too little)']
NS_urban = landuse.loc[landuse['Suitability'] == 'Not Suitable (urban fraction too large)']

#%%
NS_crops.sort_values(['crops-coverfraction', 'grass-coverfraction'], inplace = True, ascending = False)

NS_crops[['crops-coverfraction', 
          'bare-coverfraction', 
          'grass-coverfraction',
          'shrub-coverfraction', 
          'urban-coverfraction',
          'tree-coverfraction']].plot(kind='bar', stacked = True, figsize= (20,10))
plt.title('Potential locations where crop-coverfraction < 30%', fontsize = 28)
plt.ylabel('Cover fraction', fontsize = 24)
plt.xlabel('Reservoir number', fontsize = 24)
plt.legend(fontsize = 12)
#plt.xticks(rotation=90, fontsize = 7)
plt.savefig('Cover_fraction_G_not_suitable.png')
#%%
NS_urban.sort_values(['urban-coverfraction'], inplace = True, ascending = False)

NS_urban[['urban-coverfraction',
          'crops-coverfraction', 
#          'bare-coverfraction',
          'tree-coverfraction',
          'shrub-coverfraction',
          'grass-coverfraction']].plot(kind='bar', stacked = True, figsize= (10,5))
plt.title('Potential locations where urban fraction > 25%', fontsize = 12)
plt.ylabel('Cover fraction')
plt.xlabel('Reservoir number')
plt.legend(fontsize = 8)
#plt.xticks(rotation=90, fontsize = 7)
plt.savefig('Cover_fraction_G_not_suitable_urban.png')

#%%
crop_filter = NS_crops.loc[NS_crops['crops-coverfraction'] == 0]
crop_filter.sort_values(['Dist'], inplace = True, ascending = True)

#%%

ax = NS_crops[['crops-coverfraction', 
          'bare-coverfraction', 
          'grass-coverfraction',
          'shrub-coverfraction', 
          'urban-coverfraction',
          'tree-coverfraction']].plot(kind='bar', stacked = True, figsize = (12,6))
ax2 = ax.twinx()
ax2.plot(ax.get_xticks(),
         NS_crops['Dist[m]'].values,
         linestyle='-',
         marker='o', linewidth=2.0, color = 'yellow')
plt.title('Land cover and distance to stream relation potential reservoirs Ghatanji', fontsize = 18)
ax.set_xlabel('Reservoir number', fontsize = 14)
ax.set_ylabel('Coverfraction [%]', fontsize = 14)
ax2.set_ylabel('Distance to nearest stream [m]', fontsize = 14)
ax.legend(loc = 'upper right')
#ax2.set_ylim([0, 6.2])
#ax.set_ylim([0, 100])
#ax2.axhline(y = 0.3, linewidth=3, color='red')
ax.set_xticklabels(NS_crops.index)
plt.savefig('Distance_cropcover_GG.png')
#%%
plt.title('potential reservoirs: cover fraction and distance to nearest stream', fontsize = 26)
ax.legend(['shrub coverfraction', 
          'tree coverfraction','grass coverfraction'], loc = 'upper left', fontsize = 14)
ax.set_xlabel('potential reservoir ID', fontsize = 16)
ax.set_ylabel('Coverfraction', fontsize = 16)
plt.grid(b=None)
ax2.set_ylabel('Distance to nearest stream [km]', fontsize = 16)
plt.savefig("coverfraction_distancetostream_GG.png")

#%%
rejuvenated = crop_filter.loc[crop_filter['Dist[m]'] < 300]
rejuvenated.to_csv (r'/Users/jentejanssen/Documents/TU Delft/Water Management/Afstuderen/Locations Solidaridad/GG_landuse_distance_rejuvenated.csv', index = False, header=True)

#%%
average_sort = landuse.sort_values(['averga'])
average_sort = average_sort.drop([208, 209, 221, 224, 245, 352, 285, 344])

ax = average_sort[['Yield Benefit [kg/y]']].plot(kind='bar', stacked = True, figsize = (20,10))
ax2 = ax.twinx()
ax2.plot(ax.get_xticks(),
         average_sort['averga'].values,
         linestyle='-', linewidth=2.0, color = 'red', label = 'Average inflow')
#ax.axes.get_xaxis(fontsize = 5, rotataion = 90)
#plt.xticks(fontsize = 5)
plt.title('Average inflow and yield benefit Ghatanji block', fontsize = 26)
#ax.legend(['shrub coverfraction', 
#          'tree coverfraction','grass coverfraction'], loc = 'upper left', fontsize = 14)
ax.set_xlabel('Reservoir number', fontsize = 16)
ax2.legend(loc='upper right')
ax.legend(loc='upper left')
ax.set_ylabel('Yield benefit [kg/y]', fontsize = 16)
#plt.grid(b=None)
ax2.set_ylabel('Average inflow [m$^3$]', fontsize = 16)
#ax2.set_ylabel('Crop coverfraction[%]', fontsize = 16)
plt.savefig("Y_inflow_GG.png")

#%%

ax = average_sort[['crops-coverfraction']].plot(kind='bar', stacked = True, figsize = (20,10))
ax2 = ax.twinx()
ax2.plot(ax.get_xticks(),
         average_sort['averga'].values,
         linestyle='-', linewidth=2.0, color = 'yellow')

#%%
small_Y.to_csv(r'/Users/jentejanssen/Documents/TU Delft/Water Management/Afstuderen/Python scripts/small_yield_GG.csv', index = False)

med_Y.to_csv(r'/Users/jentejanssen/Documents/TU Delft/Water Management/Afstuderen/Python scripts/med_yield_H.csv', index = False)
high_Y.to_csv(r'/Users/jentejanssen/Documents/TU Delft/Water Management/Afstuderen/Python scripts/high_yield_GG.csv', index = False)
