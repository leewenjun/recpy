# -*- coding: utf-8 -*-
"""
Created on Mon Dec 08 10:35:42 2014

@author: Administrator
"""
import numpy as np
import scipy as sp

def gen_ajacent_from_txt(file,sep=None,start_index=0):
    data=np.genfromtxt(file,delimiter=sep)
    tmp=np.ones((data.shape[0],))
    return sp.sparse.coo_matrix((tmp,(data[:,0]-start_index,data[:,1]-start_index))).toarray()

def nbi(mat):
    sum_u = np.sum(mat,axis=1,keepdims=True)
    sum_o = np.sum(mat,axis=0,keepdims=True)
    tmp=mat/sum_u
    tmp[np.isnan(tmp)]=0.
    t=np.dot(tmp.T,mat)/sum_o
    t[np.isnan(t)]=0.
    p=np.dot(t,mat.T).T
    p[mat>0]=-1
    return p
    
if __name__=='__main__':
    file = r'G:\projects_lwj\data\ml-1m\train.txt'
    mat = gen_ajacent_from_txt(file)
    predition = nbi(mat)
#    print p