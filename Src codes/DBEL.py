import math 
from math import sqrt
from sklearn import neighbors
import numpy as np 

def KNN(training_data, testing_data, training_y):
    batch_size = 50
    flag = 0
    K = 25
    for label in np.unique(training_y):
        temp10 = testing_data[testing_data['label']==label].values
        temp12 = training_data[training_data['label']==label].values
        temp10 = temp10[:,0:-1]
        temp12 = temp12[:,0:-1]        
        temp13 = np.tile(temp12,(batch_size,1,1))
        print(label)
        for i in range(0, temp10.shape[0], batch_size):
            temp11 = temp10[i:i+batch_size,:]
            if temp11.shape[0]<batch_size:
            #temp13 = np.tile(temp12,(temp11.shape[0],1,1))
                temp13 = temp13[0:temp11.shape[0],:,:]
            distance = (np.square(temp11[:,np.newaxis,:])+np.square(temp13)- 2*np.multiply(temp11[:,np.newaxis,:],temp13))
            distance = np.sum(distance,axis=2)
            idx = np.argpartition(distance,-K,axis=1)[:,-K:]
            averaged_chunk = np.average(temp12[idx,:],axis=1)
            if flag==0:
                averaged_data=averaged_chunk
                preserved_label = np.full((averaged_chunk.shape[0],1),label)
                flag+=1
            else: 
                averaged_data=np.append(averaged_data,averaged_chunk,axis=0)
                preserved_label = np.append(preserved_label,np.full((averaged_chunk.shape[0],1),label))
                preserved_label = np.reshape(preserved_label,(len(preserved_label),1))
    return averaged_data, preserved_label