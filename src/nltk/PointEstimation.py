# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import random
import math

ages_1=stats.poisson.rvs(loc=18,mu=35,size=15000)
ages_2=stats.poisson.rvs(loc=18,mu=10,size=15000)
ages=np.concatenate((ages_1,ages_2))


means=[]

for x in range(200):
    sample=np.random.choice(a=ages,size=500)
    means.append(sample.mean())
    
pd.DataFrame(means).plot(kind="density",figsize=(9,9))   