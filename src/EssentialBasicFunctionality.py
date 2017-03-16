# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

index=pd.date_range('2016-01-01',periods=8)

s=pd.Series(np.random.randn(5),index=['a','b','c','d','e'])

df=pd.DataFrame(np.random.randn(8,3),index=index,columns=['A','B','C'])

df = pd.DataFrame({'one' : pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
                      'two' : pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
                   'three' : pd.Series(np.random.randn(3), index=['b', 'c', 'd'])})



