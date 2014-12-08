# -*- coding: utf-8 -*-
"""
Created on Mon Dec 08 10:35:42 2014

@author: Administrator
"""
import numpy as np
import scipy as sp

def gen_ajacent_from_txt(file,sep=None):
    data=np.genfromtxt(file,delimiter=sep)
    return sp.sparse.coo_matrix((data[:,2],(data[:,0]-1,data[:,1]-1))).toarray()

def nbi(mat):
    sum_u = np.sum(mat,axis=1,keepdims=True)
    sum_o = np.sum(mat,axis=0,keepdims=True)
    tmp=mat/sum_u
    t=np.dot(tmp.T,mat)/sum_o
    p=np.dot(mat,t)
    return p
    
if __name__=='__main__':
    file = 'G:\\projects_lwj\\data\\ml-1m\\ratings.dat'