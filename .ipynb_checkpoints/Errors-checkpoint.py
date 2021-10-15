import pandas as pd 
import numpy as np 
import math 
import scipy.stats
from math import sqrt
import itertools 

def Error_Metrics(avg,testing):
    
    error_metrics=[]
    
    for label in np.arange(0,12):
        data=testing_data[testing_data[:,-1]==label,:-1]
        #print(data.shape)
        averaged_data=avg_data[avg_data[:,-1]==label,:-1]
        #print(averaged_data.shape)

        et = data-averaged_data   
        div = data/averaged_data
        vt = np.var(et) 
        qt = data+averaged_data    
#error metrics
        rmse = np.sqrt(np.mean((et)**2,axis=1))
        mse = np.mean(et**2,axis=1)
        nmse = mse/vt
        mae = np.mean(np.abs(et),axis=1)
        mdae = np.median(np.abs(et),axis=1)
        rmdspe= np.sqrt(100 * np.median(np.abs(div)**2,axis=1))
        nrmse_sd = (rmse/(np.sqrt(vt)))
        sse = np.sum(et**2,axis=1)
        ed = np.sqrt(sse)
        nrmse_m = (rmse/np.mean(et))
        mpe = 100*np.mean(et,axis=1)
        mnb = np.mean(et,axis=1)
        mdspe = 100* np.median(np.abs(div)**2,axis=1)
        error = np.c_[rmse,mse,nmse,mae,mdae,rmdspe,nrmse_sd,sse,ed,nrmse_m,mpe,mnb,mdspe,label*np.ones(data.shape[0])]
        if label ==0:
            error_metrics = error
        else:
            error_metrics = np.concatenate((error_metrics,error),axis=0)
            
    return error_metrics