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

np.random.seed(10)

sample_size=1000
sample=np.random.choice(a=ages,size=sample_size)

sample_mean=sample.mean()

pop_std=ages.std()

z=stats.norm.ppf(q=0.975)

margin_error=z*(pop_std/math.sqrt(sample_size))

confidence_interval=(sample_mean-margin_error,sample_mean+margin_error)

print "confidence interval:" 
print confidence_interval