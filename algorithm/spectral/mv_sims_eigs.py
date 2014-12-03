# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 09:56:46 2014

@author: ui01
"""

import numpy as np
from scipy.sparse import linalg
import scipy as sp

bin_number=75
top_k=50
bin_size=13336
spectral_evolution = np.zeros((top_k*bin_number,2))

user_size=6040
eig_vecs = np.zeros((bin_number,user_size,top_k))

for k in range(0,bin_number):
    print k
    file='D:/academic/algorithm/spectral/result/sims_%i' % k
    mat = np.loadtxt(file)
    mat[np.isnan(mat)]=0
    a=sp.sparse.csr_matrix(mat)
    val,vec=sp.sparse.linalg.eigs(a,k=top_k)

    spectral_evolution[k*top_k:(k+1)*top_k,0]=bin_size*(k+1)
    spectral_evolution[k*top_k:(k+1)*top_k,1]=val.real
    
    eig_vecs[k,:,:]=vec
    