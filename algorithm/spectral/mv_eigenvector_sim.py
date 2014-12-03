# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 14:42:10 2014

@author: ui01
"""

import numpy as np
import scipy as sp

#mv-100k
user_size=943
item_size=1682

top_k=50
bin_number=50

#size=user_size+item_size

result = np.zeros((top_k,bin_number))

vals_T=eigenvalues[(bin_number-1)*top_k:,1]
index_T=np.argsort(np.abs(vals_T))

for k in range(bin_number):
    print k
    vals_t=eigenvalues[k*top_k:(k+1)*top_k,1]
    index_t=np.argsort(np.abs(vals_t))
    
    for i in range(top_k-1,-1,-1):
        a1=eigenvectors[-1,:,index_T[i]]
        a2=eigenvectors[k,:,index_t[i]]
        sim=np.abs(np.dot(a1.T,a2)/np.linalg.norm(a1)/np.linalg.norm(a2))
        result[i,k]=sim
        