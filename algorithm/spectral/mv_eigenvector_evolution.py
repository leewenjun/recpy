# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 11:27:04 2014

@author: ui01
"""

import numpy as np
import scipy as sp
from scipy.sparse import linalg
import matplotlib.pyplot as plt

bin_number=75
top_k=50
mat_T = eig_vecs[bin_number-1,:,:]
vals_T = spectral_evolution[top_k*(bin_number-1):,1]
indexs=np.argsort(vals_T)

res = np.zeros((top_k,bin_number-1))

for i in range(0,bin_number-1):
    print i
    mat_t = eig_vecs[i,:,:]
    vals_t=spectral_evolution[top_k*i:top_k*(i+1),1]
    idxs = np.argsort(vals_t)
    
    for j in range(top_k-1,0,-1):
       a = indexs[j]
       b = idxs[j]
       l_T = mat_T[:,a]
       l_t = mat_t[:,b]
       sim=np.abs(np.dot(l_T.T,l_t))
       res[j,i]=sim