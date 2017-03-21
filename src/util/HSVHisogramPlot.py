'''
Created on 13.03.2017

@author: alex
'''

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import scipy.misc

#close existed
for i in plt.get_fignums():
    print 'has existed'
    plt.close(plt.figure(i))

img = scipy.misc.imread("../../data/images/phone.png")
array=np.asarray(img)
arr=(array.astype(float))/255.0
img_hsv = colors.rgb_to_hsv(arr[...,:3])

lu1=img_hsv[...,0].flatten()
plt.subplot(1,3,1)
plt.hist(lu1*360,bins=360,range=(0.0,360.0),histtype='stepfilled', color='r', label='Hue')
plt.title("Hue")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()

lu2=img_hsv[...,1].flatten()
plt.subplot(1,3,2)                  
plt.hist(lu2,bins=100,range=(0.0,1.0),histtype='stepfilled', color='g', label='Saturation')
plt.title("Saturation")   
plt.xlabel("Value")    
plt.ylabel("Frequency")
plt.legend()

lu3=img_hsv[...,2].flatten()
plt.subplot(1,3,3)                  
plt.hist(lu3*255,bins=256,range=(0.0,255.0),histtype='stepfilled', color='b', label='Intesity')
plt.title("Intensity")   
plt.xlabel("Value")    
plt.ylabel("Frequency")
plt.legend()

manager = plt.get_current_fig_manager()
backend=matplotlib.get_backend()
if backend=='TkAgg':
    manager.resize(*manager.window.maxsize())
elif backend=='QT':
    manager.window.showMaximized()
elif backend=='WX':
    manager.frame.Maximize(True)
else:
    raise ValueError('Unhandled matplotlib backend:'+backend)
    
plt.show()
