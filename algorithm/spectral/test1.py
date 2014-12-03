# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 20:45:37 2014

@author: ui01
"""

import numpy as np
import scipy as sp
from scipy.sparse import linalg

user_size=943
item_size=1682
data=np.genfromtxt('D:/academic/data/facebook-wosn-wall/out.facebook-wosn-wall')
print 'data loaded'

size=user_size+item_size
m=np.zeros((size,size))

a=sp.sparse.lil_matrix((user_size,item_size))

for i in range(data.shape[0]):
    u_idx=data[i,0]-1
    o_idx=data[i,1]-1
    rate=data[i,2]
    a[u_idx,o_idx]=rate

a=np.array(a.todense())

m[0:user_size,user_size:]=a
m[user_size:,0:user_size]=a.T
