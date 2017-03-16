# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import random
import math

np.random.seed(1000)

ages_1=stats.poisson.rvs(loc=18,mu=35,size=150000)

ages_2=stats.poisson.rvs(loc=18,mu=10,size=100000)

ages=np.concatenate((ages_1,ages_2))

sample=np.random.choice(a=ages,size=500)


estimates=[]

for x in range(200):
    estimates.append(np.random.choice(a=ages,size=500).mean())
    
pd.DataFrame(estimates).plot(kind='density',figsize=(9,9),xlim=(41,45))    