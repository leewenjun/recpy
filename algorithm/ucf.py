# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import scipy as sp

def gen_ajacent_from_txt(file,user_size=0,item_size=0):
    data=np.genfromtxt(file)
    if user_size==0 or item_size==0:
        u_set=set()
        i_set=set()
        for i in range(data.shape[0]):
            u_set.add(data[i,0])
            i_set.add(data[i,1])
        user_size=len(u_set)
        item_size=len(i_set)
        del u_set
        del i_set
    mat = sp.sparse.lil_matrix((user_size,item_size))
    for i in range(data.shape[0]):
        mat[data[i,0]-1,data[i,1]-1]=data[i,2]
    del data
    return mat
    
    
def gen_cosie_simialrity(mat,normalization=False):
    sim_mat=np.zeros((mat.shape[0],mat.shape[0]))
    for i in range(mat.shape[0]):
        print i
        for j in range(i+1,mat.shape[0]):
#            a=np.array(mat[i,:].todense())
#            b=np.array(mat[j,:].todense())
            a=mat[i,:]
            b=mat[j,:]
            cos = np.dot(a,b.T)/np.linalg.norm(a)/np.linalg.norm(b)
            if normalization:
                cos=0.5+0.5*cos
            sim_mat[i,j]=sim_mat[j,i]=cos
    return sim_mat
    
if __name__=='__main__':
    file = 'G:\\projects_lwj\\data\\movielens-100k\\rel.rating'
    mat = gen_ajacent_from_txt(file,943,1682)
    sim = gen_cosie_simialrity(np.array(mat.todense()))
