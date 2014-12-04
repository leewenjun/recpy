# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 09:56:42 2014

@author: Administrator
"""

import pandas as pd
from pandas import Series,DataFrame

rnames=['user_id','movie_id','rating','timestamp']
ratings=pd.read_table(r'G:\projects_lwj\data\ml-1m\ratings.dat',sep='::',header=None,names=rnames)
data=ratings.pivot(index='user_id',columns='movie_id',values='rating')
#corr=data.T.corr(min_period=200)