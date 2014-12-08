# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 15:26:19 2014

@author: Administrator
"""

import numpy as np
import scipy as sp

def gen_ajacent_from_txt(file,sep=None):
    data=np.genfromtxt(file,delimiter=sep)
    mat = sp.sparse.coo_matrix((data[:,2],(data[:,0]-1,data[:,1]-1)))
    return mat.tocsr()
    
def calcu_cosine_similarity(A):
    similarity = np.dot(A, A.T)
    square_mag = np.diag(similarity)

    # inverse squared magnitude
    inv_square_mag = 1 / square_mag
    
    # if it doesn't occur, set it's inverse magnitude to zero (instead of inf)
    inv_square_mag[np.isinf(inv_square_mag)] = 0
    
    # inverse of the magnitude
    inv_mag = np.sqrt(inv_square_mag)
    
    # cosine similarity (elementwise multiply by inverse magnitudes)
    cosine = similarity * inv_mag
    cosine = cosine.T * inv_mag
    cosine-=np.diag(np.diag(cosine))

    return cosine
    
def predict_rate(A,sim,topk=10):
    pre_matrix=np.zeros(A.shape)
    ids=np.argsort(-sim)
    for i in range(A.shape[0]):
        neighbors=ids[i,0:topk]
        sims=sim[i,neighbors]
        rates=A[neighbors,:]
        k=1.0/np.sum(np.abs(sims))
        predicts=k*np.dot(sims,rates)
        pre_matrix[i,:]=predicts
    return pre_matrix 
    
    
def predict_rate_avg(A,sim,topk=10):
    pre_matrix=np.zeros(A.shape)
    ids=np.argsort(-sim)
    
    avgs=np.sum(A,axis=1,keepdims=True)/np.sum(A>0,axis=1,keepdims=True)
    B = A-avgs
    B[A==0]=0
    
    for i in range(A.shape[0]):
        neighbors=ids[i,0:topk]
        sims=sim[i,neighbors]
        rates=B[neighbors,:]
        k=1.0/np.sum(np.abs(sims))
        predicts=avgs[i]+k*np.dot(sims,rates)
        pre_matrix[i,:]=predicts
    return pre_matrix
    
if __name__=='__main__':
#    file = '/Users/liwenjun/projects/data/ml-1m/ratings.dat'
#    mat=gen_ajacent_from_txt(file,'::')
    file = '/Users/liwenjun/projects/data/test.txt'
    mat=gen_ajacent_from_txt(file,'\t')

    cos=calcu_cosine_similarity(mat.toarray())
    p=predict_rate_avg(mat.toarray(),cos,topk=3)