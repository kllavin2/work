# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 09:53:07 2019
Python script to run  statistics on new extraction control lots
@author: kbeers3
"""
import numpy as np
import scipy.stats as sci
import pandas as pd

#type of control
type_ctrl = "LPC"
#control title
ctrl_title = type_ctrl + ' Extraction Control' 
       
#input files for LPC and HPC
ctrl =open('LPC.txt','r')
    
#hpc_data = open('hpc_data.csv', 'w')
#lpc_data = open('lpc_data.csv', 'w')

#read in line
ctrl_pts = ctrl.read().splitlines()

#create an array of the data:
ctrl_pts_np = np.array(ctrl_pts).astype(np.float)


#calculations for dataset
#calculat mean
mean_ctrl = np.mean(ctrl_pts_np)

#calculate median
med_ctrl = np.median(ctrl_pts_np)

#calculate coefficient of variation
cv_ctrl = sci.variation(ctrl_pts_np)  
#calculate sample variance
sv_ctrl = np.var(ctrl_pts_np)

#calculate the standard dev
std_ctrl = np.std(ctrl_pts_np)

#calculate the standard error
stderr_ctrl = sci.skew(ctrl_pts_np)

#calculate kurtosis
kurt_ctrl = sci.kurtosis(ctrl_pts_np)
#calculate skew
skew_ctrl = sci.skew(ctrl_pts_np)

#calculate min
min_ctrl = np.min(ctrl_pts_np)

#calculate max
max_ctrl = np.max(ctrl_pts_np)

#calcualte sum
sum_ctrl = np.sum(ctrl_pts_np)

#calculate count
cnt_ctrl = np.count_nonzero(ctrl_pts_np)

#calculate range
rng_ctrl = max_ctrl - min_ctrl 

#output file
out_file = 'lpc_data.csv' 


#column names 
col_titles = ( type_ctrl + ' Statistic', type_ctrl +' Result')

#rows of stats
rows =['Mean', mean_ctrl,
       'Median', med_ctrl,
       '%CV', cv_ctrl,
       'Sample Control',sv_ctrl,
       'Standard Deviation', std_ctrl,
       'Standard Error', stderr_ctrl,
       'Kurtosis', kurt_ctrl,
       'Skewness', skew_ctrl,
       'Minimum', min_ctrl,
       'Maximum', max_ctrl,
       'Sum', sum_ctrl,
       'Count', cnt_ctrl,
       'Range',rng_ctrl,]

#convert rows to an array
results = pd.np.array(rows).reshape((len(rows)//2,2))

pd.DataFrame(results, columns = col_titles).to_csv(out_file, index = False)


    