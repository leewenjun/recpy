# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 10:52:25 2014

@author: ui01
"""
import numpy as np
import scipy as sp
from scipy.sparse import linalg

#mv-100k
user_size=943
item_size=1682
data=np.genfromtxt('D:/academic/data/movielens-100k/rel.rating')
print 'data loaded'

size=user_size+item_size

index=np.argsort(data[:,3])
bin_number=50
bin_size=index.size/bin_number
top_k=50

eigenvalues=np.zeros((bin_number*top_k,2))
eigenvectors=np.zeros((bin_number,size,top_k))

for k in range(0,bin_number):
    print k
    start = 0
    end = (k+1)*bin_size
    
    a=sp.sparse.lil_matrix((size,size))
    for i in range(start,end):
        raw_index=index[i]
        u_idx=data[raw_index,0]-1
        o_idx=data[raw_index,1]-1
        rate=data[raw_index,2]
        a[u_idx,user_size+o_idx]=rate
        a[user_size+o_idx,u_idx]=rate
        
    
    vals,vecs=linalg.eigs(a,k=top_k)
    eigenvalues[k*top_k:(k+1)*top_k,0]=(k+1)*bin_size
    eigenvalues[k*top_k:(k+1)*top_k,1]=vals.real
    eigenvectors[k,:,:]=vecs.real
    