# -*- coding: utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt

np.random.seed(3456534)

vec_1=np.array([0,0,0])
cov_mat1=np.array([[1,0,0],[0,1,0],[0,0,1]])
sample_1=np.random.multivariate_normal(vec_1,cov_mat1,20).T


vec_2=np.array([1,1,1])
cov_mat2=np.array([[1,0,0],[0,1,0],[0,0,1]])
sample_2=np.random.multivariate_normal(vec_2,cov_mat2,20).T

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d

fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot(111,projection='3d')
plt.rcParams['legend.fontsize']=10
ax.plot(sample_1[0,:],sample_1[1,:],sample_1[2,:],'o',markersize=8,color='blue',alpha=0.5,label='class_1')
ax.plot(sample_2[0,:],sample_2[1,:],sample_2[2,:],'^',markersize=8,color='red',alpha=0.5,label='class_2')

plt.title('Samples for class 1 and class 2')
ax.legend(loc='upper right')

plt.show()

all=np.concatenate((sample_1,sample_2),axis=1)

mean_x=np.mean(all[0,:])
mean_y=np.mean(all[1,:])
mean_z=np.mean(all[2,:])

mean_vector=np.array([[mean_x],[mean_y],[mean_z]])

print mean_vector