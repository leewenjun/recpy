# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 19:32:39 2014

@author: ui01
"""

import numpy as np
import scipy as sp
from scipy.sparse import linalg

def averageNoZero(a):
    return np.average(a[a!=0])


data=np.genfromtxt('D:/academic/data/facebook-wosn-wall/out.facebook-wosn-wall')
print "loaded"
size=46952

index=np.argsort(data[:,3])
bin_number=75
bin_size=index.size/bin_number

top_k=50

eigenvalues=np.zeros((bin_number*top_k,2))
eigenvectors=np.zeros((bin_number,size,top_k))

for k in range(bin_number):
    print k
    start = 0
    end = (k+1)*bin_size
    
    a=sp.sparse.lil_matrix((size,size))
    for i in range(start,end):
        raw_index=index[i]
        a[data[raw_index,0]-1,data[raw_index,1]-1]=a[data[raw_index,0]-1,data[raw_index,1]-1]+1
        a[data[raw_index,1]-1,data[raw_index,0]-1]=a[data[raw_index,0]-1,data[raw_index,1]-1]
    
    vals,vecs=linalg.eigs(a,k=top_k)
    eigenvalues[k*top_k:(k+1)*top_k,0]=(k+1)*bin_size
    eigenvalues[k*top_k:(k+1)*top_k,1]=vals.real
    eigenvectors[k,:,:]=vecs.real