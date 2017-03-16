#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 13:25:37 2016

@author: alex
"""

import pandas as pd

#read two data set
training_set=pd.read_csv("../../data/kaggle/tantic/train.csv",header=0)
test_set=pd.read_csv("../../data/kaggle/tantic/test.csv",header=0)

#concat two data frames
df=pd.concat([test_set,training_set])

#reset index
df.reset_index(inplace=True)

#drop the index generated by reset
df.drop('index',axis=1,inplace=True)

#reindex
df=df.reindex_axis(df.columns,axis=1)
